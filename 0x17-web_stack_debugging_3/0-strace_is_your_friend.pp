# debugging the .phpp code to fix it in wp-settings.php
exec { 'fix wordpress':
  command     => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
