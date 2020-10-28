
import json
from django.core.serializers.json import DjangoJSONEncoder
from django import forms
from .models import ( Category, SubCategory, ProductParent, ProductPhone, ProductCar, ProductHouse, ProductFurniture, ProductWatch, ProductApartment )

usd_valute = 10339

class ProductForm(forms.ModelForm):
	class Meta:
		model = ProductParent
		fields = '__all__'
		

class ProductPHONEForm(forms.ModelForm):
	class Meta:
		model = ProductPhone
		fields = '__all__'
		

class ProductCARForm(forms.ModelForm):
	class Meta:
		model = ProductCar
		fields = '__all__'


class ProductHOUSEForm(forms.ModelForm):
	class Meta:
		model = ProductHouse
		fields = '__all__'


class ProductFURNITUREForm(forms.ModelForm):
	class Meta:
		model = ProductFurniture
		fields = '__all__'


class ProductAPARTMENTForm(forms.ModelForm):
	class Meta:
		model = ProductApartment
		fields = '__all__'


class ProductWATCHForm(forms.ModelForm):
	class Meta:
		model = ProductWatch
		fields = '__all__'


class MiniFunctions(object):

	def __init__(self):
		pass


	def create_dict(self, product):
		obj = {}		
		for field in product._meta.get_fields():
			obj[field.name] = getattr(product, field.name)

		parentObjects = ProductParent.objects.values()
		parent = parentObjects.get(id=product.parent_product.id)

		obj['parent_product'] = parent
		return obj


	def generate_product_data(self, fields, data):
		obj = {}
		for string in fields:
			obj[string] = data[string]

		return obj


	def get_list_from_object(self, obj):
		arr = []
		for key, value in obj.items():
			arr.append({ 'key': key, 'value': value })

		return arr


	def get_all_category_data(self):
		arr = []
		all_categories = Category.objects.all()

		for category in all_categories:
			subs = []
			all_subs = SubCategory.objects.filter(parent_category=category)

			for sub in all_subs:
				subs.append({ 'name': sub.name, 'id': sub.id })

			arr.append({ 'name': category.name, 'id': category.id, 'sub': subs })

		return json.dumps(arr)


	def create_list(self, products):
		products_list = []
		json_products = []
		
		for item in products:
			if hasattr(item, 'productphone'):
				products_list.append(item.productphone)

			elif hasattr(item, 'productcar'):
				products_list.append(item.productcar)

			elif hasattr(item, 'producthouse'):
				products_list.append(item.producthouse)

			elif hasattr(item, 'productfurniture'):
				products_list.append(item.productfurniture)

			elif hasattr(item, 'productwatch'):
				products_list.append(item.productwatch)

			elif hasattr(item, 'productapartment'):
				products_list.append(item.productapartment)


		if not len(products_list):
			return { 'error': True }

		for product in products_list:
			json_product = self.create_dict(product)
			json_products.append(json_product)

		return json.dumps(json_products, sort_keys=True, indent=1, cls=DjangoJSONEncoder)


mini_func = MiniFunctions()

class FilterProducts(object):

	def __init__(self):
		pass


	def filter_list_by_type(self, arr, type_param, param):
		newarr = []
		for item in arr:
			if item[param] == type_param: newarr.append(item)

		return newarr


	def filter_list_by_from_num(self, arr, from_num, param):
		newarr = []
		for item in arr:
			if item[param] > int(from_num):
				newarr.append(item)

		return newarr


	def filter_list_by_to_num(self, arr, to_num, param):
		newarr = []
		for item in arr:
			if item[param] < int(to_num):
				newarr.append(item)

		return newarr


	def filter_list_by_bool(self, arr, boolean, param):
		newarr = []
		for item in arr:
			if item[param] == boolean:
				newarr.append(item)

		return newarr


	def filter_list_by_list(self, arr, list_param, param):
		newarr = []

		for item in arr:
			is_valid_list = []
			
			for required_param in list_param:
				if required_param in item[param]:
					is_valid_list.append(True)
				else: 
					is_valid_list.append(False)

			if not False in is_valid_list:
				newarr.append(item)

		return newarr


	def filter_products_by_title(self, q, Model, productstr):
		if not q:
			all_products = Model.objects.all()
			products_json = []

			for product in all_products:
				products_json.append( mini_func.create_dict(product) )

			return products_json

		search_result = ProductParent.objects.filter(title__contains=q)
		products = []

		for item in search_result:
			if hasattr(item, productstr):
				product = Model.objects.get(parent_product=item)
				obj = mini_func.create_dict(product)
				products.append(obj)

		return list(products)


	def filter_products(self, filter_params, Model, productstr, type_params, number_params, other_params=None):
		products = self.filter_products_by_title(filter_params['q'], Model, productstr)

		if filter_params['valute'] == 'y.e.':
			if filter_params['price_from']: 
				pr = int(filter_params['price_from'])
				filter_params['price_from'] = pr * usd_valute
			if filter_params['price_to']: 
				pr = int(filter_params['price_to'])
				filter_params['price_to'] = pr * usd_valute

		for product in products:
			if product['valute'] == 'y.e.':
				product['price'] *= usd_valute

		for param in type_params:
			if filter_params[param]:
				products = self.filter_list_by_type(products, filter_params[param], param)

		for param in number_params:
			from_txt = f'{param}_from'
			to_txt = f'{param}_to'

			if filter_params[from_txt]:
				products = self.filter_list_by_from_num(products, filter_params[from_txt], param)
			if filter_params[to_txt]:
				products = self.filter_list_by_to_num(products, filter_params[to_txt], param)

		if other_params:
			for param in other_params:
				if param['type'] == 'BOOLEAN':
					if not filter_params[param['name']] == None: products = self.filter_list_by_bool(products, filter_params[param['name']], param['name'])
				if param['type'] == 'LIST':
					if filter_params[param['name']]: products = self.filter_list_by_list(products, filter_params[param['name']], param['name'])				

		for product in products:
			if product['valute'] == 'y.e.':
				product['price'] = product['price'] / usd_valute

		return products


