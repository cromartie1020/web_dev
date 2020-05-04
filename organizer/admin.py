from django.contrib import admin
from .models import Tag, Startup, Newslink

#admin.site.register(Tag)

#admin.site.register(Startup)
admin.site.register(Newslink)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=('name','slug')


@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    list_display=('name','slug')
    prepoppulated_fields={'slug':("name")} 
