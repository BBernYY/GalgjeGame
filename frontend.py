# lives is een int met amount levens, letters_wrong is een list met alle verkeerde letters, en word is iets zoals a__le
# probeer een in een prompt zo goed mogelijk deze variabelen te zien
def display_round(lives, words_wrong, word):
    # code
    print("Je hebt nog ", lives, "levens")
    print("Deze letters zitten er niet in: ", letters_wrong)
    return input("ask what letter the player wants to guess" + "\n")
     
    
    