
import json
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import serializers

from . import utils
from .models import ( Category, SubCategory, ProductParent, ProductPhone, ProductCar, ProductHouse, ProductFurniture, ProductWatch, ProductApartment )
from .selector import ( CreateProduct, FilterProducts, MiniFunctions )
from .forms import CreateUserForm

create_product = CreateProduct()
filter_product = FilterProducts()
mini_functions = MiniFunctions()


def index(req):
	products = []
	products.append(ProductCar.objects.last())
	products.append(ProductPhone.objects.last())
	products.append(ProductHouse.objects.last())
	products.append(ProductFurniture.objects.last())
	products.append(ProductWatch.objects.last())
	products.append(ProductApartment.objects.last())

	context = {
		'products': products,
		'city': utils.address,
		'category': mini_functions.get_all_category_data()
	}
	return render(req, 'index.html', context)


def category_list(req, categoryID):
	subcategory = SubCategory.objects.get(id=categoryID)
	products = ProductParent.objects.filter(category=subcategory)
	ready = mini_functions.create_list(products)
	
	if type(ready) == dict:
		return redirect('home')

	context = {
		'products': ready,
		'category': subcategory.name,
		'city': utils.address,
		'valute': [ utils.valute[0], utils.valute[1] ],
		'payment_method': utils.payment_method,
		'seller': utils.seller,
	}
	context.update(utils.context)

	return render(req, 'category-list.html', context)


def address_list(req, addressName):
	products = ProductParent.objects.filter(address=addressName)
	ready = mini_functions.create_list(products)
	
	if type(ready) == dict:
		return redirect('home')

	context = {
		'products': ready,
	}
	return render(req, 'list.html', context)


def search_list(req):
	q = req.GET.get('q')
	if not q:
		return HttpResponse('404')

	search_result = ProductParent.objects.filter(title__contains=q)
	ready = mini_functions.create_list(search_result)

	if type(ready) == dict:
		return redirect('home')

	context = {
		'products': ready,
	}
	return render(req, 'list.html', context)


def filter_products(req):
	if not req.method == 'POST': return

	filter_params = json.loads(req.POST['data'])
	category = filter_params['category']
	products = []
	
	if category == 'Yengil mashinalar':
		type_params = ['model', 'fuel_type', 'transmission', 'condition', 'seller', 'payment_method']
		number_params = ['price', 'engine_size', 'way_length', 'production_year']
		products = filter_product.filter_products(filter_params, ProductCar, 'productcar', type_params, number_params)

	elif category == 'Mobil telefon':
		type_params = ['model', 'condition', 'seller', 'payment_method']
		number_params = ['price']
		products = filter_product.filter_products(filter_params, ProductPhone, 'productphone', type_params, number_params)

	elif category == 'Mebel':
		type_params = ['furniture_type', 'condition', 'seller', 'payment_method']
		number_params = ['price']
		products = filter_product.filter_products(filter_params, ProductFurniture, 'productfurniture', type_params, number_params)

	elif category == 'Xususiy uylar':
		type_params = ['location', 'condition', 'seller', 'house_type', 'building_type', 'water_support', 'electricity_support', 'heating_support', 'gas_support']
		number_params = ['rooms_num', 'price', 'total_area', 'living_area', 'floors_num', 'ceil_height']
		other_params = [{ 'name': 'with_furniture', 'type': 'BOOLEAN' }, { 'name': 'in_house', 'type': 'LIST' }, { 'name': 'around_house', 'type': 'LIST' }]
		products = filter_product.filter_products(filter_params, ProductHouse, 'producthouse', type_params, number_params, other_params)

	elif category == 'Qo\'l soatlari':
		type_params = ['model', 'condition', 'seller', 'payment_method']
		number_params = ['price']
		products = filter_product.filter_products(filter_params, ProductWatch, 'productwatch', type_params, number_params)

	elif category == 'Kvartiralar':
		type_params = ['plan', 'condition', 'seller', 'house_type', 'building_type', 'sanuzel']
		number_params = ['rooms_num', 'price', 'total_area', 'kitchen_area', 'living_area', 'floor', 'total_floor', 'construction_year', 'ceil_height']
		other_params = [{ 'name': 'with_furniture', 'type': 'BOOLEAN' }, { 'name': 'in_house', 'type': 'LIST' }, { 'name': 'around_house', 'type': 'LIST' }]
		products = filter_product.filter_products(filter_params, ProductApartment, 'productapartment', type_params, number_params, other_params)


	return JsonResponse(products, safe=False)


