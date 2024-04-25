from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories, name='categories'),
    path('<int:news_id>', views.single, name='single')
]
