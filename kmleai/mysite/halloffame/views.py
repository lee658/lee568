from django.shortcuts import render

# Create your views here.

def halloffame(request):
    return render(request, 'halloffame/halloffame.html')
