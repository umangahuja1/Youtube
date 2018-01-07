import urllib.request

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Muralitharan_bowling_to_Adam_Gilchrist.jpg/499px-Muralitharan_bowling_to_Adam_Gilchrist.jpg'

urllib.request.urlretrieve(url, 'cricket.jpg')
