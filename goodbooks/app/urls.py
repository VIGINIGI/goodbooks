from django.urls import include,path
from .views import sample_view

urlpatterns = [
    path('sample/',sample_view)
]