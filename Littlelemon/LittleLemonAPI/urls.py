from django.urls import path
from . import views

urlpatterns = [
    path('category', views.CategoriesView.as_view()),
    path('menu-items', views.MenuItemView.as_view()),
]