import json
from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def more_todo(request):
	if request.is_ajax():
		todo_items = ['Mow lown', 'Buy Groceries']
		data = json.dumps(todo_items)
		return HttpResponse(data, content_type='application/json')
	else:
		raise Http404

def add_todo(request):
    if request.is_ajax() and request.POST:
        data = {'message':'%s is added' % request.POST.get('item')}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
    	raise Http404
    
