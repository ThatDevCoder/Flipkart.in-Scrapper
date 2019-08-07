import urllib3
import requests
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
user_input = input("What you want to search on flipkart.in")
URL='https://www.flipkart.com/search?q='+user_input
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content , 'html.parser')
links = soup.find_all("a", class_="_2cLu-l")
price = soup.find_all("div" , class_="_1vC4OE")
for link in links[:5]:
    title = link.get('title')
    print(title)
for prices in price[:5]:
    print(prices.text)
