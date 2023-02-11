from django.shortcuts import render

# Create your views here.
def translator_view(request):
    return render(request, 'translator_view.html')