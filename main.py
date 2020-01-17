import game

if __name__ == "__main__":
    start = "Pet door"
    end = "Cat"
    g = game.Game(start, end)
    g.randomPlayer()
    print(g.visited)
    print(g.score)
