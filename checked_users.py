
user_info = {'steamID64': '76561198021543621', 'steamname': 'TANK', 'VAC': '0', 'DaysSinceLastBan': 0}

with open('test.txt', 'a') as f:
    content = f.read()
    f.write(user_info)



