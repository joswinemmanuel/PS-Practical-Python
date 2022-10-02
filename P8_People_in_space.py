import requests

count = 1

people = requests.get("http://api.open-notify.org/astros.json")
json = people.json()

print("People now in space are : ")
for p in json["people"]:
    print(count, p["name"])
    count += 1


# People now in space are : 
# 1 Oleg Artemyev
# 2 Denis Matveev
# 3 Sergey Korsakov
# 4 Kjell Lindgren
# 5 Bob Hines
# 6 Samantha Cristoforetti
# 7 Jessica Watkins
# 8 Cai Xuzhe
# 9 Chen Dong
# 10 Liu Yang
# 11 Sergey Prokopyev
# 12 Dmitry Petelin
# 13 Frank Rubio