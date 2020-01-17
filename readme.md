# This project aims at making a bot play the Wikipedia game

A player is given a starting wikipedia page and a target wikipedia page, the player has to get to the target page only by following links in the current page  

## Strategies :
* Random : if the end page is not found, chooses a random link (not good at all)
* Using nlp : chooses the word closest to the target in the page
    * Max : compute similarity between two strings as the max similarity between verds from the two strings  
        Could get stuck in pages about Turkey (country) when trying to get to Bacon
    * Mean : compute similarity between two strings as the average similarity between verds from the two strings  
        Better against the previous issue

## Tools:
* BeautifulSoup to parse html
* Spacy to find similarities