class CreateProduct(object):

	def __init__(self):
		pass
		

	def create_product_model(self, req, parent_model_data, Form, fields):
		product = req.POST
		category = SubCategory.objects.get(name=product['subcategory'])	
		parent_model_data['category'] = category
		parent_form = ProductForm(parent_model_data)

		if parent_form.is_valid():
			parent_form.save()
		else:
			error = mini_func.get_list_from_object(parent_form.errors)
			return { 'error': True, 'message': error }	

		parent_product = ProductParent.objects.last()
		required_fields = fields
		ready_data = mini_func.generate_product_data(required_fields, product)	
		
		ready_data['parent_product'] = parent_product
		product_form = Form(ready_data)

		if product_form.is_valid():
			product_form.save()
			return { 'error': False }
		else:
			deleted = parent_product.delete()
			print(deleted)
			error = mini_func.get_list_from_object(product_form.errors)
			return { 'error': True, 'message': error }		


	def create_product(self, req, parent_model_data):
		product = req.POST
		
		if product['category'] == 'Transport':
			if product['subcategory'] == 'Yengil mashinalar':
				required_fields = ['payment_method', 'valute', 'price', 'model', 'production_year', 'transmission', 'fuel_type', 'engine_size', 'way_length', 'condition', 'other_options', 'seller']
				return self.create_product_model(req, parent_model_data, ProductCARForm, required_fields)

		if product['category'] == 'Elektr jihozlari':
			if product['subcategory'] == 'Mobil telefon':
				required_fields = ['payment_method', 'valute', 'price', 'model', 'condition', 'seller']
				return self.create_product_model(req, parent_model_data, ProductPHONEForm, required_fields)

		if product['category'] == 'Ko\'chmas mulk':
			if product['subcategory'] == 'Xususiy uylar':
				required_fields = ['payment_method', 'valute', 'price', 'rooms_num', 'total_area', 'living_area', 'location', 'floors_num', 'ceil_height', 'with_furniture', 'condition', 'house_type', 'building_type', 'water_support', 'electricity_support', 'heating_support', 'gas_support', 'in_house', 'around_house', 'seller']
				return self.create_product_model(req, parent_model_data, ProductHOUSEForm, required_fields)

			if product['subcategory'] == 'Kvartiralar':
				required_fields = ['payment_method', 'valute', 'price', 'house_type', 'total_area', 'living_area', 'rooms_num', 'kitchen_area', 'floor', 'with_furniture', 'condition', 'total_floor', 'building_type', 'plan', 'construction_year', 'sanuzel', 'ceil_height', 'in_house', 'around_house', 'seller']
				return self.create_product_model(req, parent_model_data, ProductAPARTMENTForm, required_fields)
				
		if product['category'] == 'Uy va bog\'':
			if product['subcategory'] == 'Mebel':
				required_fields = ['payment_method', 'valute', 'price', 'furniture_type', 'condition', 'seller']
				return self.create_product_model(req, parent_model_data, ProductFURNITUREForm, required_fields)

		if product['category'] == 'Moda va stil':
			if product['subcategory'] == 'Qo\'l soatlari':
				required_fields = ['payment_method', 'valute', 'price', 'model', 'condition', 'seller']
				return self.create_product_model(req, parent_model_data, ProductWATCHForm, required_fields)

		else:		
			return { 'error': True, 'message': 'Typing Error or Not function exist!' }