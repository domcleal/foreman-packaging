#!/usr/bin/env ruby
#
# Converts %{?scl_prefix}rubygem-foo in a load of spec files to use a different scl_prefix variant
# Used when moving from a single SCL to multiple, as it's configurable for different packages to
# have different scl_prefixes.

def lookup_table
  return @table if @table
  @table = {}
  File.read(File.expand_path('scl_prefix_update.conf', File.dirname(__FILE__))).each_line do |l|
    k,v = l.chomp.split('=')
    @table[k] = v
  end
  @table
end

def lookup(string)
  return lookup_table[string] if lookup_table.has_key?(string)
  if string =~ /\Arubygem[(-]([\w-]+)\)?\z/
    return lookup_table[$1] if lookup_table.has_key?($1)
  end
  raise("unknown #{string}")
end

def replace(file)
  file.gsub(/(%{\??)scl_prefix}([\w%{}()-]+)/) { |m| "#{$1}#{lookup($2)}}#{$2}" }
end

def add_obsoletes(file, filename)
  old_name = `rpm --define 'scl ruby193' --qf '%{name}\n' -q --specfile #{filename}`.split($/).first
  old_name = $1.gsub(/%{\??scl_prefix}/, 'ruby193-') if file =~ /^Name:\s*(.+?)\s*$/
  file.sub!(/((?:^Provides:[^\n]+$\s*)+)/m) { "#{$1}Obsoletes: #{old_name}\n\n" } if old_name.include?('ruby193')
  file
end

raise 'Usage: scl_prefix_update.rb FILE..' if ARGV.empty?

ARGV.each do |a|
  begin
    File.write(a, add_obsoletes(replace(File.read(a)), a))
  rescue => e
    puts "parsing #{a}"
    raise e
  end
end
