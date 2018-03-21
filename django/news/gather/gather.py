# does the gathering

import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime, timedelta

from sources import sources # imports dict of rss feeds
from source_scrapers import * # imports functions to scrape different feeds
import organize

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


# def gather():
# 	'''Main function for gathering. Called periodically.'''
# 	all_things = {'stories':[]}
# 	for sourcename, url, handler in SOURCES:
# 		func = eval(handler) # This is just a personal app, so I don't think this is insecure
# 		results = func(url)
# 		all_things['stories'] += results
# 	# this is where we're going to do the processing n stuff
# 	global at
# 	at = all_things
# 	organized = dummydata # REMOVE FOR PRODUCTION
# 	# organized = organize(all_things)
# 	with open('now.txt', 'w') as f:
# 		f.write(json.dumps(organized))

def gather():
	everything = []
	for source in sources:
		sourcename = source.split(" ")[0]
		scraper = eval(sourcename+"_scraper")
		everything += scraper(sources[source]) # sources[source] is the url
	organized = organize.organize(everything)
	with open('now.txt', 'w') as f:
		f.write(json.dumps(organized))


if __name__=="__main__":
	# with open("sources.txt", 'r') as f:
	# 	lines = f.readlines()
	# 	global SOURCES
	# 	SOURCES = [s.split(" ") for s in lines]
	gather()


# TODO: FILTERING or else it's not gonna be useful
# ALSO checking for updates and notifying of new stories

# we're gonna need some Watson for extracting article topics and coagulating them... proper nouns and stuff




