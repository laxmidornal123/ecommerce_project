from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Avg, Q
from django.core.paginator import Paginator

from .models import Product, Review, Wishlist
from orders.models import OrderItem


# 🔍 HOME PAGE (SEARCH + CATEGORY + PAGINATION + WISHLIST)
def home(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    product_list = Product.objects.all()

    # 🔍 SEARCH FILTER
    if query:
        product_list = product_list.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    # 📂 CATEGORY FILTER (NEW 🔥)
    # CATEGORY FILTER
    if category:
       product_list = product_list.filter(category__iexact=category.strip())
    # 📄 PAGINATION
    paginator = Paginator(product_list, 12)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    # ❤️ WISHLIST ITEMS
    wishlist_items = []
    wishlist_count = 0

    if request.user.is_authenticated:
        wishlist_items = Wishlist.objects.filter(user=request.user)\
                                         .values_list('product_id', flat=True)

        wishlist_count = Wishlist.objects.filter(user=request.user).count()

    return render(request, 'products/home.html', {
        'products': products,
        'query': query,
        'wishlist_items': wishlist_items,
        'wishlist_count': wishlist_count,   # 🔥 for navbar badge
        'selected_category': category       # 🔥 optional UI highlight
    })


# 🛍 PRODUCT DETAIL + REVIEW SYSTEM
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    reviews = Review.objects.filter(product=product)

    # ⭐ Average rating
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    # ✅ Check purchase
    if request.user.is_authenticated:
        has_purchased = OrderItem.objects.filter(
            order__user=request.user,
            product=product
        ).exists()
    else:
        has_purchased = False

    # 📝 Add review
    if request.method == "POST" and has_purchased:
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        Review.objects.create(
            product=product,
            user=request.user,
            rating=rating,
            comment=comment
        )

        return redirect('product_detail', slug=product.slug)

    return render(request, 'products/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'has_purchased': has_purchased
    })


# ❤️ ADD TO WISHLIST
def add_to_wishlist(request, product_id):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    product = get_object_or_404(Product, id=product_id)

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect('/')


# ❤️ REMOVE FROM WISHLIST
def remove_from_wishlist(request, product_id):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    product = get_object_or_404(Product, id=product_id)

    Wishlist.objects.filter(
        user=request.user,
        product=product
    ).delete()

    return redirect('/wishlist/')


# ❤️ WISHLIST PAGE
def wishlist_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    items = Wishlist.objects.filter(user=request.user)

    return render(request, 'products/wishlist.html', {
        'items': items
    })


# ❤️ TOGGLE WISHLIST (AJAX)
def toggle_wishlist(request, product_id):
    if not request.user.is_authenticated:
        return JsonResponse({'status': 'login_required'})

    product = get_object_or_404(Product, id=product_id)

    obj, created = Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        obj.delete()
        return JsonResponse({'status': 'removed'})
    else:
        return JsonResponse({'status': 'added'})