@login_required(login_url='login')
def create_announcement(req):
	if req.method == 'POST':
		product = req.POST

		main_data = {
			'user': req.user,	
			'title': product['title'],
			'image_url': product['image_url'],
			'description': product['description'],
			'address': product['city'],
			'contact_phone': product['contact_phone'],
			'contact_email': product['contact_email'],
		}
		res = create_product.create_product(req, main_data)
		return JsonResponse(res, safe=False)

	categories = Category.objects.all()
	subcategories = SubCategory.objects.all()
	subcategories_data = []

	for sub in subcategories:
		subcategories_data.append({ 'name': sub.name, 'parent_category': sub.parent_category.name })

	context = {
		'categories': categories,
		'subcategories': json.dumps( list(subcategories_data) ),
		'city': utils.address,
		'valute': [ utils.valute[0], utils.valute[1] ],
		'payment_method': utils.payment_method,
		'seller': utils.seller,
	}	
	context.update(utils.context)

	return render(req, 'create-announcement.html', context)


def ad_page(req, id):
	product = ProductParent.objects.get(id=id)
	subproduct = {}
	product_tags = {}
	other_tags = []

	if hasattr(product, 'productphone'):
		subproduct = product.productphone
		product_tags = {
			'Model': subproduct.model,
			'Holati': subproduct.condition,
			'Sotuvchi': subproduct.seller,
			'Viloyat': product.address,
			'Rukn': product.category,
		}

	elif hasattr(product, 'productcar'):
		subproduct = product.productcar
		other_options = json.loads(subproduct.other_options)

		product_tags = {
			'Model': subproduct.model,
			'Ishlab chiqarilgan yili': subproduct.production_year,
			'Bosgan yo\'li': f'{subproduct.way_length} km',
			'Uzatmalar qutisi': subproduct.transmission,
			'Dvigatel hajmi': subproduct.engine_size,
			'Yoqilg\'i turi': subproduct.fuel_type,
			'Mashina holati': subproduct.condition,
			'Sotuvchi': subproduct.seller,
			'Viloyat': product.address,
			'Rukn': product.category,
		}

		if len(other_options):
			obj = { 'name': 'Qo\'shimcha optsiyalar', 'options': [] }		
			for category in other_options:
				obj['options'].append({ 'name': category, 'link': '#' })

			other_tags.append(obj)

	elif hasattr(product, 'producthouse'):
		subproduct = product.producthouse
		in_house = json.loads(subproduct.in_house)
		around_house = json.loads(subproduct.around_house)
		with_furniture = ''

		if subproduct.with_furniture: with_furniture = 'Bor'
		elif not subproduct.with_furniture: with_furniture = 'Yo\'q'

		product_tags = {
			'Xonalar soni': subproduct.rooms_num,
			'Umumiy maydon': subproduct.total_area,
			'Yashash maydoni': subproduct.living_area,
			'Joylashuvi': subproduct.location,
			'Uy qavatliligi': subproduct.floors_num,
			'Shiftining balandligi': subproduct.ceil_height,
			'Mebel': with_furniture,
			'Uy holati': subproduct.condition,
			'Uy turi': subproduct.house_type,
			'Qurilish turi': subproduct.building_type,
			'Suv ta\'minoti': subproduct.water_support,
			'Elektr ta\'minoti': subproduct.electricity_support,
			'Isitish': subproduct.heating_support,
			'Gaz ta\'minoti': subproduct.gas_support,
			'Sotuvchi': subproduct.seller,
			'Viloyat': product.address,
			'Rukn': product.category,
		}

		if len(in_house):
			obj = { 'name': 'Uyda bor', 'options': [] }		
			for category in in_house:
				obj['options'].append({ 'name': category, 'link': '#' })

			other_tags.append(obj)

		if len(around_house):
			obj = { 'name': 'Yaqinida joylashgan', 'options': [] }		
			for category in around_house:
				obj['options'].append({ 'name': category, 'link': '#' })

			other_tags.append(obj)

	elif hasattr(product, 'productfurniture'):
		subproduct = product.productfurniture
		product_tags = {
			'Mebel turi': subproduct.furniture_type,
			'Holati': subproduct.condition,
			'Sotuvchi': subproduct.seller,
			'Viloyat': product.address,
			'Rukn': product.category,
		}

	elif hasattr(product, 'productwatch'):
		subproduct = product.productwatch
		product_tags = {
			'Marka': subproduct.model,
			'Holati': subproduct.condition,
			'Sotuvchi': subproduct.seller,
			'Viloyat': product.address,
			'Rukn': product.category,
		}

	elif hasattr(product, 'productapartment'):
		subproduct = product.productapartment
		in_house = json.loads(subproduct.in_house)
		around_house = json.loads(subproduct.around_house)
		with_furniture = ''

		if subproduct.with_furniture: with_furniture = 'Bor'
		elif not subproduct.with_furniture: with_furniture = 'Yo\'q'

		product_tags = {
			'Uy turi': subproduct.house_type,
			'Xonalar soni': subproduct.rooms_num,
			'Umumiy maydon': subproduct.total_area,
			'Yashash maydoni': subproduct.living_area,
			'Oshxona maydoni': subproduct.kitchen_area,
			'Qavati': subproduct.floor,
			'Uy qavatliligi': subproduct.total_floor,
			'Qurilish turi': subproduct.building_type,
			'Rejasi': subproduct.plan,
			'Qurilgan/topshiriladigan yil': subproduct.construction_year,
			'Sanuzel': subproduct.sanuzel,
			'Mebel': with_furniture,
			'Shiftining balandligi': subproduct.ceil_height,
			'Ta\'miri': subproduct.condition,
			'Sotuvchi': subproduct.seller,
			'Viloyat': product.address,
			'Rukn': product.category,
		}

		if len(in_house):
			obj = { 'name': 'Uyda bor', 'options': [] }		
			for category in in_house:
				obj['options'].append({ 'name': category, 'link': '#' })

			other_tags.append(obj)

		if len(around_house):
			obj = { 'name': 'Yaqinida joylashgan', 'options': [] }		
			for category in around_house:
				obj['options'].append({ 'name': category, 'link': '#' })

			other_tags.append(obj)

	tags = mini_functions.get_list_from_object(product_tags)

	context = {
		'product': product,
		'subproduct': subproduct,
		'tags': tags,
		'other_tags': other_tags,
	}
	return render(req, 'ad-page.html', context)
	

