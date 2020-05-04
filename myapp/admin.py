from django.contrib import admin
from .models import Musician, Person,Album,Waiter,Place
from .models import Restaurant
from .models import Language, Framework, Movie, Character
#from .models import Tag, Startup,Newslink

admin.site.register(Musician)
admin.site.register(Person)
admin.site.register(Album)
admin.site.register(Waiter)
admin.site.register(Restaurant)
admin.site.register(Place)
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Movie)
admin.site.register(Character)
#admin.site.register(Tag)
#admin.site.register(Startup)
#admin.site.register(Newslink)

