

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
def displayInfo():
  print('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ipsum orci, consectetur quis feugiat a, venenatis in nibh. Phasellus dignissim varius libero vitae pellentesque. Curabitur molestie erat magna, eu volutpat mi efficitur in. Curabitur vitae nisl at dolor congue elementum quis ac elit. Fusce at lorem ut mauris efficitur eleifend id eget lorem. Pellentesque sapien libero, cursus sed ipsum a, interdum pretium risus. Phasellus ornare ultricies elementum. Integer venenatis eleifend urna eu accumsan. Praesent tempor dui non eros consectetur facilisis. Fusce volutpat congue elit eu elementum. Nullam dapibus velit quam, in aliquet mi volutpat at. Nulla eget varius ex. Curabitur nec diam maximus, hendrerit nulla non, viverra felis. Nullam facilisis eget augue id posuere. Nam finibus erat vitae sapien sodales, fringilla tempus odio dictum. Ut quis dolor malesuada, consectetur ipsum at, auctor nulla.Donec eget accumsan neque, et varius mauris. Suspendisse eget felis ut risus rhoncus egestas vitae et metus. Nullam venenatis nisi augue, eu volutpat diam semper sed. Suspendisse potenti. Pellentesque congue lobortis ligula vel posuere. Aenean feugiat eros at interdum aliquam. Duis mattis felis quis purus finibus aliquam. Proin egestas nunc vel nulla ornare mollis. Donec fermentum massa ut dignissim feugiat. Curabitur aliquam dictum ex ut feugiat. Nulla aliquam convallis porttitor. Ut vehicula felis eu mauris viverra vestibulum. Nullam luctus scelerisque placerat. In eu nisi sit amet odio varius rutrum eu tincidunt nisl.Nulla non efficitur ligula, a hendrerit sem. Proin ipsum eros, vulputate id lorem non, dapibus cursus enim. Quisque suscipit ut dolor ut euismod. Nulla tristique, elit in aliquet sagittis, urna orci lobortis justo, ut lacinia leo felis sit amet augue. Donec pulvinar a erat quis volutpat. Duis vestibulum sollicitudin lacus ut egestas. Nam eu semper neque, nec malesuada lacus. Nullam vel leo congue neque ornare iaculis at ut ipsum. Curabitur sit amet enim lobortis, ornare lorem sed, pulvinar nisi. Suspendisse vel vulputate urna. Aliquam vulputate nisi magna, a congue felis gravida in. Praesent consectetur metus eu dolor vulputate, quis malesuada neque sodales. Suspendisse quis dapibus leo.Praesent laoreet, neque sit amet euismod laoreet, ex risus lacinia massa, et venenatis ipsum dolor eget elit. Fusce vitae est eu ligula pellentesque lobortis. Sed et imperdiet massa, sed efficitur nibh. Nulla semper vulputate felis sit amet congue. In vulputate mi dolor, consequat congue ipsum tristique non. Aenean luctus finibus nulla. Sed sit amet vulputate mauris. Nam et justo et dolor tempus ultricies. Nam tempor, ante sed euismod efficitur, massa lectus feugiat orci, vitae consectetur nulla neque quis ex. Etiam dignissim semper arcu, et faucibus nulla ullamcorper vitae. In vulputate est nec mi vulputate sollicitudin. Maecenas luctus, massa eu sollicitudin auctor, nisl mi malesuada velit, et faucibus ex tortor non orci. Duis rutrum est quis ipsum rutrum, eu tincidunt augue pulvinar.Praesent pretium in felis et bibendum. Donec varius vulputate nisl sed tincidunt. Praesent facilisis blandit ex, quis pellentesque mi ullamcorper quis. Integer placerat elit orci, sed facilisis justo pharetra nec. Mauris tempus nisl sed urna rutrum, et commodo ex tempor. Curabitur ac tincidunt lorem. Cras mattis eleifend tortor vel mollis. Sed dolor lorem, congue eget laoreet id, posuere quis lectus.\n')
  
  print('Press Q to return back to the Menu: ')
  key = ''
  while key != 'q':
    key = getkey().lower()



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

