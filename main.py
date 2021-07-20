import random
import frontend as f
import english_words as ew
def round_check(lives, no_letters, word, wordP):
    if lives == 1:
        event("die", word)
    elif not "_" in wordP:
        event("win", word)
    else:
        return getword(no_letters, word, wordP, f.func(lives, no_letters, wordP), lives)
def getword(no_letters, word, wordP, letter, lives):
    if letter in word:
        s = list(wordP)
        s[word.index(letter)] = letter
        wordP = "".join(s)
    else:
        no_letters.append(letter)
        lives -= 1
    return {"no_letters": no_letters, "word": word, "wordP": wordP, "lives": lives}
def event(e_type, word):
    global running
    if e_type == "die":
        print("You died... Sadly...")
        print("The word was "+word)
    else:
        print("GG! well played!")
    print("Starting next round\n\n")
    running = False
while True:
    d = {}
    d["no_letters"], d["word"], d["wordP"], d["lives"] = [], random.choice(list(ew.english_words_lower_alpha_set)), "", 11
    for i in range(len(d["word"])):
        d["wordP"] += "_"
    running = True
    while running:
        d = round_check(d["lives"], d["no_letters"], d["word"], d["wordP"])