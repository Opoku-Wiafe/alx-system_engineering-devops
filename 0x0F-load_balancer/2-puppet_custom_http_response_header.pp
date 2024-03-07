#!/usr/bin/env bash
# Install Nginx (if not already installed)
package { 'nginx':
  ensure => installed,
}

# Config Nginx
class { 'nginx':
  # Your Nginx configuration settings go here
}

# Add custom HTTP header
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => present,
  content => "add_header X-Served-By $::hostname;",
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure => running,
  enable => true,
}
