# Date: 09/02/2018
# Author: Mehran
# Description: Instagram Account Checker

from argparse import ArgumentParser
from lib.instagram import Instachecker

def main():
    args = ArgumentParser()
    args.add_argument('usersfile', help='User File')
    args = args.parse_args()
    file = args.usersfile
    checker = Instachecker(file)
    try:
        checker.start()
    except KeyboardInterrupt:
        print('Exiting ...')
        checker.stop()

if __name__ == '__main__':
    main()