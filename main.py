import game

def test():
    g = game.Game("Basil", "Antarctica")
    #print("Game validity :", g.isValid())
    g.set_max_iter(100)
    g.nlpMeanPlayer()
    print("path :", g.visited)
    print("score : ", g.score)

if __name__ == "__main__":
    #test()
    while True:
        x = input('New game ? (Y/N) ')
        if(x.upper() != 'Y' ):
            print("exit")
            break
        start = input('Starting page : ')
        end = input('Target page : ')
        max = input('Maximum number of loaded pages : ')
        g = game.Game(start, end)
        if(not max):
            print("default max = 100\n")
            max = 100
        g.set_max_iter(max)
        g.nlpMeanPlayer()
        print("path :", g.visited)
        print("score : ", g.score)