import os, socket, webbrowser

commands = ['cd', 'ls', 'nano']
currentDirectory = '~'
user = '$'
login = os.getlogin()
hostname = socket.gethostname()
start = login + '@' + hostname + ':' + currentDirectory + user + ' '

#main loop
while True:
    terminput = input(start)
    terminputx = ''
    terminput = terminput.replace(' ', '\n')
    termlist = terminput.splitlines()
    if termlist[0] not in commands:
        print(termlist[0] + ': command not found')
    if termlist[0] == 'ls' and currentDirectory == '~':
        print('''
        Desktop    Downloads         Pictures  snap       Videos
    Documents    Music              Public    Templates
    ''')
    if termlist[0] == 'nano' and len(termlist) == 2:
        print('Opening nano')
        webbrowser.open('file:////media/zane/AC66-1723/python/linuxcommandline/files/nano.html')
    

