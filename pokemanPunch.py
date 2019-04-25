import requests
from bs4 import BeautifulSoup
import json
import os

class PokemonRap (object) :
        def __init__(self):
                self.url = 'https://genius.com/4489901' 
                 

        def getData(self):
                html = requests.get(self.url).text
                self.soup = BeautifulSoup(html, 'lxml')

        def parseList(self):

                punch = self.soup.find('div',{'class': 'rich_text_formatting'})
                print(punch.text)
                
                punchList = []
                for punchLineEl in punch:        
                        punchLine = punchLineEl.find_all('blockquote') 
                        descPunch = punchLineEl.find_all('p')  
                        detail = {
                                'punchLine': punchLine.text,
                                'description':descPunch.text,
                        } 
                     
                        punchList.append(detail)  

                return punchList

if __name__ == '__main__':
        ln = PokemonRap()

        ln.getData()
        parsedJson = json.dumps(ln.parseList())
        

        f = open("pokemonJson.json", "w")
        f.write(parsedJson)
        f.close()