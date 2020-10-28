
from django.db import models
from django.contrib.auth.models import User
from . import utils


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    parent_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class ProductParent(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=70, null=True)
    category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, null=True)
    image_url = models.URLField(null=True)
    address = models.CharField(max_length=10000, choices=utils.ADDRESS, null=True)
    contact_phone = models.CharField(max_length=200, null=True)
    contact_email = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class ProductPhone(models.Model):
    parent_product = models.OneToOneField(ProductParent, on_delete=models.CASCADE, null=True)
    payment_method = models.CharField(max_length=100, choices=utils.PAYMENT_METHOD, null=True)
    valute = models.CharField(max_length=100, choices=utils.VALUTE, null=True)
    price = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=100, choices=utils.PHONE_MODEL, null=True)
    condition = models.CharField(max_length=100, choices=utils.PHONE_CONDITION, null=True)
    seller = models.CharField(max_length=100, choices=utils.SELLER, null=True)

    def __str__(self):
        return self.parent_product.title


class ProductCar(models.Model):
    parent_product = models.OneToOneField(ProductParent, on_delete=models.CASCADE, null=True)
    payment_method = models.CharField(max_length=100, choices=utils.CAR_PAYMENT_METHOD, null=True)
    valute = models.CharField(max_length=100, choices=utils.VALUTE, null=True)
    price = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=100, choices=utils.CAR_MODEL, null=True)
    production_year = models.IntegerField(null=True)
    transmission = models.CharField(max_length=100, choices=utils.CAR_TRANSMISSION, null=True)
    fuel_type = models.CharField(max_length=100, choices=utils.CAR_FUEL_TYPE, null=True)
    engine_size = models.IntegerField(null=True)
    way_length = models.IntegerField(null=True)
    condition = models.CharField(max_length=100, choices=utils.CAR_CONDITION, null=True)
    other_options = models.CharField(max_length=10000, null=True)
    seller = models.CharField(max_length=100, choices=utils.SELLER, null=True)
    
    def __str__(self):
        return self.parent_product.title


class ProductHouse(models.Model):
    parent_product = models.OneToOneField(ProductParent, on_delete=models.CASCADE, null=True)
    payment_method = models.CharField(max_length=100, null=True)
    valute = models.CharField(max_length=100, choices=utils.VALUTE, null=True)
    price = models.IntegerField(blank=True, null=True)
    rooms_num = models.IntegerField(null=True)
    total_area = models.IntegerField(null=True)
    living_area = models.IntegerField(null=True)
    location = models.CharField(max_length=100, choices=utils.HOUSE_LOCATION, null=True)
    floors_num = models.IntegerField(null=True)
    ceil_height = models.IntegerField(null=True)
    with_furniture = models.BooleanField(null=True)
    condition = models.CharField(max_length=100, choices=utils.HOUSE_CONDITION, null=True)
    house_type = models.CharField(max_length=100, choices=utils.HOUSE_TYPE, null=True)
    building_type = models.CharField(max_length=100, choices=utils.HOUSE_BUILDING_TYPE, null=True)
    water_support = models.CharField(max_length=100, choices=utils.HOUSE_WATER, null=True)
    electricity_support = models.CharField(max_length=100, choices=utils.HOUSE_ELECTRICITY, null=True)
    heating_support = models.CharField(max_length=100, choices=utils.HOUSE_HEATING, null=True)
    gas_support = models.CharField(max_length=100, choices=utils.HOUSE_GAS, null=True)
    in_house = models.CharField(max_length=10000, null=True)
    around_house = models.CharField(max_length=10000, null=True)
    seller = models.CharField(max_length=100, choices=utils.SELLER, null=True)
    
    def __str__(self):
        return self.parent_product.title


class ProductFurniture(models.Model):
    parent_product = models.OneToOneField(ProductParent, on_delete=models.CASCADE, null=True)
    payment_method = models.CharField(max_length=100, choices=utils.PAYMENT_METHOD, null=True)
    valute = models.CharField(max_length=100, choices=utils.VALUTE, null=True)
    price = models.IntegerField(blank=True, null=True)
    furniture_type = models.CharField(max_length=100, choices=utils.FURNITURE_TYPE, null=True)
    condition = models.CharField(max_length=100, choices=utils.PHONE_CONDITION, null=True)
    seller = models.CharField(max_length=100, choices=utils.SELLER, null=True)
    
    def __str__(self):
        return self.parent_product.title


class ProductWatch(models.Model):
    parent_product = models.OneToOneField(ProductParent, on_delete=models.CASCADE, null=True)
    payment_method = models.CharField(max_length=100, choices=utils.PAYMENT_METHOD, null=True)
    valute = models.CharField(max_length=100, choices=utils.VALUTE, null=True)
    price = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=100, choices=utils.WATCH_MODEL, null=True)
    condition = models.CharField(max_length=100, choices=utils.PHONE_CONDITION, null=True)
    seller = models.CharField(max_length=100, choices=utils.SELLER, null=True)
    
    def __str__(self):
        return self.parent_product.title


class ProductApartment(models.Model):
    parent_product = models.OneToOneField(ProductParent, on_delete=models.CASCADE, null=True)
    payment_method = models.CharField(max_length=100, null=True)
    valute = models.CharField(max_length=100, choices=utils.VALUTE, null=True)
    price = models.IntegerField(blank=True, null=True)
    house_type = models.CharField(max_length=100, choices=utils.APARTMENT_TYPE, null=True)
    rooms_num = models.IntegerField(null=True)
    total_area = models.IntegerField(null=True)
    living_area = models.IntegerField(null=True)
    kitchen_area = models.IntegerField(null=True)
    floor = models.IntegerField(null=True)
    total_floor = models.IntegerField(null=True)
    building_type = models.CharField(max_length=100, choices=utils.HOUSE_BUILDING_TYPE, null=True)
    plan = models.CharField(max_length=100, choices=utils.APARTMENT_PLAN, null=True)
    construction_year = models.IntegerField(null=True)
    sanuzel = models.CharField(max_length=100, choices=utils.APARTMENT_SANUZEL, null=True)
    with_furniture = models.BooleanField(null=True)
    ceil_height = models.IntegerField(null=True)
    in_house = models.CharField(max_length=10000, null=True)
    around_house = models.CharField(max_length=10000, null=True)
    condition = models.CharField(max_length=100, choices=utils.HOUSE_CONDITION, null=True)    
    seller = models.CharField(max_length=100, choices=utils.SELLER, null=True)
    
    def __str__(self):
        return self.parent_product.title