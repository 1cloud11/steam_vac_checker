import requests
import xml.etree.ElementTree as et
from settings import STEAM_API_KEY

user_url = 'https://steamcommunity.com/id/alex_pimenov/'

def get_userinfo(user_data):
    user_url_xml = user_data + '?xml=1'
    root = et.fromstring(requests.get(user_url_xml).content)
        
    steamid64 = root.find('steamID64').text
    steam_name = root.find('steamID').text
    vac = root.find('vacBanned').text
    print(f'SteamID: {steamid64}')
    print(f'Ник пользователя на момент репорта {steam_name}')
    print(f'Количество VAC-банов: {vac}')

    json_url = 'http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=' + STEAM_API_KEY + '&steamids=' + steamid64
    params = {
        'format': 'json',
    }

    result = requests.get(json_url, params=params)
    json_data = result.json()
    #След конструкция возвращает False, нужно посмотреть что не так
    if 'players' in json_data:
        if 'DaysSinceLastBan' in json_data['players']:
            try:
                last_vac = json_data['players']['DaysSinceLastBan']
                print(f'С последнего VAC-бана прошло {last_vac}')
            except(IndexError, TypeError):
                return False
    return False

if __name__ == "__main__":
    g = get_userinfo(user_url)
    print(g)

    #Создать список словарей, в который будет вносится новый словарь в случае добавления юзера.
    #Словарь в виде {'steamid': steamid, 'steam_name': steam_name, {'VAC': True, 'VAC_count': int, 'last_VAC': timedelta, }
    #Перед внесением юзера программа должна проверить по steamid, нет ли уже такого юзера в списке. Если есть - программа должна получить новые данные по VAC, и сообщить, были ли изменения.
    #Если изменений нет - отразить старую информацию, если есть - обозначить, что информация новая (дописать New), и указать новую.
    #








"""GetPlayerBans (v1)

GetPlayerBans returns Community, VAC, and Economy ban statuses for given players.

Example URL: http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=XXXXXXXXXXXXXXXXX&steamids=XXXXXXXX,YYYYY """