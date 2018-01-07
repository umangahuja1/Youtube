from bs4 import BeautifulSoup
import requests

choice = {
    '1': 'english',
    '2': 'hindi',
    '3': 'punjabi',
    '4': 'bengali',
    '5': 'gujarati'
}


def print_choice():
    for sno in sorted(choice):
        print('{}. {}'.format(sno, choice[sno]))
    ch = input('Enter your choice (1-5) : ')
    return choice[ch]


def get_songs(lang):

    res = requests.get('https://www.saavn.com/s/featured/' + lang + '/Weekly_Top_Songs')

    soup = BeautifulSoup(res.text, 'lxml')

    data = soup.find('ol', {'class': 'content-list'})
    all_songs = data.find_all('div', {'class': 'details'})
    return all_songs


def print_songs(all_songs):
    for count, s in enumerate(all_songs, 1):
        song = s.find('p', {'class': 'song-name'})
        print(count, song.text)


def saavn_songs():
    lang = print_choice()
    all_songs = get_songs(lang)
    print_songs(all_songs)


saavn_songs()
