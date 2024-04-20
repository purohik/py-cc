from django.contrib import admin

# Register your models here.
from .models import Frog, Task

admin.site.register(Frog)
admin.site.register(Task)