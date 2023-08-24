from django.shortcuts import render

# Create your viwes here
# MVT


def index(request):
    return render(request, 'index.html')