

# * PLAN
# 1. Authentication + API Session
# 2. User inputs URL
# 3. Run function x on Hugh's code 
# 4. Refactor and add more documentation

import fire
from getpass import getpass
import argparse

def test():
  return "Hello, this is a test!"

def bye(name="World"):
  return "Bye %s!" % name
  

if __name__ == '__main__':
  username = input("Username:\n")
  password = getpass()
  url = input('What website do you want to check?\n')

  temp = True
  while temp:
    inp = input()
    if inp == 'q' or inp == 'exit':
      temp = False
    else :
      print('I am here')
      fire.Fire()

