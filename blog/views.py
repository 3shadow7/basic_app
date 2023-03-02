from django.shortcuts import render, get_object_or_404 
import json
from django.http import HttpResponse ,JsonResponse
from .models import Todo , checker
from django.views.generic import View 


def error_404 (request,exception):
    if request.method == 'POST':
        box = request.POST.get('box') == "false"
        theme = not request.session['theme']
        request.session['theme'] = theme
        return render(request, 'blog/404.html' , {'title': 'page not found' ,"theme" : theme},status=404)
        
    try:
        if request.session['theme'] == True or request.session['theme'] == False :
            theme = request.session['theme']
            return render(request, 'blog/404.html' , {'title': 'page not found' ,"theme" : theme},status=404)

    except KeyError:
        request.session['theme'] = True
        theme = request.session['theme']
        return render(request, 'blog/404.html' , {'title': 'page not found' ,"theme" : theme},status=404)

    
def is_it_post(request,name_of_file,context_title):
    
    if request.method == 'POST':
        box = request.POST.get('box') == "false"
        theme = not request.session['theme']
        request.session['theme'] = theme
        return render(request, name_of_file , {'title': context_title ,"theme" : theme})
        
    try:
        if request.session['theme'] == True or request.session['theme'] == False :
            theme = request.session['theme']
            return render(request, name_of_file , {'title': context_title ,"theme" : theme})

    except KeyError:
        request.session['theme'] = True
        theme = request.session['theme']
        return render(request, name_of_file , {'title': context_title ,"theme" : theme})


# -------------------------------------------------------------------- #


def home(request):
    """
    request : brawser checker the page if he 200
    then go to templates  <NameOfFolder>/<NameOfFile>
    then the title of page

    """
    context_title = 'Home'
    name_of_file = 'blog/home.html'
    return is_it_post(request,name_of_file,context_title)
    
        
def skills_1 (request):
    context_title = 'skills -> specialty'
    name_of_file = 'blog/skills-1.html'
    return is_it_post(request,name_of_file,context_title)


def skills_2 (request):
    context_title = 'skills -> services'
    name_of_file = 'blog/skills-2.html'
    return is_it_post(request,name_of_file,context_title)


def skills_3 (request):
    context_title = 'skills -> talents'
    name_of_file = 'blog/skills-3.html'
    return is_it_post(request,name_of_file,context_title)




