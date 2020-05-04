from django.db import models
from datetime import date

class Person(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=75)



class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=75)
    instrument = models.CharField(max_length=100)


    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date=models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return "The album name is: %s made by %s" % (self.name, self.artist)


class Place(models.Model):
    name=models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


    def __str__(self):
        return "%s the restaurant" % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str(self):
        return "%s the waiter as %s" % (self.name, self.restaurant)


class Language(models.Model):
    name=models.CharField(max_length=50)

class Framework(models.Model):
    name=models.CharField(max_length=50)
    language=models.ForeignKey(Language,on_delete=models.CASCADE)


class Movie(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Character(models.Model):
    movie=models.ManyToManyField(
    Movie)
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name
'''
class Tag(models.Model):
    name = models.CharField(max_length=31, unique =True)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text="A label for URL config",
    )

    def __str__(self):
        return self.name

class Startup(models.Model):
    name = models.CharField(max_length=40)
    slug=models.SlugField(max_length=40,
    unique=True,
    help_text="A label for URL config",
    )
    description=models.TextField()
    founded_date=models.DateField("date founded")
    contact = models.EmailField()

    website = models.URLField(
        max_length=255
    )
    tags=models.ManyToManyField(Tag)


    def __str__(self):
        return self.name


class Newslink(models.Model):
    title = models.CharField(max_length=63)
    slug=models.SlugField(max_length=63)
    pub_date=models.DateField("Date Published")
    link = models.URLField(
        max_length=255
    )
    startup=models.ForeignKey(Startup,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.start}: {self.title}"
'''