import requests
from pprint import pprint
 
apiKey = 'e0f758a29c10735363824aadd696a09a' 
 
City = input("Enter the city: ")
BaseUrl = "https://api.openweathermap.org/data/2.5/weather?appid=" + apiKey+"&q="+City

weatherData = requests.get(BaseUrl).json()

pprint(weatherData)