import parser
import random
import spacy
spacy.load('en_core_web_lg')

class Game:
    start = "";
    end = "";
    current = "",
    visited = [];
    score = 0;
    max_iter = 100

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
        self.visited.append(start)
        self.score = 0
        self.visited= [start]

    def setStart(self, name):
        self.start = name

    def setEnd(self, name):
        self.end = name

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def randomPlayer(self):
        self.__init__(self.start, self.end)
        wikiParser = parser.WikiParser()
        while self.current != self.end and self.score < self.max_iter:
            page = wikiParser.getPage(self.current)
            next_words = wikiParser.getLinksFromPage(page)
            if self.end in next_words:
                self.current = self.end
                print("I win")
            else: #select random
                r = random.randint(0, len(next_words)-1)
                self.current = next_words[r]
            self.visited.append(self.current)
            self.score += 1


