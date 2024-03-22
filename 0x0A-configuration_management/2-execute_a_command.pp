# executing a command

# pkill in action
exec { 'pkill':
  command => 'pkill killmenow',
}
