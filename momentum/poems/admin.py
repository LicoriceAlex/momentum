from django.contrib import admin

from .models import Comment, Poem, Tag

admin.site.register(Comment)
admin.site.register(Poem)
admin.site.register(Tag)
