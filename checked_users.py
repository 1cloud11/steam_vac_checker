
user_info = {'steamID64': '76561198021543621', 'steamname': 'TANK', 'VAC': '0', 'DaysSinceLastBan': 0}
f_playerid = '4c568fce-ef08-4e4d-a90d-3b0da03a6a35'

with open('test.txt', 'a') as f:
    content = f.read()
    f.write(user_info)



