import sys
import os
import json

from rich.text import Text
from rich.console import Console
from bs4 import UnicodeDammit

console = Console()

'''
[D] DESCRIPTION | runs a URL request on the parameter country and saves the response to path in JSON format
[I] INPUT       | { url: string, country: string }
[R] RETURNS     | dictionary of specific parts of the HTTP response (url, status_code, headers, text)
[T] RETURN TYPE | dictionary
'''
def runCountry(url, country):
  url = 'http://youtube.com'
  if sys.version_info[0]==3:
    import urllib.request
    import random
    username = "lum-customer-c_0abac4c6-zone-static"
    password = "2s7c5n20jxn5"
    port = 22225
    session_id = random.random()
    super_proxy_url = ('http://%s-country-%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %
        (username, country, session_id, password, port))
    proxy_handler = urllib.request.ProxyHandler({
        'http': super_proxy_url,
        'https': super_proxy_url,
    })
    opener = urllib.request.build_opener(proxy_handler)

    try:
      r = opener.open(url)
    except Exception as e:
      headers = dict((x, y) for x, y in e.headers.items())
      return {'url': url, 'status_code': e.code, 'headers': headers, 'text': e.reason}


    headers = dict((x, y) for x, y in r.getheaders())
    text = UnicodeDammit.detwingle(r.read()) # Used to improve decoding of websites with unicode characters

    return { 
        "url": r.url,
        "status_code": r.getcode(),
        "headers": headers,
        "text": text.decode('utf-8')
    }
  else:
    print("Python version is not supported, please upgrade to Python 3")



""" 
[D] DESCRIPTION | validates the user's credentials
[I] INPUT       | { customerID: string containing user's customerID }
                  { password: string containing user's password }
[R] RETURNS     | True if user's credentials are valid, else False
[T] RETURN TYPE | boolean
"""
def validate_user(customerID, password):
  # * Auth for BrightData proxy service 
  if sys.version_info[0]==3:
    import urllib.request
    import random
    username = customerID 
    password = password
    port = 22225
    session_id = random.random()
    super_proxy_url = ('http://%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %
        (username, session_id, password, port))

    proxy_handler = urllib.request.ProxyHandler({
        'http': super_proxy_url,
        'https': super_proxy_url,
    })
    opener = urllib.request.build_opener(proxy_handler)
    try:
      opener.open('http://youtube.com').read()
    except urllib.request.HTTPError as e:
      if e.code == 407:
        text = Text('\n\nAuthentication failed, please try again')
        text.stylize("bold red")
        console.print(text)
        return False
      elif e.code == 403:
        text = Text('\nIP has been disabled, please whitelist your IP in the brightdata.com portal')
        text.stylize("bold yellow")
        console.print(text)
        return False
      else:
        print(e.code)
      pass
    
    # Creating global variables storing user's credentials after confirming validity
    global cid, psw
    cid = customerID
    psw = password
    
    return True