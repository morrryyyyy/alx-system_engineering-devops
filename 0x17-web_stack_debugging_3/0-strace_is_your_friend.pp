# Ensure the document root directory exists
file { '/var/www/html/mysite':
  ensure  => 'directory',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
}

# ensure that an index file exists in that directory
file { '/var/www/html/mysite/index.html':
  ensure  => 'file',
  content => '<html><body><h1>Welcome to MySite</h1></body></html>',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# Restart Apache to apply the changes
service { 'apache2':
  ensure     => 'running',
  enable     => true,
  subscribe  => File['/var/www/html/mysite'],
}
