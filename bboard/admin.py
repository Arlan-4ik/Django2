from django.contrib import admin

from bboard.models import Bboard, Rubric


class BboardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Bboard, BboardAdmin)
admin.site.register(Rubric)
