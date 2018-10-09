#from django.http import HttpResponse
from .models import Board
from django.shortcuts import render

# Create your views here.

def home(request):
    #return HttpResponse('Hello World!')
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards':boards})

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board':board})