import requests

def hasShopify(d_name):
  d_name = d_name.lower().replace(' ','')
  # has_schema = False
  schema = d_name.split('/')
  found_msg = 'Shopify domain exist for '
  notfound_msg = 'Shopify domain not found for '

  if schema[0] == 'http:' or schema[0] == 'https:':
    # has_schema = True
    pass
  elif len(schema) == 3:
    d_name = 'https://' + schema[2]
  else:
    d_name = 'https://' + schema[0]

  url = d_name
  try:
    r = requests.get(url+'/admin')
    if 'myshopify' in r.url.split('.'):
      print(found_msg + url)
    else:
      print(notfound_msg + url)
  except Exception as e:
    print(notfound_msg + url)

hasShopify('happyratio.com/')
