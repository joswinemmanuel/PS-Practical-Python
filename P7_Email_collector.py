contacts = {
    "number" : 4,
    "students" :
    [
        {"name" : "Marie T J", "email" : "mtj@example.com"},
        {"name" : "Ron P Joe", "email" : "ron@example.com"},
        {"name" : "Alaina Marie Joe", "email" : "amj@example.com"},
        {"name" : "Bibin T", "email" : "bibt@example.com"},
        {"name" : "Baki Hanma", "email" : "baki@example.com"},
    ]
}

for student in contacts["students"]:
    print(f'Email : {student["email"]}')


# Email : mtj@example.com
# Email : ron@example.com
# Email : amj@example.com
# Email : bibt@example.com
# Email : baki@example.com