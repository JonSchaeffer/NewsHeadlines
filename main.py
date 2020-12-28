import requests
import json

#Read config.json and apply the user config to our variables.
with open ('config.json') as c:
    config = json.load(c)

#Get together the apikey and how many sections the user wants to see and the quantity
#If there are multiple sections, it will be read as a list and we must extend the list. Otherwise, for one
#section, we must append the list. 
apiKey = config["api_Key"]
section = []
if type(config["section"]) is list:
    section.extend(config["section"])
else: 
    section.append(config["section"])

if config["Number_of_Headlines"] == "all":
    numOfHeadlines = "all"
else: 
    numOfHeadlines = int(config["Number_of_Headlines"])


def getNews(apiKey, section, numOfHeadlines):
    for x in range (len(section)):
        #Get the top stories and place the titles and abstracts in their respective lists.
        news = requests.get(("https://api.nytimes.com/svc/topstories/v2/{}.json?api-key={}").format(section[x], apiKey)).json()
        titles = []
        abstracts = []

        #Add all of the headlines and abstracts to their respective lists
        for headlines in news['results']:
            titles.append((headlines['title']))
            abstracts.append((headlines['abstract']))

        #Lets deal with the headlines now
        if numOfHeadlines == "all":
            numOfHeadlines = len(titles)
        elif numOfHeadlines > len(titles):
            numOfHeadlines = len(titles)
        else:
            break

        #Based off of the number of headlines, print out the quantity that the user requested.
        for y in range (numOfHeadlines):
            print(section[x].upper() + ": " + titles[y])
            print(abstracts[y])

getNews(apiKey, section, numOfHeadlines)