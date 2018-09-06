#web scrape example

import requests
import bs4

#download the web page
resp = requests.get('http://www.nasdaq.com')
try:
    resp.raise_for_status()
except Exception as e:
    print('There is a problem: %s' % (e))
print(resp.status_code)

textInputAttrib = bs4.BeautifulSoup(resp.text, "html.parser")
elems = textInputAttrib.select('input[name]')
print("\nThere are {} elements of type '<input>[name]'".format(len(elems)))

print("====== List all INPUT elements =====")
#print all items in list
for item in elems:
    print(item)
    
print("\n\n====== List all INPUT attributes =====")
#print the item attributes
for item in elems:
    print(item.attrs)

print("\nThe End.")
