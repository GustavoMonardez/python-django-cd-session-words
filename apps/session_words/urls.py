from django.conf.urls import url 
from . import views

urlpatterns = [
    url("^$", views.index),
    url("^session_words$", views.index),
    url("^session_words/process$", views.process),
    url("^session_words/clear$", views.clear)
]