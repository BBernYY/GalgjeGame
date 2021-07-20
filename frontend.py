# lives is een int met amount levens, letters_wrong is een list met alle verkeerde letters, en word is iets zoals a__le
# probeer een in een prompt zo goed mogelijk deze variabelen te zien
def func(lives, letters_wrong, word):
    # code
    string = ""
    for i in list(word):
        string += i+" "
    print(string)
    print("You've got", lives, "lives")
    print("These letters aren't in there:", letters_wrong)
    return input("Please guess a letter." + "\n")
     
    
    