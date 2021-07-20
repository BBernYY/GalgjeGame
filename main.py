import random
import frontend as f
import english_words as ew
def round_check(lives, no_letters, word, wordP):
    running = True
    if lives == 0:
        event("die")
    elif not "_" in wordP:
        event("win")
    else:
        return getword(no_letters, word, wordP, f.func(lives, no_letters, wordP), lives)
def getword(no_letters, word, wordP, letter, lives):
    if letter in word:
        wordP[word.index(letter)] = letter
    else:
        no_letters.append(letter)
        lives -= 1
    return {"no_letters": no_letters, "word": word, "wordP": wordP, "lives": lives}
def event(e_type):
    global running
    if e_type == "die":
        print("You died... Sadly...")
    else:
        print("GG! well played!")
    print("Starting next round\n\n")
    running = False
while True:
    d = {}
    d["no_letters"], d["word"], d["wordP"], d["lives"] = 11, [], random.choice(list(ew.english_words_lower_alpha_set)), ""
    for i in len(d["word"]):
        d["wordP"] += "_"
    while running:
        d = round_check(d["lives"], d["no_letters"], d["word"], d["wordP"])
        
        