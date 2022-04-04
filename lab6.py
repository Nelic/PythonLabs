import requests
import re
from bs4 import BeautifulSoup

req = requests.get("https://news.ycombinator.com/newest")

page = BeautifulSoup(req.text, 'html.parser')
print("There are " + str(len(page.findAll('a'))-1) + " references")
print("There are " + str(len(page.findAll("img"))-1) + " images")

tagRate = input("Input tag ")
print("Tag rate for " + tagRate + " is " + str(len(page.findAll(tagRate))))

wordRate = input("Input word ")
results = page.find_all(string=re.compile('.*{0}.*'.format(wordRate)), recursive=True)

print("Word rate of word " + wordRate + " is " + str(len(results)))

# print(page(text=wordRate))