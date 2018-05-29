from django.urls import path

from jokes_jokes.html_contents import pages

urlpatterns = [
    path('nice_html/', pages.nice_page, name='nice_page'),
]