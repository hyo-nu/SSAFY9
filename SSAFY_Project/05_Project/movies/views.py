from django.shortcuts import render,redirect
from .forms import MovieForm
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'movies/index.html',context)

def create(request):
    if request.method=='POST':#전송이POST방식이면,
        form = MovieForm(request .POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail',movie.pk) 
    else:#전송이GET방식이면([새글작성]버튼누름),
        form = MovieForm()#그냥빈품보여줌

    #유효성검증통과못할시
    context = {
    'form':form#통과못한것다시돌려줌
    }
    return render(request, 'movies/create.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie':movie,
    }
    return render(request, 'movies/detail.html', context)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance = movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail',movie.pk)
    else:
        form = MovieForm(instance = movie)
    context={
        'form':form,
        'movie':movie,
    }
    return render(request, 'movies/update.html',context)

def delete(request,pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')