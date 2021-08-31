import requests
import xml.etree.ElementTree as et
from webapp.config import STEAM_API_KEY, FACEIT_API_KEY


def get_steamdata(steam_user_url):
    #Getting steam info
    try:
        steam_user_url_xml = steam_user_url + "?xml=1"
        root = et.fromstring(requests.get(steam_user_url_xml).content)
        steamid64 = root.find("steamID64").text #steamid
        steam_name = root.find("steamID").text #steamname
        vac = root.find("vacBanned").text #VAC_count
        
        json_url = "http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=" + STEAM_API_KEY + "&steamids=" + steamid64
        result = requests.get(json_url, params={"format": "json",})
        steam_json_data = result.json()
        last_vac = steam_json_data["players"][0]["DaysSinceLastBan"]
        
        steam_user_info = {
            "steamID64": steamid64, 
            "steamname": steam_name, 
            "VAC": vac, 
            "DaysSinceLastBan": last_vac}
        return steam_user_info
    except AttributeError:
        return "User not found."


def get_faceitdata(steamid64):
    first_faceit_url = "https://open.faceit.com/data/v4/players?game=csgo&game_player_id="+steamid64
    headers = {
               "accept": "application/json",
               "Authorization": f"Bearer {FACEIT_API_KEY}",
              }
    faceit_info = requests.get(first_faceit_url, headers=headers).json()
    faceit_id = faceit_info["player_id"]
    faceit_name = faceit_info["nickname"]
    faceit_level = faceit_info["games"]["csgo"]["skill_level_label"]
    faceit_elo = faceit_info["games"]["csgo"]["faceit_elo"]
    
    faceit_user_info = {        
                        "FACEITID": faceit_id,
                        "FACEIT_NAME": faceit_name,
                        "FACEIT_LEVEL": faceit_level,
                        "FACEIT_ELO": faceit_elo,
                       }
    return faceit_user_info


def total_user_data():
    steam_data = get_steamdata(input("Введите ссылку на профиль steam: "))
    faceit_data = get_faceitdata(steam_data["steamID64"])
    total_user_info = {**steam_data, **faceit_data}
    return total_user_info

# 'https://steamcommunity.com/id/1cloud/'
print(total_user_data())