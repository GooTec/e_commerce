# from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView # 오브젝트를 생성하는 뷰 (form 혹은 model과 연결되서 새로운 데이터를 넣을 때 CreateView - generic view를 사용)
from django.urls import reverse_lazy

from .forms import CreateUserForm
from .models import Product


#### USER 생성 ####
class CreateUserView(CreateView): # generic view중에 CreateView를 상속받는다.
    template_name = 'shop/signup.html' # 템플릿은?
    form_class =  CreateUserForm # 푸슨 폼 사용? >> 내장 회원가입 폼을 커스터마지징 한 것을 사용하는 경우
    # form_class = UserCreationForm >> 내장 회원가입 폼 사용하는 경우
    success_url = reverse_lazy('create_user_done') # 성공하면 어디로?

class RegisteredView(TemplateView): # generic view중에 TemplateView를 상속받는다.
    template_name = 'shop/signup_done.html' # 템플릿은?

#-----------------INFOVIEW START------------------#

class InfoTemplateView(TemplateView):
    template_name =  'shop/info.html'

class IntroTemplateView(TemplateView):
    template_name =  'shop/intro.html'

class AuthTemplateView(TemplateView):
    template_name =  'shop/auth.html'

class ProcessTemplateView(TemplateView):
    template_name =  'shop/process.html'

#-----------------INFOVIEW END-----------------#


#-----------------HOME START------------------#

class HomeListView(ListView):
    template_name =  'shop/home.html'
    model = Product

    def get_queryset(self):  # 컨텍스트 오버라이딩
        return Product.objects.filter(recommend=True)

#-----------------HOME END-----------------#

#-----------------PRODUCT START------------------#

class ProductListView(ListView):
    template_name = 'shop/product_list.html'
    model = Product
    def get_queryset(self):  # 컨텍스트 오버라이딩
        return Product.objects.all()

class CategoryListView(ListView):
    template_name = 'shop/product_list.html'
    model = Product
    def get_queryset(self, **kwargs):
        category = kwargs.get('category', None)
        if category == 'gumoongo':
            return Product.objects.filter(category='Gu')
        elif category == 'haegum':
            return Product.objects.filter(category='Hae')
        elif category == 'ajeng':
            return Product.objects.filter(category='Ah')
        elif category == 'gayagum' :
            return Product.objects.filter(category='Ga')
        else :
            return Product.objects.all()

class ProductDetailView(DetailView):
    template_name = 'shop/product_detail.html'
    model =  Product
    def get_queryset(self, **kwargs):
        product_id = kwargs.get('product_id', None)
        return Product.objects.filter(pk=product_id)

#-----------------PRODUCT END------------------#

'''
 path('/', coreViews.HomeListView.as_view() , name='home'),
    path('info/', coreViews.InfoTemplateView.as_view(), name='info'),
    path('info/intro/', coreViews.IntroTemplateView.as_view(), name='intro'),
    path('info/auth/', coreViews.AuthTemplateView.as_view(), name='auth'),
    path('info/process/', coreViews.ProcessTemplateView.as_view(), name='process'),
    path('products/', coreViews.ProductListView.as_view(), name='products'),
    path('products/<int:category_id>/', coreViews.CategoryListView.as_view(), name='category' ),
    path('products/<int:product_id>/', coreViews.ProductDetailView.as_view(), name='product'),
    path('mypage/', coreViews.ProfileDetailView.as_view(), name='profile'),
    path('mypage/edit/', coreViews.ProfileUpdateView.as_view(), name='profile_edit'),
    path('mypage/cart/', coreViews.CartUpdateView.as_view(), name='cart'),
    path('mypage/order/', coreViews.OrderListView.as_view(), name='my_order'),
    path('order/', coreViews.OrderFormView.as_view(), name='order'),
]
'''
#-----------------MYPAGE START------------------#

class ProfileDetailView(DetailView):
    template_name = 'shop/profile.html'
    model = User

    def get_queryset(self, **kwargs):
        user_id = kwargs.get('user_id', None)
        return User.objects.filter(pk=user_id)

