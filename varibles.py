import os, socket

commands = ['cd', 'ls', 'nano', 'mkdir']
currentPath = '~'
home = {
    'contentList' : ['Desktop'],
    'Desktop' : {
        'Type' : 'Folder',
        'Pemissions' : [3,3,3],
        'Contents' : {}
    }
}
rootcmd = False
login = os.getlogin()
hostname = socket.gethostname()
currentDirectory = '~'
if rootcmd:
    start = login + '@' + hostname + ':' + currentDirectory + '#' + ' '
else:
    start = login + '@' + hostname + ':' + currentDirectory + '$' + ' '
nanopath = 'file://' + os.getcwd() + '/files/nano.html'