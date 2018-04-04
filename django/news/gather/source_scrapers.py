import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def TheNewYorkTimes_text_getter(url):
    try:
        soup = BeautifulSoup(requests.get(url).text, "html5lib")
        a = soup.find_all(attrs={'class':'story-body-text story-content'})
        result = '\n'.join([e.text for e in a])
        return result
    except:
        return None

def Wired_text_getter(url):
    try:
        headers = {'cookie':'CN_xid=befc046c-b271-40cd-b638-31380df25caa; ev_sid=5a78f68be4b06ff2602e83d7; ev_did=5aa8463fe4b00aaae40892f3; visitedCount_dft=7; cneplayermuted=1; cneplayercount=9; cneplayervolume=1; cnid_uuid=b523095f-8cb2-4895-b3ca-51017b00be57; amg_user=W1NiPT1BalwtfAtuGWpffSF/Y0MmaBB3BUwM; amg_user_partner=b3b7bc23-fb64-415f-8a58-e3ac1e027235; ev_ss=a7a54f27-5f6e-4363-9939-8b0e456aeac2; ev_auth=893e6109-aa4e-46d3-9a39-6b9a5390edf9; user_email=darcy2252755@gmail.com; _wired_logged_in=1; cneplayercaptions=showing'}
        global testsoup
        testsoup = BeautifulSoup(requests.get(url, headers=headers).text, "html5lib")
        ps = [c for c in testsoup.find("article").children][0].find_all("p", recursive=False)
        full = "\n".join([p.text for p in ps])
        return full
    except:
        return None

def BbcNews_text_getter(url):
    try:
        soup = BeautifulSoup(requests.get(url).text)
        a = soup.find(attrs={"class":"story-body__inner"})
        full = "\n".join([p.text for p in a.find_all("p", recursive=False)])
        return full
    except:
        return None

def Politico_text_getter(url):
    if "/playbook/" in url:
        return None
    try:
        soup = BeautifulSoup(requests.get(url).text)
        a = soup.find(attrs={"class":"story-text"})
        full = "\n".join([p.text for p in a.find_all("p", recursive=False)])
        return full
    except:
        return None

def TheGuardianUk_text_getter(url):
    try:
        soup = BeautifulSoup(requests.get(url).text)
        a = soup.find(attrs={"class":"content__article-body"})
        full = "\n".join([p.text for p in a.find_all("p", recursive=False)])
        return full
    except:
        return None

def Cnn_text_getter(url):
    try:
        soup = BeautifulSoup(requests.get(url).text)
        a = soup.find_all(attrs={"class":"zn-body__paragraph"})
        full = "\n".join([p.text for p in a])
        return full
    except:
        return None

def CbsNews_text_getter(url):
    try:
        soup = BeautifulSoup(requests.get(url).text)
        a = soup.find(attrs={"id":"article-entry"})
        full = "\n".join([p.text for p in a.find_all("p")])
        return full
    except:
        return None


