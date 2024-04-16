import requests
api = 'e82eacb212c5f2ff09188300ee4511bc'
input = input("Enter city: ")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={input}&units=imperial&APPID={api}")
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    data = weather_data.json() 
    weather = data['weather'][0]['main']
    temp = round(data['main']['temp'])
    humidity = data['main'] ['humidity']
    pressure = data['main'] ['pressure']

    print(f"The weather in {input} is: {weather}")
    print(f"The temperature in {input} is: {temp}ºF")
    print(f"The humidity in {input} is: {humidity} g/m³")
    print(f"The pressure in {input} is: {pressure} Pa")