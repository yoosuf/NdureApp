from django.shortcuts import render

# Homepage view
def homepage_view(request):
    return render(request, 'homepage.html')
    
