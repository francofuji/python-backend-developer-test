from django.contrib import admin

from top_songs.models import Track, Artist, Genre


admin.site.register(Track)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Artist)
admin.site.register(Genre)
