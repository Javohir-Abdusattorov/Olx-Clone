
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),

	path('register/', views.register, name='register'),
	path('login/', views.login_user, name='login'),
	path('logout/', views.logout_user, name='logout'),

	path('category/<int:categoryID>', views.category_list, name='category-list'),
	path('address/<str:addressName>', views.address_list, name='address-list'),
	path('search/', views.search_list, name='search-list'),
	path('filter/', views.filter_products, name='filter-list'),

	path('create-ad/', views.create_announcement, name='create-ad'),
	path('delete-ad/<int:id>', views.delete_ad, name='delete-ad'),
	path('ad/<int:id>', views.ad_page, name='ad'),
	path('user-ads/<int:userID>', views.user_ads, name='user-ads'),
	path('user-saved-ads', views.saved_ads, name='user-saved-ads'),
]
