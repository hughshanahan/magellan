
# * Journey
# 1. Authentication + API Session
# 2. User inputs URL
# 3. Run function x on Hugh's code 
# 4. Refactor and add more documentation

import json
import os
import re
from click import style

#? Dependencies that need to be installed using pip install
import inquirer #! (v2.8.0, as of yet no fix for backspace input error)
from getkey import getkey 
from yaspin import yaspin 
import pyfiglet
from pyfiglet import figlet_format
from rich import print
from rich.console import Console
from rich.text import Text
from rich.traceback import install
from rich.markdown import Markdown


install() #implements custom traceback styling || Rich
console = Console() #creates new rich console || Rich

# Provides styling options for the inquirer list menu
script_dir = os.path.dirname(__file__)
file_path1 = os.path.join(script_dir, 'inqTheme.json')
f = open(file_path1)
theme_data = json.load(f)
customInq = inquirer.themes.load_theme_from_dict(theme_data)

#
file_path2 = os.path.join(script_dir, 'info.md')
f = open(file_path2, 'r')
md = Markdown(f.read())
f.close()

""" Displays main menu

-> returns the user selection in dictionalry form (e.g. "choice" : "Info")
"""
def displayMenu():
  menu = [
  inquirer.List('choice',
                message="MENU",
                choices=['RELOAD_FOR_DEBUG', 'Info', 'Login', 'Exit'],
            ),
  ]
  return inquirer.prompt(menu, theme=customInq)

# TODO: implement validation for customerID and password
def displayLogin():
  questions = [
    inquirer.Text('accountID', message="CustomerID"),
    inquirer.Password('password', message="Password"),
    inquirer.Text('url', message="URL",validate=validate_url),
  ]
  answer = inquirer.prompt(questions)

def validate_url(answer, current):
  regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

  if not re.match(regex, current):
    raise inquirer.errors.ValidationError("", reason='ERROR: invalid URL format -> expected https://www.example.com')
  
  return True
  
# - myConfig known components: zone, customer, password

# TODO: create and style info page
def displayInfo():
  console.print(figlet_format('fair data', font = 'isometric3'), style="bold green")
  console.print(md)
  
  # Exit info page
  print('\nPress Q to return back to the Menu: ')
  key = ''
  while key != 'q':
    key = getkey().lower()


if __name__ == '__main__':
  temp = True
  reload = False

  os.system('clear')
  displayInfo()
  os.system('clear')
  print('wagwan')
  while temp:
    os.system('clear')
    choice = displayMenu()['choice']
    os.system('clear')
    
    match choice:
      case 'Info':
        displayInfo()
      case 'Login':
        displayLogin()
      case 'Exit':
        temp = False
      case 'RELOAD_FOR_DEBUG':
        reload = True
        temp = False
    os.system('clear')

  if reload: os.system('python3 ~/Develop/pythonCLI/src/cli.py')

