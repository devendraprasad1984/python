from django.db import models

# run following commands in order to apply changes to sqlLiteDB
# python manage.py makemigrations testApp
# python manage.py migrate
# C:\Python34\python.exe F:/python/djangoTest/dp1/manage.py runserver 0.0.0.0:6200
# https://code.google.com/archive/p/modwsgi/downloads
# http://groups.google.com/group/modwsgi
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#mod_wsgi
# https://pypi.org/project/mod_wsgi/

class movie(models.Model):
    actor = models.CharField(max_length=30)
    actor_movie = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    movie_logo= models.CharField(max_length=200)
    is_favourite=models.BooleanField(default=False)
    def __str__(self):
        return self.actor+'-->'+self.actor_movie



class songs(models.Model):
    movieName=models.ForeignKey(movie,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=50)
    song_name=models.CharField(max_length=200)
    def __str__(self):
        return self.song_name+"-->"+self.movieName


