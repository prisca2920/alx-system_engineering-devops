# executing a command
exec { 'pkill':
  command => 'pkill killmenow',

}
