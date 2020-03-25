english = ['chicken', 'salt', 'apple', 'earth', 'bean', 'water', 'milk',
           'man', 'god', 'search', 'mango', 'car', 'fuel', 'cake', 'body']
french = ['poulet', 'sel', 'pomme', 'terre', 'haricot', 'eau', 'lait', 'homme',
          'dieu', 'chercher', 'mangue', 'voiture', 'carburant', 'gâteau', 'corps']
print("Program to translate words from English to French and vice-versa")
print(" ")

while 1:
    print(" ")
    word = input("Enter an English or French word to translate : ").lower()
    result = ""

    if word == "":
        print("Exiting ...")
        break

        # checking  word in french
    if word in french:

        index = french.index(word)
        result = english[index]
        print(f"The French word '{word}' is '{result}' in English")

        # checking word in english
    elif word in english:
        index = english.index(word)
        result = french[index]
        print(f"The English word '{word}' is '{result}' in French")

        # if entered word is not found in english or french
    else:
        print(
            f"The word '{word}' was not found in English or French word lists")

        print(
            f"Would you like to add {word} to the lists? <y>es or <n>o ", end=" ")
        y = input().lower()
        if y == "y":

            print(f"What language {word} in? <E>nglish or<F>rench", end=" ")
            l = input()
            if l.lower() == "e":
                english.append(word)
                print(f"What is the French word for '{word}' ? ", end=" ")
                newResult = input().lower()
                french.append(newResult)
            elif l.lower() == "f":
                french.append(word)
                print(f"What is the English word for '{word}' ? ", end=" ")
                newResult = input().lower()
                english.append(newResult)
            else:
                print("error : ", end=" ")
                print(f"You enter '{l}' ehich is not avilable ")
        elif y == "n":
            continue

    # VARIABLE USED

    # word => IT CONTAINS USER INPUT OF WORD
    # result => IT CONTAINS TRANSLATED WORD
    # l => IT CONTAINS INPUT LANGUAGE
    # newResult => IT CONTAINS TRANSLATED NEW WORD
    # english AND french are list which contains corresponding word in each language
