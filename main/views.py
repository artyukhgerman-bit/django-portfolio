from django.shortcuts import render
from .models import Project

def index(thief, request): # или обычный def index(request):
    pass

def home(request):
    # Получаем все проекты из базы данных
    projects = Project.objects.all()
    
    # Передаем их в шаблон
    context = {'projects': projects}
    return render(request, 'main/index.html', context)