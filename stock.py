from dotenv import load_dotenv  #for loading environment variables
import os
import requests
import csv
import json

# read personal token
load_dotenv('.env')
token = os.getenv("TOKEN")

#read csv file
file = 'Book1.csv'

with open(file) as symbols:
    readCSV = csv.reader(symbols)
    for symbol in readCSV:
    
        url = 'https://www.gurufocus.com/api/public/user/' + token + '/stock/' + symbol[0] + '/quote'

        # get response json data.
        result = requests.get(url)

        if result.status_code == requests.codes.ok:
                
            result_array = json.loads(result.content.decode('ascii'))

            # extract price
            price = result_array['price']
            currency = result_array['currency']
            print(price)
            print(currency)
        




