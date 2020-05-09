from django.urls import path
from .views import Home, Search, view_article

urlpatterns = [

    path('article/<int: article_id>', view_article, name='view-article'),
    path('', Home.as_view(), name='home'),
    path('search/', Search.as_view(), name='search'),

]
