from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .cores import views as coreViews

app_name = 'shop'
urlpatterns = [
    path('', coreViews.HomeListView.as_view(), name='home'),
    url('accounts/signup/', coreViews.CreateUserView.as_view(), name = 'signup'),
    url('accounts/login/done/', coreViews.RegisteredView.as_view(), name = 'create_user_done'),
    path('info/', coreViews.InfoTemplateView.as_view(), name='info'),
    path('info/intro/', coreViews.IntroTemplateView.as_view(), name='intro'),
    path('info/auth/', coreViews.AuthTemplateView.as_view(), name='auth'),
    path('info/process/', coreViews.ProcessTemplateView.as_view(), name='process'),
    path('products/', coreViews.ProductListView.as_view(), name='products'),
    path('products/<slug:category>/', coreViews.CategoryListView.as_view(), name='category' ),
    path('products/<int:product_id>/', coreViews.ProductDetailView.as_view(), name='product'),
    path('mypage/', coreViews.ProfileDetailView.as_view(), name='profile'),
    path('mypage/create', coreViews.ProfileCreateView.as_view(), name='profile_create'),
    path('mypage/edit/<int:pk>', coreViews.ProfileUpdateView.as_view(), name='profile_edit'),
    # path('mypage/cart/', coreViews.CartUpdateView.as_view(), name='cart'),
    # path('mypage/order/', coreViews.OrderListView.as_view(), name='my_order'),
    # path('order/', coreViews.OrderFormView.as_view(), name='order'),
]
# r'^profile/(?P<username>[\w.@+-]+)/$
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
