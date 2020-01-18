import os, socket, webbrowser
from varibles import *


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
    if termlist[0] == 'cd' and len(termlist) == 2:
        if termlist[1] in home:
            currentPath += '/' + termlist[1]
            currentDirectory = termlist[1]
         if termlist[1] == '..':
            if currentDirectory in home:
                currentDirectory = '~'
                currentPath = '~'
    start = login + '@' + hostname + ':' + currentPath + user + ' '

    

