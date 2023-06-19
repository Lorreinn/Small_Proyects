'''
Nombre: Esther Ramírez
Fecha: 19/6/23
Contacto: estherrz2996@gmail.com

'''
def generate_displaykeyword(keyword, keywordlist):
    """display_keyword es la propia keyword pero cambiando las palabras que no conocemos por "_" """
    display_keyword = keyword 
    for letra in keywordlist:
        display_keyword = display_keyword.replace(letra, "_")    
    return display_keyword

#Part1: Check the words.
keyword = "palabra"
lifes = 5
correct_users_letters = []
keywordlist = []

for letra in keyword:
    keywordlist.append(letra)
    
keywordlist_2 = list(set([letra for letra in keyword]))

keywordlist_3 = [*keyword]

#Part 2: Ask the user for a letter.
while (len(keywordlist_2) > 0) and (lifes > 0) :
    #Part 5: Feedback.
    print(generate_displaykeyword(keyword, keywordlist_2))
    user_choice = input("Introduce una letra: ").lower()

    #Part 3: Check the letter is correct.
    if user_choice in keywordlist_2:
        print("Correct")
        #Part 4: Update the words list.
        keywordlist_2.remove(user_choice)
        #print(keywordlist_2)
        #print(len(keywordlist_2))
    else:
        lifes-=1
        print("Lost a life")
        print(f"Now you have {lifes} lifes")

#Part 5: Feedback.
