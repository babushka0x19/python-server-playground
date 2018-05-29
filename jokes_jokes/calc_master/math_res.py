from django.http import HttpResponse



def add(req, num1, num2):
    i = 1
    return HttpResponse(num1 + num2)