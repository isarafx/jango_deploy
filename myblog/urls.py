from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_text),
    path('post/<int:id>', views.show_single_post)
]