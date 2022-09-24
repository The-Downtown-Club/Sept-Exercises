
import requests
def yesno(url):
    try:
        r = requests.get(url, timeout=4)
        
        newstr = r.url
        print(newstr)

        newspl = newstr.split('.')
        print(newspl)

        if('myshopify' in newspl):
            print("YES")

        else:
            print("NO")
    
    except:
        print("NO")

def shopify(url):   
    
    ustr = url
    
    spl = ustr.split('/')
    print(spl)

    if (spl[0] == 'http:' or spl[0] == 'https:' ):
        yesno(url)
    else:
        url = "https://"+ url
        yesno(url)

ip_url = input("Enter URL : ")

shopify(ip_url + "/admin")



