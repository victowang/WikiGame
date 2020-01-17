import parser
import random
import spacyTools
import warnings

class Game:
    start = "";
    end = "";
    current = "",
    visited = [];
    score = 0;
    max_iter = 100;

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
        self.visited.append(start)
        self.score = 0
        self.visited= [start]

    def isValid(self):
        wikiParser = parser.WikiParser()
        is_valid = True
        if not wikiParser.pageExists(self.start):
            print("tha page " + self.start + " doesn't exist")
            is_valid = False
        if not wikiParser.pageExists(self.end):
            print("tha page " + self.end + " doesn't exist")
            is_valid = False
        return is_valid

    def randomPlayer(self):
        self.__init__(self.start, self.end)
        print("start :" + self.start + ", goal :" + self.end)
        wikiParser = parser.WikiParser()
        while self.current != self.end and self.score < self.max_iter:
            page = wikiParser.getPage(self.current)
            next_words = wikiParser.getLinksFromPage(page)
            if self.end in next_words:
                self.current = self.end
                self.visited.append(self.current)
                self.score += 1
                print("I win")
                return
            else: #select random
                r = random.randint(0, len(next_words)-1)
                self.current = next_words[r]
            self.visited.append(self.current)
            self.score += 1

    def nlpPlayer(self):
        self.__init__(self.start, self.end)
        print("Start :" + self.start + ", Goal :" + self.end)
        wikiParser = parser.WikiParser()
        while self.current != self.end and self.score < self.max_iter:
            page = wikiParser.getPage(self.current)
            next_words = wikiParser.getLinksFromPage(page)
            max_similarity = 0
            max_word = ""

            # filter to prevent looping
            for word in next_words:
                if word in self.visited:
                    next_words.remove(word)
                if next_words == []:
                    print("I am stuck")
                    return

            for word in next_words:
                if self.end in next_words:
                    self.current = self.end
                    self.visited.append(self.current)
                    self.score += 1
                    print("Found page :", self.end)
                    return
                else: #select most similar
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore")
                        similarity = spacyTools.getSimilarity(word, self.end)
                    if similarity > max_similarity:
                        max_similarity = similarity
                        max_word = word
            self.visited.append(max_word)
            self.current=max_word
            self.score += 1
        print("I loose")

    # setters and getters

    def set_start(self, name):
        self.start = name

    def set_end(self, name):
        self.end = name

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def set_max_iter(self, n):
        self.max_iter = n

    def get_max_iter(self):
        return self.max_iter

