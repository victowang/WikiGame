# This project aims at making a bot play the Wikipedia game

A player is given a starting wikipedia page and a target wikipedia page, the player has to get to the target page only by following links in the current page  

## Strategies :
* Random : if the end page is not found, chooses a random link  
        _Unlikely to succeed_  
        
* Using nlp : chooses the word closest to the target in the page
    * Max : compute similarity between two strings as the max similarity between verds from the two strings  
        _Could get stuck in pages about Turkey (country) when trying to get to Bacon_
        
    * Mean : compute similarity between two strings as the average similarity between verds from the two strings  
        _Better when facing the previous issue_

## Tools:
* BeautifulSoup to parse html
* Spacy to find similarities

## Choose a spacy ressource to download:
* lighter :  
python -m spacy download en_core_web_sm  
* medium :  
python -m spacy download en_core_web_md  
* heavier :  
python -m spacy download en_core_web_lg  

In spacyTools.py choose between 'sm', 'md' and 'lg' by editing the following line :  
nlp = spacy.load('en_core_web_lg')