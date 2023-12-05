from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def to_index(request):
    return HttpResponseRedirect(reverse_lazy("users-app:index-view"))