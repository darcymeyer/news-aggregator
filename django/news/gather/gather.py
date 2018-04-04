# does the gathering

import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime, timedelta

# from sources import sources # imports dict of rss feeds
from source_scrapers import * # imports functions to scrape different feeds
import organize

from tqdm import tqdm

dummydata = {
	'stories': [
		{
			'title': "Vulnerability discovered",
			'brief': "there was a Vulnerability discovered in such and such software",
			'sources': [
				{
					'source': "Wired",
					'articletitle': "Researchers find Vulnerability",
					'articlelink': "https://wired.com",
					'summary': "some few lines of summary of the article"
				},
				{
					'source': "BBC",
					'articletitle': "Oxford research group discovers Vulnerability",
					'articlelink': "https://bbc.co.uk",
					'summary': "some more lines of summary of this article"
				}
			]
		},
		{
			'title': "Election in Europe",
			'brief': "some country is having an election",
			'sources': [
				{
					'source': "BBC",
					'articletitle': "European country election this Tuesday",
					'articlelink': "https://bbc.co.uk",
					'summary': "some few lines of summary of the article"
				},
				{
					'source': "NYT",
					'articletitle': "Close race for European country election",
					'articlelink': "https://nyt.com",
					'summary': "some more lines of summary of this article"
				}
			]
		}

	]
}


current_sources = "the-new-york-times,bbc-news,wired,politico,cbs-news,cnn,the-guardian-uk"
srcs = current_sources.split(",")
api_key = "f3dc0127c680461698cba88df56f323b"
headers={"X-Api-Key":api_key}
data={
      "pageSize":30,
      "language":"en",
     }

def gather():
    allarticles = []
    for s in tqdm(srcs):
        data['sources'] = s
        r = requests.get("https://newsapi.org/v2/everything", headers=headers, params=data)
        for art in tqdm(r.json()['articles']):
            # just make a new dict
            getter = eval(s.title().replace("-","")+"_text_getter")
            art_text = getter(art['url'])
            if art_text:
                d = {
                    "title":art['title'],
                    "blurb":art['description'],
                    "source":art['source']['name'],
                    "pubdate":art['publishedAt'],
                    "link":art['url'],
                    "text":art_text
                }
                allarticles.append(d)
    organized = organize.organize(allarticles) # orig. organize.organize()
    with open('now.txt', 'w') as f:
        f.write(json.dumps(organized))


if __name__=="__main__":
	gather()


# TODO: (BETTER) FILTERING or else it's not gonna be useful
# ALSO checking for updates and notifying of new stories

# we're gonna need some Watson for extracting article topics and coagulating them... proper nouns and stuff




