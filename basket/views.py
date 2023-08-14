from django.shortcuts import render

# Create your views here.
def view_basket(request):
    """Set up a view to display our shaopping basket"""
    return render(request, 'basket/basket.html')
