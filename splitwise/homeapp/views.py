from django.shortcuts import render, HttpResponse

# Create your views here.
def my_home_page(request):
    return render(request, 'home.html', {})
