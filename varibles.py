import os, socket

commands = ['cd', 'ls', 'nano']
currentPath = '~'
user = '$'
login = os.getlogin()
hostname = socket.gethostname()
currentDirectory = '~'
start = login + '@' + hostname + ':' + currentDirectory + user + ' '
home = ['Desktop', 'Downloads', 'Pictures', 'snap', 'Videos', 'Documents', 'Music', 'Public', 'Templates']#

