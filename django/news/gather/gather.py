# does the gathering

# let's try to stick to RSS feeds

import requests
from bs4 import BeautifulSoup

def gather():
	all_things = {}
	for url, handler, sourcename in RSS_SOURCES:
		result = handler(url)
		all_things[sourcename] = result
	# dummyobject = {"title1":"useful info", "title2":"more useful info"}
	return all_things#dummyobject
	# pass

def wired_handler(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text)
	result = {}
	stories = soup.find_all("item")
	for story in stories:
		title = story.find("title").string
		desc = story.find("description").string
		pubdate = story.find("pubdate").string
		mediaurl = story.find("media:thumbnail").get("url")
		result[title] = {"desc":desc, "pubdate":pubdate, "mediaurl":mediaurl}
	# print r.text
	global s 
	s= soup
	return result#r.text#None


def get_summary():
	pass

RSS_SOURCES = [("https://www.wired.com/feed/category/security/latest/rss", wired_handler, "WIRED Security"), 
				("https://www.wired.com/feed/category/business/latest/rss", wired_handler, "WIRED Business")]


if __name__=="__main__":
	gather()


# TODO: FILTERING or else it's not gonna be useful
# ALSO checking for updates and notifying of new stories

# going to need some major organizing...
# we're gonna need some Watson for extracting article topics and coagulating them... proper nouns and stuff




