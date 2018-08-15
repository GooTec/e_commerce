from django.contrib import admin
from django.urls import path,re_path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .cores import views as coreViews

app_name = 'shop'
urlpatterns = [
    path('', coreViews.HomeListView.as_view(), name='home'),
    url('accounts/signup/', coreViews.CreateUserView.as_view(), name = 'signup'),
    url('accounts/login/done/', coreViews.RegisteredView.as_view(), name = 'create_user_done'),
    path('accounts/findpw/', coreViews.findPW , name='findPW'),
    path('idCheck/', coreViews.idCheck , name='id_check'),

    path('info/', coreViews.InfoTemplateView.as_view(), name='info'),
    path('info/intro/', coreViews.IntroTemplateView.as_view(), name='intro'),
    path('info/auth/', coreViews.AuthTemplateView.as_view(), name='auth'),
    path('info/process/', coreViews.ProcessTemplateView.as_view(), name='process'),
    path('products/', coreViews.ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', coreViews.ProductDetailView.as_view(), name='product'),
    path('products/<slug:category>/', coreViews.CategoryListView.as_view(), name='category' ),
    path('mypage/', coreViews.ProfileDetailView.as_view(), name='profile'),
    path('mypage/create', coreViews.ProfileCreateView.as_view(), name='profile_create'),
    path('mypage/edit/<int:pk>', coreViews.ProfileUpdateView.as_view(), name='profile_edit'),
    path('mypage/cart/', coreViews.CartListView.as_view(), name='cart'),
    path('mypage/cart/<int:pk>/', coreViews.CartDeleteView.as_view(), name='cart_delete'),

    path('mypage/order/', coreViews.OrderListView.as_view(), name='my_order'),
    re_path('^mypage/order/(?P<pk>\d+)/$', coreViews.OrderDetailView.as_view(), name='order_detail'),

    path('order/cart/', coreViews.OrderCreateView.as_view(), name='order'),
    re_path('^order/(?P<pk>\d+)/$', coreViews.OrderCreateByProductView.as_view(), name='order_product'),

]
# r'^profile/(?P<username>[\w.@+-]+)/$
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
