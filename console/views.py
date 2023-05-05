from django.shortcuts import render

# Create your views here.
def console(request):
    """set up new page for displaying all content"""
    context = {}
    return render(request, 'console/console.html', context)