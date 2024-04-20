from django.shortcuts import render
from .models import *
from myproject.settings import BASE_DIR
from django.http import HttpResponseRedirect 

# Create your views here.
def index(request):
    # Recipe.objects.all().delete()
    recipes=Recipe.objects.all()
    return render(request,'index.html',{'recipes':recipes,'BASE_DIR':BASE_DIR})

def enter_recipe(request):
    if request.method == 'POST':
        recipe = Recipe()
        recipe.dish = request.POST.get("dish", False)
        recipe.time = request.POST.get("time", False)
        recipe.ingredients = request.POST.get("ingredients", False)
        recipe.save()

    
    return render(request, 'enter_recipe.html')

def comment(request):
        return render(request, 'comment.html')

def save_comment(request,id):
            recipe = Recipe.objects.get(id=id)
            recipe.comment = request.POST.get("comment")
            recipe.save()
            return HttpResponseRedirect('')
