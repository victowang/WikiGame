import game

def test():
    g = game.Game("Flying Spaghetti Monster", "Bolzano–Weierstrass theorem")
    print("Game validity :", g.isValid())
    g.nlpMeanPlayer()
    print("path :", g.visited)
    print("score : ", g.score)

if __name__ == "__main__":
    test()
    while True:
        x = input('New game ? (Y/N) ')
        if(x.upper() != 'Y' ):
            print("exit")
            break
        while (True):
            start = input('Starting page : ')
            end = input('Target page : ')
            g = game.Game(start.replace('_', ' '), end.replace('_', ' '))
            break
            if (g.isValid()):
                print("Valid game")
                break
            else:
                print("Invalid inputs, please enter existing pages")
        max = input('Maximum number of loaded pages : ')
        if(not max):
            print("default max = 100\n")
            max = 100
        g.set_max_iter(int(max))
        g.nlpMeanPlayer()
        print("path :", g.visited)
        print("score : ", g.score)