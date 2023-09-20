from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.hello_page, name='home'),
    path('words_list/', views.page_words_table, name='words_list'),
    path('add_word/', views.postuser, name='add_word'),
]