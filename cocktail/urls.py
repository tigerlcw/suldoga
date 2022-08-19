from django.urls import path
from . import views

app_name = 'cocktail'

urlpatterns = [
    path('', views.MainView, name='main'),
    path('info', views.InfoView, name='info'),
    path('cocktail', views.ListView, name='cocktail'),
    path('kocktail', views.KListView, name='kocktail'),
    path('combination1', views.Combination1View, name="combination1"),
    path('combination2', views.Combination2View, name="combination2"),
    path('combination3', views.Combination3View, name="combination3"),
    path('combinationFin', views.CombinationFinView, name="combinationFin"),
    path('test', views.TestView, name='test'),
    path('like/<int:cocktails_id>?next=<str:next_page>', views.LikeView, name="likes"),
    path('myprofile/<int:user_id>', views.myprofile, name='profile'),
]
