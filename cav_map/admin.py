from django.contrib import admin
from .models import Class, ClassSchedule

admin.site.register(Class)
#admin.site.register(useradmin)

from .models import ForumPost

admin.site.register(ForumPost)
