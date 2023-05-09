from django.shortcuts import render

# Create your views here.
def personnel(request):
    """set up new page for displaying all content"""
    context = {}
    return render(request, 'personnel/personnel.html', context)
