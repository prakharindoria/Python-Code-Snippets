import random
def player_input():
        mydict={
        'penury':"poverty",
        'vicarious':"secondhand",
        'ephemeral':"impermanant",
        'euphemism':"circumlocution",
        'badinage':"banter",
        'bovine':"placid",
        'nostalgia':"homesickness",
        'cacophony':"harsh noise",
        'carnivorous':"meat eating",
        'clandestine':"secret"
        }
        score=0
        for i in range(0,len(mydict)):
            word=random.choice(list(mydict.keys()))
            myans = input(word+' ').lower()
            if mydict[word] == myans:
                print("Right Answer !!!")
                score=score+1
            else:
                print("Wrong Answer !!! Try Next One.")
            mydict.pop(word)
        print("You scored : ",score)
print('----------WORD GAME----------')
player_input()
