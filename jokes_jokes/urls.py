from django.urls import path

from . import views

urlpatterns = [
    path('admin/', views.index, name='index'),
    path('say_hi/', views.say_hi, name='say_hi'),
    path('error/', views.error, name='error'),
    path('i_want_nice_page/', views.nice_page, name='nice_page'),
]