from django.conf.urls import include
from django.urls import path

from jokes_jokes.html_contents import pages
from . import views

urlpatterns = [
    path('admin/', views.index, name='index'),
    path('say_hi/', views.say_hi, name='say_hi'),
    path('error/', views.error, name='error'),

    path('html/', include('jokes_jokes.html_contents.urls')),
    path('calc/', include('jokes_jokes.calc_master.urls')),

    path('i_want_nice_page/', views.nice_page, name='nice_page'),
]