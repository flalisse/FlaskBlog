import requests


#define global variables
city = "Praha"
appiKey = '98bab0ed96648da85a1b6ef8e5e8f79b'

#retrieve current information about prague
def getcurrentInfo():

    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}".format(city,appiKey))

    if response.status_code == 200:
        response_json= response.json()
        print('succes')
        print(response_json)
        current_temp = response_json['main']['temp']
        current_speed_wind = response_json['wind']['speed']

        current_temp_in_celsius = current_temp - 273.15
        print(current_temp_in_celsius, current_speed_wind)
        return current_temp_in_celsius, current_speed_wind

    elif response.status_code == 404:
        print("request Failed")


if __name__ ==  '__main__':
    getcurrentInfo()
