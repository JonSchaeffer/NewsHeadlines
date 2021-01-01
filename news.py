from samplebase import SampleBase
from rgbmatrix import graphics, RGBMatrixOptions
import time

import requests
import json

#Read config.json and apply the user config to our variables.
with open ('config.json') as c:
    config = json.load(c)

#Get together the apikey and how many sections the user wants to see and the quantity
#If there are multiple sections, it will be read as a list and we must extend the list. Otherwise, for one
#section, we must append the list. 

class News:
    def __init__(self):
        self.apiKey = config["api_Key"]
        self.section = []
        if type(config["section"]) is list:
            self.section.extend(config["section"])
        else: 
            self.section.append(config["section"])

        if config["Number_of_Headlines"] == "all":
            self.numOfHeadlines = "all"
        else: 
            self.numOfHeadlines = int(config["Number_of_Headlines"])


    def getNews(self):
        for x in range (len(self.section)):
            #Get the top stories and place the titles and abstracts in their respective lists.
            news = requests.get(("https://api.nytimes.com/svc/topstories/v2/{}.json?api-key={}").format(self.section[x], self.apiKey)).json()
            titles = []
            abstracts = []
            headline = ""

            #Add all of the headlines and abstracts to their respective lists
            for headlines in news['results']:
                titles.append((headlines['title']))
                abstracts.append((headlines['abstract']))

            #Lets deal with the headlines now
            if self.numOfHeadlines == "all":
                self.numOfHeadlines = len(titles)
            elif self.numOfHeadlines > len(titles):
                self.numOfHeadlines = len(titles)
            else:
                break

        
        #Based off of the number of headlines, print out the quantity that the user requested.
        
        for y in range (self.numOfHeadlines):
            if y + 1 < self.numOfHeadlines:
                headline += titles[y] + ",    "
            else:
                headline += titles[y]
        
        #print(headline)
        return headline

#news = News()
#result = news.getNews()
#news.getNews()
