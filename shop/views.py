from django.shortcuts import render, get_object_or_404


from .models import Category, Product


def products_list(request, slug=None):
    categories = Category.objects.all()
    if not slug:
        products = Product.objects.all()
        title = "All"
    else:
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=category)
        title = category.name
    return render(request, 'shop/list.html',
                  {'title': title,
                   'products': products,
                   'categories': categories})


def products_by_category(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    title = "By Category"
    return render(request, 'shop/products_by_category.html',
                  {'title': title,
                   'products': products,
                   'categories': categories})


def product_detail(request, slug, id):
    product = get_object_or_404(Product, slug=slug)
    categories = Category.objects.all()
    title = "Produect Detail"
    return render(request, 'shop/detail.html',
                  {'title': title,
                   'product': product,
                   'categories': categories})
