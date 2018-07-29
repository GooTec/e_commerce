from django.contrib import admin
from django.urls import path, include, url

from .cores import views as coreViews

app_name = 'shop'
urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    path('/', coreViews.HomeListView.as_view() , name='home'),
    path('info/', coreViews.InfoTemplateView.as_view(), name='info'),
    path('info/intro/', coreViews.IntroTemplateView.as_view(), name='intro'),
    path('info/auth/', coreViews.AuthTemplateView.as_view(), name='auth'),
    path('info/process/', coreViews.ProcessTemplateView.as_view(), name='process'),
    path('products/', coreViews.ProductListView.as_view(), name='products'),
    path('products/<int:category_id>/', coreViews.CategoryListView.as_view(), name='category' ),
    path('products/<int:product_id>/', coreViews.ProductDetailView.as_view(), name='product'),
    path('mypage/', coreViews.ProfileDetailView.as_view(), name='profile'),
    path('mypage/edit', coreViews.ProfileUpdateView.as_view(), name='profile_edit'),
    path('mypage/cart', coreViews.CartUpdateView.as_view(), name='cart'),
    path('')
]
