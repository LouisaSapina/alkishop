from django.shortcuts import render

def index(request):
	return render(request, 'feed/index.html', context=context)
