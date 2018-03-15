from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from gather import gather
import json

def main(request):
	with open("gather/now.txt", 'r') as f:
		text = f.readlines()[0]
		stories = json.loads(text)
	# gather() NO! don't go through this long loading process. read from a file

	return JsonResponse(stories) # use safe=False for non-dict stuff [will be dict]