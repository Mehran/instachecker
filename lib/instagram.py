# Date: 09/02/2018
# Author: Mehran
# Description: Instagram Account Checker

import requests
from colorama import Fore
from time import sleep

class Instachecker:

    def __init__(self,file):
        self.count = 0
        self.line_count = 0
        self.url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36', 'cookie': 'mcd=3; shbid=5597; ig_cb=1; mid=W4PfJAAEAAE1DGjnE45SEwFztzbV; csrftoken=P8DvqEB5AxkRuWyoNWhrZ3Bi2scbrVm9; csrftoken=P8DvqEB5AxkRuWyoNWhrZ3Bi2scbrVm9; rur=PRN', 'x-csrftoken': 'P8DvqEB5AxkRuWyoNWhrZ3Bi2scbrVm9'}
        self.usersfile = file
        self.is_alive = True

    def start(self):
        with open(self.usersfile, 'rt') as f:
            allLines = f.readlines() 
        self.line_count = len(allLines)
        for line in allLines:
            self.count += 1
            if not self.is_alive:break  # when the user presses Ctrl + C, self.is_alive will become False
            username = line.strip()
            self.check_account(username)

    def check_account(self,username):
        redo = True
        while redo:
            data = {'password':'mypass', 'email':'myemailherer@mail.com', 'username':username, 'first_name':'Mehran+Mehrani'}
            r = requests.post(url = self.url, headers = self.headers, data = data)
            responde = r.text
            if ('"error_type": "form_validation_error"' in responde):
                redo=False
                print('{}[+]Trying ({}/{}) -{}{} Username: {} Taken{}'.format(Fore.WHITE, self.count, self.line_count, Fore.RESET, Fore.RED, username, Fore.RESET))
            elif ('Please wait a few minutes before you try again.' in responde):
                print('{}[+]Blocked , Waiting 1min and retry ...{}'.format(Fore.YELLOW, Fore.RESET))
                sleep(90)
            else:
                redo=False
                print('{}[+]Trying ({}/{}) -{}{} Username: {} Available{}'.format(Fore.WHITE, self.count, self.line_count, Fore.RESET, Fore.GREEN, username, Fore.RESET))
                with open('available.txt', 'a') as f:
                    f.write(username + '\n' )

    def stop(self):
        self.is_alive = False