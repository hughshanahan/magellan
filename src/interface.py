
# * Journey
# 1. Authentication + API Session
# 2. User inputs URL
# 3. Run function x on Hugh's code 
# 4. Refactor and add more documentation

# TODO: adding content to the info page
# TODO: adding styling to the info page
# TODO: figuring out how to resolve different error codes while logging in


import json
import os
import re
import requests as r
from datetime import datetime

#? Dependencies that need to be installed using pip install
import inquirer #! (v2.8.0, as of yet no fix for backspace input error)
import iso3166
from getkey import getkey
from yaspin import yaspin 
from yaspin.spinners import Spinners
from pyfiglet import figlet_format
from rich import print
from rich.console import Console
from rich.text import Text
from rich.traceback import install
from rich.markdown import Markdown
from rich.table import Table


# ! Credentials for BrightData proxy service (temporary)
# lum-customer-c_0abac4c6-zone-static
# 2s7c5n20jxn5

install() # implements custom traceback styling || rich.traceback
console = Console() # creates new rich console || rich.console

isLogedIn = True # global boolean to check if user is logged in

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



""" 
[D] DESCRIPTION | requests the url and prints a table of results and saves the results to a file
[I] INPUT       | { url: string containing the url }
"""
def requestURL(url):
  countries = []
  table = Table()


  table.add_column("Code", style="cyan", no_wrap=True)
  table.add_column("Country", style="magenta")
  table.add_column("Status", justify="right", style="blue")
  table.add_column("Description", style="red")


  for c in iso3166.countries_by_alpha2.keys():
    countries.append(c.lower())
  countries.sort()

  if not os.path.exists('responses'):
    os.mkdir('responses')

  requestTime = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
  requestPath = os.path.join('responses', requestTime)
  analysisPath = os.path.join(requestPath, 'analysis')
  summaryPath = os.path.join(requestPath, 'summary.txt')
  os.mkdir(requestPath)
  os.mkdir(analysisPath)

  counter = 1
  with yaspin(Spinners.earth, text='Loading...', color='yellow') as spinner:
    for c in countries:
      country_full = iso3166.countries_by_alpha2[c.upper()].name
      spinner.text = f'[{counter}/{len(countries)}]  Loading ' + c.upper() + '...'

      try:
        data_dict = r.runCountry(url, c, analysisPath)
        status_code = data_dict['status_code']
        table.add_row(c.upper(), country_full, f"{status_code} ✅")
      except Exception as e:
        description = str(e.args[0])
        table.add_row(c.upper(), country_full, "Failed ❌", description)

      counter+=1
    spinner.stop()

  console.print(table)
  
  with open(summaryPath, 'w') as w:
    try:
      w.write(print(table, file=w))
    except TypeError as e:
      pass
  
  exitPage()



""" 
[D] DESCRIPTION | displays main menu 
[I] INPUT       | { choices: list of choices to display }
[R] RETURNS     | user's choice
[T] RETURN TYPE | dictionary (e.g. "choice" : "Info")
"""
def displayMenu(choices):
  menu = [
  inquirer.List('choice',
                message="MENU",
                choices=choices,
            ),
  ]
  return inquirer.prompt(menu, theme=customInq)



""" 
[D] DESCRIPTION | displays the request prompt to the user
[R] RETURNS     | user's answers to the url query
[T] RETURN TYPE | dictionary (e.g. "url" : "https://www.google.com")
"""
def displayRequest():
  questions = [
    inquirer.Text('url', message="URL",
    # validate=validate_url # ! temporary
    ),
  ]
  answer = inquirer.prompt(questions, theme=customInq)  

  requestURL(answer['url'])


# TODO: add a way to display the return code of login errors
""" 
[D] DESCRIPTION | displays login promt to the user
[R] RETURNS     | user's answers to the 3 queries
[T] RETURN TYPE | dictionary (e.g. "url" : "https://www.google.com")
"""
def displayLogin():
  global isLogedIn

  questions = [
    inquirer.Text('accountID', message="CustomerID"),
    inquirer.Password('password', message="Password"),
  ]
  answer = inquirer.prompt(questions, theme=customInq)  

  if r.validate_user(answer['accountID'], answer['password']):
    print('Logging In...')
    isLogedIn = True
  else: 
    print('Failed to Log in')
  input() # ! pause for user to read



""" 
[D] DESCRIPTION | validates the url
[I] INPUT       | { answer: dictionary containing pervious user input } 
                  { current: string that represents user input i.e. url }
[R] RETURNS     | True if input is valid, else raises exception
[T] RETURN TYPE | boolean / exception
"""
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
  


""" 
[D] DESCRIPTION | displays the markdown file with all of the essential information
"""
def displayInfo():
  console.print(figlet_format('fair data', font = 'isometric3'), style="bold yellow")
  console.print(md)
  exitPage()
  


""" 
[D] DESCRIPTION | a widget to allow user to exit a page
"""
def exitPage():
  qText = Text('\n\nPress Q to return back to the Menu: ')
  qText.stylize("bold green", 0, 9)
  console.print(qText)

  key = ''
  while key != 'q':
    key = getkey().lower()



"""
[D] DESCRIPTION | main function
"""
if __name__ == '__main__':
  temp = True
  reload = False
  loggedIn = ['RELOAD_FOR_DEBUG', 'Info', 'Run', 'Logout', 'Exit']
  loggedOut = ['RELOAD_FOR_DEBUG', 'Info', 'Login', 'Exit']

  while temp:
    os.system('clear')
    x = loggedIn if isLogedIn else loggedOut
    choice = displayMenu(x)['choice']
    os.system('clear')
    
    match choice:
      case 'Info':
        displayInfo()
      case 'Login':
        displayLogin()
      case 'Logout':
        isLogedIn = False
      case 'Run':
        displayRequest()
      case 'Exit':
        temp = False
      case 'RELOAD_FOR_DEBUG':
        reload = True
        temp = False

  if reload: os.system('python3 ~/Develop/pythonCLI/src/interface.py')