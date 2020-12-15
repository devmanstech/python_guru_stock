from dotenv import load_dotenv  #for loading environment variables
import os
import requests

# read personal token
load_dotenv('.env')
token = os.getenv("TOKEN")

url = 'https://www.gurufocus.com/api/public/user/' + token + '/stock/AAPL/quote'

result = requests.get(url)

print(result.content)
