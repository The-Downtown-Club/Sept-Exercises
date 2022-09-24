import json
import itertools

def getInfo(product):
  media = product['media']
  lst = []
  prod_id = product['id'].split('/')[-1]

  for node in media:  #new media
    for cont_type in media[node]: #mediaContentType
      if cont_type['mediaContentType'] == 'VIDEO':
        for items in cont_type['sources']:
          final_dict = {'domain':'oriana-jewels_myshopify_com.json', 'product_id':prod_id}
          final_dict['video_id'] = cont_type['id'].split('/')[-1]
          final_dict['url'] = items['url']
          final_dict['mimeType'] = items['mimeType']
          final_dict['height'] = items['height']
          final_dict['width'] = items['width']
          final_dict['format'] = items['format']
          lst.append(final_dict)
  
  return lst

def process_data(file_name):
    with open(file_name) as f:
        json_data = json.load(f)

    lst = []
    for product in json_data:
        lst.append(getInfo(product))

    lst2 = list(itertools.chain(*lst))
    uniques = list({v['url']:v for v in lst2}.values())
    json_string = json.dumps(uniques)

    with open('/content/j_string.txt', 'w') as f2:
        f2.write(json_string)

f_name = 'sample.json'
process_data(f_name)