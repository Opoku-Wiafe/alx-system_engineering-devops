# fix the server and make it work well
exec { 'update ulimit':
  command  => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 15000\"/' /etc/default/nginx",
  provider => 'shell',
}

-> exec { 'restart':
  command  => 'service nginx restart',
  provider => 'shell',
}
