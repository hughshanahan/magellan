import sys
import os
import json

from rich.text import Text
from rich.console import Console
from bs4 import UnicodeDammit

console = Console()

'''
[D] DESCRIPTION | runs a URL request on the parameter country and saves the response to path in JSON format
[I] INPUT       | { url: string, country: string, path: string }
[R] RETURNS     | dictionary of specific parts of the HTTP response (url, status_code, headers, text)
[T] RETURN TYPE | dictionary
'''
def runCountry(url, country, path):
  if sys.version_info[0]==3:
    import urllib.request
    import random
    username = cid
    password = psw
    port = 22225
    session_id = random.random()
    super_proxy_url = ('http://%s-country-%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %
        (username, country, session_id, password, port))
    proxy_handler = urllib.request.ProxyHandler({
        'http': super_proxy_url,
        'https': super_proxy_url,
    })

    opener = urllib.request.build_opener(proxy_handler)
    r = opener.open(url)
    
    header_info = r.getheaders()

    status_code = r.getcode()
    dct = dict((x, y) for x, y in header_info)

    # Used to improve decoding of websites with unicode characters
    new_doc = UnicodeDammit.detwingle(r.read()) 
    text = new_doc.decode('utf-8')

    requestData = { 
        "url": r.url,
        "status_code": status_code,
        "headers": dct,
        "text": text
    }

    countryPath = os.path.join(path, f"{country}.json")
    with open(countryPath, "w") as outfile:
        json.dump(requestData, outfile)

  return requestData



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