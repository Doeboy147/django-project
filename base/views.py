from django.db.models.fields import FloatField
from django.http import JsonResponse
from django.shortcuts import render
from .models import Product, Vendor, Order
import random, re
from django.db.models import F, Sum
from datetime import timedelta, date

# Create your views here.


def home(request):
    vendor_filter = request.GET.get('filter')
    if request.method == 'GET' and vendor_filter and vendor_filter != 'all':
        products = Product.objects.filter(vendor=request.GET.get('filter'))
    else:
        products = Product.objects.all()
    vendors = Vendor.objects.all()
    totalProducts = Product.objects.count()
    return render(request, 'home.html', {'products': products, 'vendors': vendors, 'total': totalProducts})


def create_order(request):
    if request.method == 'POST':
        VAT = 0
        product_ids = request.POST.get('product_ids')
        clean_ids = re.findall(r'(\d+)', product_ids)
        for id in clean_ids:
            product = Product.objects.get(pk=id);
            VAT += product.price * 0.15

        customerOrder = Order()
        customerOrder.order_number = random.randint(0, 12)
        customerOrder.total = request.POST.get('total')
        customerOrder.delivery_date = date.today() + timedelta(days=6)
        customerOrder.sub_total = request.POST.get('total')
        customerOrder.vat = VAT
        customerOrder.ordered_item = clean_ids
        customerOrder.status = 'Pending'
        customerOrder.save()

    return JsonResponse({'success': clean_ids})


def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders' : orders})