#from django.http import HttpResponse
from .models import Board
from django.shortcuts import render

# Create your views here.

def home(request):
    #return HttpResponse('Hello World!')
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards':boards})