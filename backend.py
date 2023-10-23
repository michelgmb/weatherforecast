import requests
import pandas as pd
import json

df = pd.read_json('city.list.json')
# print(df.head())
# print(df.columns)

api_key = api_key
#city = "Toronto"
#days = 5


# API_city_ID= "api.openweathermap.org/data/2.5/forecast?id={city ID}&appid={API key}"
# url = "https://api.openweathermap.org/data/2.5/forecast?id=524901&appid=4dbb51ed104ec589614d61d8fcdcd301"


def get_data(city, days ):
    # url = f"https://api.openweathermap.org/data/2.5/forecast?id={city_ID}&appid={api_key}"
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(url)
    content = response.json()
    number_obser =  8*days
    filtered =  content['list'][:number_obser]


    filtered_days =  filtered  #  [dict for dict in filtered[0] ]

    #numbers = days *

    return filtered_days #, filtered


if __name__ == '__main__':
 print(get_data('Toronto', 2))
