from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Course

class CourseListView(LoginRequiredMixin, generic.ListView):
    model = Course