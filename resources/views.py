from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Q

from .models import Product, Category
from .forms import ProductForm, ApproveProductForm

# Create your views here.
def resources(request):
    """set up shop for our resources"""
    categories = Category.objects.all()
    products = Product.objects.filter(approved_item=1)

    sort = None
    direction = None
    category = None
    cat = None
    query = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(
                    lower_name=Lower('name')
                )
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)
            cat = Category.objects.filter(name=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    'Woops! You forgot to include a search term - Try again!'
                )
                return redirect(reverse('resources'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'categories': categories,
        'cat': cat,
        'current_sorting': current_sorting,
        'search_term': query,
        'category': category,
    }
    return render(request, 'resources/resources.html', context)

@login_required
def pending_resources(request):
    """set up page for pending resources"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('home'))

    products = Product.objects.filter(approved_item=0)

    context = {
        'products': products,
        'from_homepage': True,
    }
    return render(request, 'resources/resources.html', context)

def resource_details(request, slug):
    """create a new view to display item's details"""
    from_pending = False

    product = get_object_or_404(Product, slug=slug)

    if product.approved_item == 0:
        from_pending = True

    if request.method == 'POST':
        form = ApproveProductForm(
            request.POST,
            instance=product
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'You have updated the appearance of the product!'
            )
        else:
            messages.error(
                request,
                "You have failed to update this item's approval"
            )
    else:
        form = ApproveProductForm(instance=product)

    context = {
        'product': product,
        'from_pending': from_pending,
        'form': form,
    }

    return render(request, 'resources/resource-details.html', context)

@login_required
def add_resource(request):
    """set up a new view for adding new products"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'You have successfully added the new item to be reviewed!'
            )
            return redirect(reverse('pending_resources'))
        else:
            messages.error(
                request,
                'Something went wrong - Please check through the form again!'
            )
    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'resources/add-resource.html', context)

@login_required
def edit_resource(request, slug):
    """set up our view for editing resources"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('resources'))

    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'You have successfully edited { product.name }'
            )
        else:
            messages.error(request, (
                'You have failed to update this resource,'
                'Please check your form again!'
            ))
    else:
        form = ProductForm(
            instance=product
        )
        messages.info(
            request,
            f'You are editing { product.name }'
        )

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'resources/edit-resource.html', context)

@login_required
def delete_resource(request, slug):
    """set up view to delete product from db"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=slug)

    from_pending = False

    if product.approved_item==0:
        from_pending = True

    if request.method == 'POST':
        product.delete()
        messages.success(
            request,
            f'You have successfully deleted ${ product.name }'
        )
        return redirect(reverse('resources'))

    context = {
        'product': product,
        'from_pending': from_pending,
    }
    return render(request, 'resources/delete-resource.html', context)
