# does the gathering

# let's try to stick to RSS feeds

import requests
from bs4 import BeautifulSoup
import json
import re


dummydata = {
	'stories': [
		{
			'title': "Vulnerability discovered",
			'brief': "there was a Vulnerability discovered in such and such software",
			'sources': [
				{
					'source': "Wired",
					'articlelink': "https://wired.com",
					'summary': "some few lines of summary of the article"
				},
				{
					'source': "BBC",
					'articlelink': "https://bbc.com",
					'summary': "some more lines of summary of this article"
				}
			]
		}

	]
}


def gather():
	'''Main function for gathering. Called periodically.'''
	all_things = {}
	for sourcename, url, handler in SOURCES:
		func = eval(handler) # This is just a personal app, so I don't think this is insecure
		result = func(url)
		all_things[sourcename] = result
	# dummyobject = {"title1":"useful info", "title2":"more useful info"}
	# return all_things#dummyobject
	# pass
	# this is where we're going to do the processing n stuff
	with open('now.txt', 'w') as f:
		f.write(json.dumps(all_things))

def wired_handler(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html5lib")
	result = {}
	stories = soup.find_all("item")
	for story in stories:
		title = story.find("title").string
		desc = story.find("description").string
		link = re.findall('(?<=<link/>).*?(?=<guid)', str(story))[0]
		pubdate = story.find("pubdate").string
		mediaurl = story.find("media:thumbnail").get("url")
		summary = summarize("the text")
		result[title] = {"desc":desc, "pubdate":pubdate, "mediaurl":mediaurl}
	# print r.text
	global s 
	s= soup
	return result#r.text#None


def summarize(text):
	'''takes a block of text and returns a 3-sentence summary'''
	pass# just use a small thing from github. the https://github.com/lekhakpadmanabh/Summarizer/tree/master/smrzr thing.



if __name__=="__main__":
	with open("gather/sources.txt", 'r') as f:
		lines = f.readlines()
		global SOURCES
		SOURCES = [s.split(" ") for s in lines]
	gather()


# TODO: FILTERING or else it's not gonna be useful
# ALSO checking for updates and notifying of new stories

# going to need some major organizing...
# we're gonna need some Watson for extracting article topics and coagulating them... proper nouns and stuff




