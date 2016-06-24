from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext, loader
from news.models import *
from datetime import date, timedelta
import datetime

# Create your views here.


def index(request):
	section = Section.objects.all()
	slide = Slide.objects.all()
	card = Card.objects.order_by('-Section_id')
	breaking = Breaking.objects.order_by('-id')
	news_slider=[]
	for i in breaking:
		news_slider.append(i.text+"  "*15)
	print news_slider


	context = {'card':card, 'slide':slide, 'breaking':" ***** ".join(news_slider), 'section':section, "slide_len": []}
	context['slide_len'] = range(1, len(slide))
	print context
	return render(request, 'index.html', context)