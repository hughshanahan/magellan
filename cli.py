

# * Journey
# 1. Authentication + API Session
# 2. User inputs URL
# 3. Run function x on Hugh's code 
# 4. Refactor and add more documentation

import fire
import inquirer
import os
from getkey import getkey
import re

def bye(name="World"):
  return "Bye %s!" % name

def displayMenu():
  menu = [
  inquirer.List('choice',
                message="Menu",
                choices=['RELOAD_FOR_DEBUG', 'Info', 'Login', 'Exit'],
            ),
  ]
  return inquirer.prompt(menu)

# TODO: implement regular expressions to validate input
# TODO: add url query

def displayLogin():
  query = [
    inquirer.Text('username', message="Username"),
    inquirer.Password('password', message="Password"),
    # inquirer.Text('phone', message="What's your phone number",
    #               validate=lambda _, x: re.match('\+?\d[\d ]+\d', x),
    #             )
  ]
  answers = inquirer.prompt(query)
  

# TODO: create and style info page
# TODO: add instantaneous quit option (e.g. press space to quit)
def displayInfo():
  print('lorem ipsum ...jjfkjads;fjdksa;ljf;kldsajf;dsajf;jd;fkj\n')
  temp = True
  print('Press Q to quit')
  while temp:
    key = getkey()
    if key == 'q': temp = False



if __name__ == '__main__':
  temp = True
  reload = False
  while temp:
    os.system('clear')
    choice = displayMenu()['choice']
    os.system('clear')
    match choice:
      case 'Info':
        fire.Fire(displayInfo)
      case 'Login':
        fire.Fire(displayLogin)
      case 'Exit':
        temp = False
      case 'RELOAD_FOR_DEBUG':
        reload = True
        temp = False
    os.system('clear')
  if reload: os.system('python3 cli.py')

