from django.urls import path

from jokes_jokes.calc_master import math_res

urlpatterns = [
    path('add/<int:num1>/<int:num2>', math_res.add, name='nice_page'),
]