import requests
import xml.etree.ElementTree as et
from settings import STEAM_API_KEY

user_url = "https://steamcommunity.com/id/1cloud/"

def get_userinfo(user_url):
    user_url_xml = user_url + "?xml=1"
    root = et.fromstring(requests.get(user_url_xml).content)
        
    steamid64 = root.find("steamID64").text #steamid
    steam_name = root.find("steamID").text #steamname
    vac = root.find("vacBanned").text #VAC_count

    json_url = "http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=" + STEAM_API_KEY + "&steamids=" + steamid64
    params = {
        "format": "json",
    }

    result = requests.get(json_url, params=params)
    json_data = result.json()

    if "players" in json_data:
        try:
            last_vac = json_data["players"][0]["DaysSinceLastBan"]
        except(IndexError, TypeError):
            return 'Возникла ошибка'
    
    user_info = {
        "steamID64": steamid64, 
        "steamname": steam_name, 
        "VAC": vac, 
        "DaysSinceLastBan": last_vac
        }

    return user_info

if __name__ == "__main__":
    g = get_userinfo(user_url)
    print(g)

    #Создать список словарей, в который будет вносится новый словарь в случае добавления юзера.
    #Список словарей записывать в файл.txt
    #Запрос поступает боту тг, имя файла = tg_user_id.txt
    #Перед внесением юзера программа должна проверить по steamid, нет ли уже такого юзера в списке. Если есть - программа должна получить новые данные по VAC:
    #   Если есть:
    #   - [SteamID: ...]
    #   - [Steam_name: Name (New name)]
    #   - [VAC: ... (New +..)]
    #   - [DaysSinceLastBan: ...]
    #   Если нет:
    #   - отразить старую информацию
    #
    #
