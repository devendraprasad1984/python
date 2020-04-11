from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import movie


def index(request):
    sRes="<h1>Hello DP, this is test App Index Page</h1>"
    sRes+="Movies are as follows<br/>"
    all_movies=movie.objects.all()
    for myMovie in all_movies:
        sUri='/testApp/'+str(myMovie.id)+'/'
        sRes+='<a href="'+sUri+'">'+str(myMovie)+'</a><br/>'

    sRes+="<br/>loading via the django template<br/>"
    myTemplate=loader.get_template('index1.html')
    context={
        'jsonData': all_movies
    }
    # return HttpResponse(sRes) #plain response of html contents back to html
    # return HttpResponse(myTemplate.render(context,request)) //via loader template
    return render(request,'index1.html',context)

def getDetailsOfMovie(request,movie_id):
    sRes="<h1>welcome, id: "+str(movie_id)+"</h1>"
    # try:
    #     myMovieObject=movie.objects.get(pk=movie_id)
    # except movie.DoesNotExist:
    #     # raise Http404("Object not found, invalid id")
    #     return render(request, 'myMovieNotFound.html', {'errMsg': 'page not found'})
    #
    myMovieObject=get_object_or_404(movie,pk=movie_id)
    return render(request,'myMovieObject.html',{'myMovieObject':myMovieObject, 'movieName':''})
    # return HttpResponse(sRes)

def favourite(request):
    movie_id=request.POST['movie'];
    # movie[movie_id].is_favourite=True;
    myMovieObject = get_object_or_404(movie, pk=movie_id)
    # return render(request,'myMovieObject.html',{'myMovieObject':myMovieObject})
    return HttpResponse('this is movie object '+str(myMovieObject))