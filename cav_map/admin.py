from django.contrib import admin
from .models import Class, ClassSchedule, ForumPost

admin.site.register(Class)
#admin.site.register(useradmin)

admin.site.register(ForumPost)
