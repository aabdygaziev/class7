a = {"Aktan": {"name": "Aktan", "age": "26", "city": "Bishkek", "country": "KG", "sex": "M"},
     "Sergei": {"name": "Sergei", "age": "26", "city": "Bishkek", "country": "KG", "sex": "M"}}
print(a['Aktan'])

'#new_list'

c = {}
while True:
    n1 = input()
    if n1 == "add":
        name = input()
        c[name] = {"age": input(), "city": input(), "country": input(), "sex": input()}
    elif n1 == "remove":
        n2 = input()
        if n2 in c:
            del c[n2]
    elif n1 == "get":
        print(c)
    elif n1 == "get by name":
        n2 = input()
        print(c[n2])
    


