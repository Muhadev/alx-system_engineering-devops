# kill_process.pp

exec { 'killmenow_process':
  command => '/usr/bin/pkill -f "killmenow"',
  path    => ['/usr/bin', '/bin'],
  onlyif  => '/usr/bin/pgrep -f "killmenow"',
  require => Package['procps'], # Ensure the procps package is installed
}

package { 'procps':
  ensure => installed,
}
