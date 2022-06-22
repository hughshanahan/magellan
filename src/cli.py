
# * Journey
# 1. Authentication + API Session
# 2. User inputs URL
# 3. Run function x on Hugh's code 
# 4. Refactor and add more documentation

import json
import os
import re
from xmlrpc.client import boolean
from click import style
import sys
import ssl

#? Dependencies that need to be installed using pip install
import inquirer #! (v2.8.0, as of yet no fix for backspace input error)
import iso3166
from getkey import getkey
from numpy import void
import requests 
from yaspin import yaspin 
from pyfiglet import figlet_format
from rich import print
from rich.console import Console
from rich.text import Text
from rich.traceback import install
from rich.markdown import Markdown

# lum-customer-c_0abac4c6-zone-unblocker
# u6lk0tgc5mfo

install() # implements custom traceback styling || rich.traceback
console = Console() # creates new rich console || rich.console

# * Provides styling options for the inquirer list menu
script_dir = os.path.dirname(__file__)
file_path1 = os.path.join(script_dir, 'inqTheme.json') 
f = open(file_path1)
theme_data = json.load(f)
customInq = inquirer.themes.load_theme_from_dict(theme_data)

# * Import markdown file used in displayInfo()
file_path2 = os.path.join(script_dir, 'info.md')
f = open(file_path2, 'r')
md = Markdown(f.read())
f.close()



def requestURL(url):
  """ 
  [D] DESCRIPTION | requests the url and returns the response
  """

  countries = []
  for c in iso3166.countries_by_alpha2.keys():
    countries.append(c.lower())

  for c in countries:
      print("Starting run on " + c)
      # runCountry(c,path)
      print("Finished run on " + c)
      # doneCountries.append(c)
      # updateDoneCountries(doneCountries)
      print('you have requested url ' + url)
      print(customerID + ' ' + pswrd)


def displayMenu():
  """ 
  [D] DESCRIPTION | displays main menu 
  [R] RETURNS     | user's choice
  [T] RETURN TYPE | dictionalry (e.g. "choice" : "Info")
  """

  menu = [
  inquirer.List('choice',
                message="MENU",
                choices=['RELOAD_FOR_DEBUG', 'Info', 'Login', 'Exit'],
            ),
  ]
  return inquirer.prompt(menu, theme=customInq)



# TODO: implement validation for customerID and password
def displayLogin():
  """ 
  [D] DESCRIPTION | displays login promt to the user
  [R] RETURNS     | user's answers to the 3 queries
  [T] RETURN TYPE | dictionary (e.g. "url" : "https://www.google.com")
  """

  questions = [
    inquirer.Text('accountID', message="CustomerID"),
    inquirer.Password('password', message="Password"),
    inquirer.Text('url', message="URL",validate=validate_url),
  ]
  answer = inquirer.prompt(questions, theme=customInq)  
  
  global customerID, pswrd 
  customerID= answer['accountID']
  pswrd = answer['password']

  validate_user()

  # requestURL(answer['url'])

def testURL(url):
    # * Auth for BrightData proxy service 
  if sys.version_info[0]==3:
    import urllib.request
    import random
    username = customerID 
    password = pswrd
    port = 22225
    session_id = random.random()
    super_proxy_url = ('http://%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %
        (username, session_id, password, port))

    proxy_handler = urllib.request.ProxyHandler({
        'http': super_proxy_url,
        'https': super_proxy_url,
    })
    opener = urllib.request.build_opener(proxy_handler)
    print('Performing request')
    try:
      opener.open(url).read()
    except urllib.request.HTTPError as e:
      return False

    return True



def validate_user():
  """ 
  [D] DESCRIPTION | validates the user's credentials
  """
  global isValidUser
  isValidUser = False

  isValidUser =  testURL('http://www.youtube.com')

  print(isValidUser)
  input()
  return isValidUser



def validate_url(answer, current):
  """ 
  [D] DESCRIPTION | validates the url
  [I] INPUT       | { answer: dictionary containing pervious user input } 
                    { current: string that represents user input i.e. url }
  [R] RETURNS     | True if input is valid, else raises exception
  [T] RETURN TYPE | boolean / exception
  """

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
  """ 
  [D] DESCRIPTION | displays the markdown file with all of the essential information
  """

  console.print(figlet_format('fair data', font = 'isometric3'), style="bold yellow")
  console.print(md)
  exitPage()
  


def exitPage():
  """ 
  [D] DESCRIPTION | a widget to allow user to exit a page
  """

  qText = Text('\n\nPress Q to return back to the Menu: ')
  qText.stylize("bold green", 0, 9)
  console.print(qText)

  key = ''
  while key != 'q':
    key = getkey().lower()



if __name__ == '__main__':
  temp = True
  reload = False

  # os.system('clear')
# displayInfo()~
  # os.system('clear')

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

  if reload: os.system('python3 ~/Develop/pythonCLI/src/cli.py')