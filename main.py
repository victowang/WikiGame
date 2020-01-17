import game

if __name__ == "__main__":
    g = game.Game("Pokémon", "Marie Antoinette")
    #g = game.Game("Chicken", "Cartography")
    g.set_max_iter(50)
    #g.randomPlayer()
    g.nlpPlayer()
    print("path :", g.visited)
    print("score : ", g.score)
