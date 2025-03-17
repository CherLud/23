import requests
from bs4 import BeautifulSoup
import pandas as pd
from operator import itemgetter

url = f'https://www.kinoafisha.info/online/movies/'
html_content = requests.get(url).text

soup = BeautifulSoup(html_content, 'lxml')

entries = soup.find_all('div', class_='movieList_item movieItem movieItem-grid grid_cell3')
data = []
for entry in entries:
    td_film_details = entry.find('div', class_='movieItem_info')
    film_name = td_film_details.find('a').text

    film_genre = entry.find('span', class_='movieItem_genres').text

    release_date = entry.find('span', class_='movieItem_year').text

    rating = entry.find('span', class_='mark_num').text

    data.append({'film_name': film_name, 'film_genre': film_genre, 'release_date': release_date, 'rating': rating})

df = pd.DataFrame(data)
df.to_excel('user_rates_all.xlsx')

data1 = sorted(data, key=itemgetter('rating'), reverse=True)
print(f'ТОП 20 фильмов с высшим рейтингом:\n {data1[:20]}')
df = pd.DataFrame(data1[:20])
df.to_excel('user_rates_top20.xlsx')

