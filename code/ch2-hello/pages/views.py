from django.shortcuts import HttpResponse

# Create your views here.
def home_page(request):
  return HttpResponse("Hello, World! This is the home page of our Django application.")