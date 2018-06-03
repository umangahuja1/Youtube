import requests


def by_city():
    city = input('Enter your city : ')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid= your api key here &units=metric'.format(city)
    res = requests.get(url)
    data = res.json()
    show_data(data)


def by_location():
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]

    url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid= your api key here &units=metric'.format(latitude, longitude)
    res = requests.get(url)
    data = res.json()
    show_data(data)



def show_data(data):
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    description = data['weather'][0]['description']

    print()
    print('Temperature : {} degree celcius'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Description : {}'.format(description))


def main():
    print('1. Get data By city')
    print('2. Get data By location')
    choice = input('Enter your choice : ')

    if choice == '1':
        by_city()

    else:
        by_location()    

if __name__ == '__main__':
    main()
    
