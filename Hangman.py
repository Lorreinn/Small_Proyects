'''
Nombre: Esther Ramírez
Fecha: 19/6/23
Contacto: estherrz2996@gmail.com

'''

keyword = "palabra"
keywordlist = []
for letra in keyword:
    keywordlist.append(letra)
print(keywordlist)    

keywordlist_2 = [letra for letra in keyword]
print(keywordlist_2)

keywordlist_3 = [*keyword]
print(list(set(keywordlist_3)))

user_choice = input("Introduce una letra: ")