def delete_ad(req, id):
	parent = ProductParent.objects.get(id=id)
	product = {}

	if hasattr(parent, 'productphone'):
		product = parent.productphone

	elif hasattr(parent, 'productcar'):
		product = parent.productcar

	elif hasattr(parent, 'producthouse'):
		product = parent.producthouse

	elif hasattr(parent, 'productfurniture'):
		product = parent.productfurniture

	elif hasattr(parent, 'productwatch'):
		product = parent.productwatch

	elif hasattr(parent, 'productapartment'):
		product = parent.productapartment

	parent.delete()
	product.delete()

	return JsonResponse({ 'deleted': True})


@login_required(login_url='login')
def user_ads(req, userID):
	products = ProductParent.objects.filter(user_id=userID)
	ready = mini_functions.create_list(products)

	if type(ready) == dict:
		return redirect('home')

	context = {
		'products': ready,
	}
	return render(req, 'users/user-ads.html', context)


def saved_ads(req):
	products = []
	ids = json.loads(req.GET.get('products'))

	for prod in ids:
		products.append(ProductParent.objects.get(id=prod))

	ready = mini_functions.create_list(products)

	if type(ready) == dict:
		return redirect('home')

	context = {
		'products': ready,
	}
	return render(req, 'list.html', context)	


def register(req):
    form = CreateUserForm()

    if req.method == 'POST':
        form = CreateUserForm(req.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')

    context = { 'form': form } 
    return render(req, 'users/register.html', context)


def login_user(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)
        
        if user is not None:
            login(req, user)
            return redirect('home')
        else:
            messages.error(req, 'Username or password is invalid')

    return render(req, 'users/login.html', {})


def logout_user(req):
    logout(req)
    return redirect('login')