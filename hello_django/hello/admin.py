from django.contrib import admin

# Register your models here.

from hello.models import *

admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Book)
admin.site.register(Publisher)