from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from gather import gather

# Create your views here.

def main(request):
	stories = gather()
	return JsonResponse(stories) # use safe=False for non-dict stuff