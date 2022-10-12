import requests

def check_url(url):
  try:
    response = requests.get(url, timeout=2)
  except Exception as e:
    return False
  else:
    return True

def hasShopify(d_name):
  host_name = d_name.lower().replace(' ','').split('//')[-1]
  found_msg = 'Shopify domain exist for '
  notfound_msg = 'Shopify domain not found for '

  url_https = 'https://' + host_name
  if check_url(url_https):
    url = url_https
  else:
    url_http = 'http://' + host_name
    url = url_http
  
  try:
    response = requests.get(url+'/admin', timeout=2)
    if 'myshopify' in response.url.split('.'):
      return found_msg + url
    else:
      return notfound_msg + url
  except Exception as e:
    return notfound_msg + url

url_list = ['https://happyratio.com/',
'www.clayventures.in',
'http://merojewellery.in',
'http://jivikanaturals.com',
'https://www.tribeshop.com',
'http://heroku.projectoptimal.com/',
'http://breadandbeta.com/']

for url in url_list:
  print(hasShopify(url))