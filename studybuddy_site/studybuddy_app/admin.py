from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Course
from .models import Meetup


# admin.site.register(Meetup)

class MeetupAdmin(admin.ModelAdmin):
    # fields = ["location", "title", "start_time", "end_time"]
    
    fieldsets = [
        ("What?", {"fields": ["title"]}),
        ("When?", {"fields": ["start_time", "duration"]}),
        ("Where?", {"fields": ["location"]}),
        ("Who?", {"fields": ["participants"]}),
    ]
    list_display = ["title", "start_time"]

class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

admin.site.register(Course, CourseAdmin)
admin.site.register(Meetup, MeetupAdmin)
