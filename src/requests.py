import sys
import os
import json


'''
[D] DESCRIPTION | runs a URL request on the parameter country and saves the response to path in json format
[I] INPUT       | { url: string, country: string, path: string }
[R] RETURNS     | dictionary of specific parts of the HTTP response (url, status_code, headers, text)
[T] RETURN TYPE | dictionary
'''
def runCountry(url, country, path):
  url='https://youtube.com' # ! temporary
  if sys.version_info[0]==3:
    import urllib.request
    import random
    username = 'lum-customer-c_0abac4c6-zone-static'
    password = '2s7c5n20jxn5'
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

    requestData = { 
        "url": r.url,
        "status_code": status_code,
        "headers": dct,
        "text": r.read().decode('utf-8')
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
    print('Performing request')
    try:
      opener.open('http://youtube.com').read()
    except urllib.request.HTTPError as e:
      # match e.code:
      #   case 401:
      #     print('blacklisted_ip')
      #   case 407:
      #     print('wrong_credentials')
      print(e)
      return False
    global cid, psw
    cid = customerID
    psw = password
    return True