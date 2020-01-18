commands = ['cd', 'ls', 'nano']
currentDirectory = '~'
user = '$'
login = os.getlogin()
hostname = socket.gethostname()
start = login + '@' + hostname + ':' + currentDirectory + user + ' '
home = ['Desktop', 'Downloads', 'Pictures', 'snap', 'Videos', 'Documents', 'Music', 'Public', 'Templates']
