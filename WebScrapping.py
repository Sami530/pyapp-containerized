import requests
from bs4 import BeautifulSoup as bs

githubUser = input('Enter Github User: ')
url = 'https://github.com/'+githubUser 
p=requests.get(url)
soup =bs(p.content,'html.parser')

ProfileImg = soup.find( 'img',{'alt':'Avatar'})['src']

print(ProfileImg) 
