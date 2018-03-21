import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# WIRED
def WIRED_scraper(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html5lib")
	results = []
	stories = soup.find_all("item")
	for story in stories:
		articletitle = story.find("title").string
		blurb = story.find("description").string
		articlelink = re.findall('(?<=<link/>).*?(?=<guid)', str(story))[0]
		pubst = story.find("pubdate").string
		pubdate = datetime.strptime(pubst[:-6], "%a, %d %b %Y %H:%M:%S") 
			# "Thu, 15 Mar 2018 21:09:57 +0000"
		tz = pubst[-5:]
		td = timedelta(hours=int(tz[1:3]), minutes=int(tz[3:5]))
		if tz[0] == "+":
			pubdate -= td
		elif tz[0] == "-":
			pubdate += td
		# mediaurl = story.find("media:thumbnail").get("url")
		text = WIRED_text_getter(articlelink)
		processed = {
			'source':'WIRED',
			'title':articletitle,
			'link':articlelink,
			'blurb':blurb,
			'pubdate':pubdate, # TODO: display this
			'text':text
		}
		results.append(processed)
	return results

# NYT
def NYT_scraper(url):
	def NYT_text_getter(url): # this works don't change it
		whole = ''
		soup = BeautifulSoup(requests.get(url).text)
		a = soup.find_all(attrs={'class':'story-body-text story-content'})
		result = '\n'.join([e.text for e in a])
		return result
	results = []
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html5lib")
	stories = soup.find_all("item")
	for story in stories:
		articlelink = story.find("guid").string
		if "/opinion/" in articlelink:
			continue
		articletitle = story.find("title").string
		blurb = story.find("description").string
		pubst = story.find("pubdate").string
		pubdate = datetime.strptime(pubst[:-4], "%a, %d %b %Y %H:%M:%S") 
			# 'Sun, 18 Mar 2018 17:29:47 GMT'
		text = NYT_text_getter(articlelink)
		processed = {
			'source':'NYT',
			'title':articletitle,
			'link':articlelink,
			'blurb':blurb,
			'pubdate':pubdate,
			'text':text
		}
		results.append(processed)
	return results
