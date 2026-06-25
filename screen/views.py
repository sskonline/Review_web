from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.core.paginator import Paginator


#static demo data
#movies=[
#        {'year':'2026','title':'Obsession','genre':'Horror','id':'Obsession'},
#        {'year':'2026','title':'Backrooms','genre':'Horror','id':'Backrooms'},
#        {'year':'2026','title':'The Odyssey','genre':'Periodic','id':'The Odyssey'},
#       {'year':'2026','title':'Spiderman-Brand new day','genre':'Action','id':'Spiderman-Brand new day'},
    
def index(request):
    all_movies= Movie.objects.all()
    #paginate
    paginator = Paginator(all_movies,3)
    pagenum = request.GET.get('page')
    pageobj = paginator.get_page(pagenum)
    screentitle='Rbox'
    return render(request,'index.html',{'screentitle':screentitle,'pageobj':pageobj})
def detail(request, slug):
    #for static data
    #post= next((i for i in movies if i['id']==str(id)), None)
    #from model
    movies=Movie.objects.get(slug = slug)
    rel_movies= Movie.objects.filter(year= movies.year).exclude(slug=slug)
    return render(request,'detail.html',{'movies':movies,'rel_movies':rel_movies})
