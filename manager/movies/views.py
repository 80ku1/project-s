from django.shortcuts import render
from . models import MovieDB
# Create your views here.
from .forms import MovieClass

def create(request):
    movie_details= MovieDB.objects.all()
    create_form = MovieClass()
    if request.POST:
        create_form=MovieClass(request.POST)
        if create_form.is_valid():
            create_form.save()
            return render(request,'list.html', { "movies":movie_details})
    else: 
        create_form=MovieClass()

    return render(request, 'create.html',{'form':create_form})
                  
def list(request):

    movie_details= MovieDB.objects.all()
    return render(request,'list.html', { "movies":movie_details}) 

def edit(request,pk):
    movie_details= MovieDB.objects.all()
    inst = MovieDB.objects.get(pk=pk)
    if request.POST:
        edit_form=MovieClass(request.POST, instance=inst)
        if edit_form.is_valid():
            edit_form.save()
            return render(request,'list.html', { 'movies':movie_details})
        
    edit_form=MovieClass(instance=inst)
    return render(request, 'create.html',{'form':edit_form})

def delete(request,pk):
    
    inst = MovieDB.objects.get(pk=pk)
    inst.delete()
    movie_details= MovieDB.objects.all()
    return render(request,'list.html', { 'movies':movie_details})

def home(request):

    return render(request,'home.html')