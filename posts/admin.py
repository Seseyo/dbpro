# posts/admin.py

import imp
from django.contrib import admin

# Register your models here.

from .models import Post

admin.site.register(Post)
