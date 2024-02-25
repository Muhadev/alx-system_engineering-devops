# Puppet Manifest for creating a file in /tmp/school
# Configures file permissions, owner, and group.
file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
