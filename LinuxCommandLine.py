import os, socket, webbrowser, getpass
from varibles import *


#main loop
while True:
    terminput = input(start)
    terminputx = ''
    terminput = terminput.replace(' ', '\n')
    termlist = terminput.splitlines()
    if terminput == ' ':
        pass
    else:
        if termlist[0] not in commands:
            print(termlist[0] + ': command not found')
        if termlist[0] == 'ls' and currentDirectory == '~':
            print('''
            Desktop    Downloads         Pictures  snap       Videos
        Documents    Music              Public    Templates
        ''')
        if termlist[0] == 'nano' and len(termlist) == 2:
            
            if termlist[1] == '-www.letsparty.com':
                
                notsecret = getpass.getpass('-www.letsparty.com is not a regsterd flag. Click Enter to exitp: ')
                
                if notsecret == '54321KABOOM':
                    print('Welcome to Menu. For security, your input is not shown.')
                     notsecret = getpass.getpass('> ')

                     if notsecret == 'change':
                         notsecret = getpass.getpass('> ')

                        if notsecret == 'userperm':

                        if user == '$':
                            user = '#'
                        else:
                            user = '$'
            else:

                print('Opening nano. When finished, type \'exit\' and click Enter to exit')
                webbrowser.open(nanopath)
        
        if termlist[0] == 'cd' and len(termlist) == 2:
            
            if termlist[1] in home:
                currentPath += '/' + termlist[1]
                currentDirectory = termlist[1]
            
            if termlist[1] == '..':
                if currentDirectory in home:
                    currentDirectory = '~'
                    currentPath = '~'
        
        if termlist[0] == 'mkdir' and len(termlist) == 2:
            
            if currentDirectory == '~':
                termlist.append(termlist[1])

        start = login + '@' + hostname + ':' + currentPath + user + ' '

    

