from django.contrib import admin
from .models import *

# Registering models to admin panel
admin.site.register(Post)
# to be removed since it dosen't make sense to add commnent from admin 
admin.site.register(Comment)
admin.site.register(Tag)