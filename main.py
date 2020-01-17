import game

if __name__ == "__main__":
    g = game.Game("Body Mass Index", "Russell's teapot")
    print("Game validity :", g.isValid())
    g.set_max_iter(100)
    #g.randomPlayer()
    g.nlpMeanPlayer()
    print("path :", g.visited)
    print("score : ", g.score)
