from django.db import models
from django.contrib.auth.models import  User


class movie(models.Model):
    Title       =models.CharField(max_length=255,help_text="A movie title",unique=True)
    Year        =models.IntegerField(help_text="year of movie",default=1)
    Rated       =models.CharField(max_length=255,help_text="movies rating",default='N.A')
    Released    =models.CharField(max_length=255,help_text="movie released time",default='N.A')
    Runtime     =models.CharField(max_length=255,help_text="total runtime",default='N.A')
    Genre       =models.CharField(max_length=255,help_text="genres",default='N.A')
    Director    =models.CharField(max_length=255,help_text="directors",blank=True,null=True)
    Writer      =models.CharField(max_length=255,help_text="writters",default='N.A')
    Actors      =models.CharField(max_length=255,help_text="Actors",default='N.A')
    Plot        =models.CharField(max_length=255,help_text="plot",default='N.A')
    Language    =models.CharField(max_length=255,help_text="language",blank=True,null=True)
    Country     =models.CharField(max_length=255,help_text="movie country",default='N.A')
    Awards      =models.CharField(max_length=255, blank=True,null=True,help_text="movie awards")
    Poster      =models.URLField(max_length=300,help_text="movies poster image url",default='N.A')
    Ratings     =models.CharField(max_length=255,help_text="A movie title",default='N.A')
    Metascore   =models.CharField(max_length=255,help_text="Meta score",default="N.A")
    imdbRating  =models.FloatField(help_text="imbd rating",default='N.A')
    imdbVotes   =models.CharField(max_length=20,help_text="movies imbd votes",default='N.A')
    imdbID      =models.CharField(max_length=10,help_text="movies imbs id",default='N.A')
    Type        =models.CharField(max_length=20,help_text="movie type",default='N.A')
    DVD         =models.CharField(max_length=20,blank=True,null=True, help_text="Dvd release date")
    BoxOffice   =models.CharField(max_length=255,help_text="A box office profit",default='N.A')
    Production  =models.CharField(max_length=255,help_text="some production data",default='N.A')
    Website     =models.URLField(max_length=255,help_text="movies website url",default='N.A')
    Response    =models.BooleanField(help_text="Response",default='N.A')
    
    def _str_(self):
        return self.Title

class review(models.Model):
    movie_id=models.ForeignKey(movie,on_delete=models.CASCADE)
    review=models.CharField(max_length=230)
    user_name = models.ForeignKey( User,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.movie_id   
    