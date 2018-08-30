# from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core import mail

import locale

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView ,DeleteView# 오브젝트를 생성하는 뷰 (form 혹은 model과 연결되서 새로운 데이터를 넣을 때 CreateView - generic view를 사용)
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import  View
from .forms import CreateUserForm, ProfileCreateForm, CartItemForm ,OrderCreateForm , OrderItemCreateForm
from .models import Product, Profile , CartItem, Order, OrderItem






#### USER 생성 ####
class CreateUserView(CreateView): # generic view중에 CreateView를 상속받는다.
    template_name = 'registration/signup.html' # 템플릿은?
    form_class =  CreateUserForm # 푸슨 폼 사용? >> 내장 회원가입 폼을 커스터마지징 한 것을 사용하는 경우
    # form_class = UserCreationForm >> 내장 회원가입 폼 사용하는 경우

    success_url = reverse_lazy('shop:create_user_done') # 성공하면 어디로?

    def form_valid(self, form):
        print(form)
        super_log = super(CreateUserView, self).form_valid(form)
        print(super_log)
        return super_log


class RegisteredView(TemplateView): # generic view중에 TemplateView를 상속받는다.
    template_name = 'registration/signup_done.html' # 템플릿은?

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
    locale.setlocale(locale.LC_ALL, 'en_US.utf-8')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {}
        context['object_list'] = Product.objects.all()
        context['categories'] = Product.count_of_category(Product)
        context['best'] = Product.count_of_best(Product)

        for item in context['object_list'] :
            item.price = locale.currency(item.price, grouping=True)

        return context

class CategoryListView(ListView):
    template_name = 'shop/product_list.html'
    model = Product

    def get_context_data(self, **kwargs):
        category  = self.kwargs['category']
        context = {}
        context['object_list'] = Product.objects.filter(category=category)
        locale.setlocale(locale.LC_ALL ,'en_US.utf-8')

        for item in context['object_list'] :
            item.price = locale.currency(item.price, grouping=True)

        context['categories'] = Product.count_of_category(Product)
        context['best'] = Product.count_of_best(Product)

        return context



class BestListView(ListView):
    template_name = 'shop/product_list.html'
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {}
        context['object_list'] = Product.objects.filter(recommend=True)
        locale.setlocale(locale.LC_ALL ,'en_US.utf-8')
        for item in context['object_list'] :
            item.price = locale.currency(item.price, grouping=True)

        context['categories'] = Product.count_of_category(Product)
        context['best'] = Product.count_of_best(Product)
        return context

class ProductDetailView(FormMixin, DetailView):
    template_name = 'shop/product_detail.html'
    model =  Product
    form_class =  CartItemForm
    # def get_queryset(self, **kwargs):
    #     product_id = self.kwargs['pk']
    #     print(product_id)
    #     return Product.objects.filter(pk =product_id)

    def get_success_url(self):
        return reverse_lazy('shop:cart')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_active:
            return redirect('login')
        self.object = self.get_object()
        form = self.get_form()
        form.instance.count = request.POST['count']
        form.instance.price = int(self.object.price) * int(form.instance.count)
        # form.instance.price = self.object.price
        print(form.instance.price, form.instance.count)
        form.instance.user = self.request.user
        form.instance.product = self.object
        if form.is_valid():
            return self.form_valid(form)
        else:
            print("form is invalid")
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        # print(self.object)
        # form.instance.save()
        form.save()
        return super().form_valid(form)

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

class ProfileDetailView(ListView):
    template_name = 'shop/profile.html'
    model = Profile
    def get_queryset(self):
        user_id = self.request.user.id
        return Profile.objects.filter(pk=user_id)

    def get(self, request, *args, **kwargs):
        """
        Same as django.views.generic.edit.ProcessFormView.get(), but adds test cookie stuff
        """
        if not self.request.user.is_active:
            return redirect('login')
        print("HERE")
        return super(ProfileDetailView, self).get(request, *args, **kwargs)

class ProfileCreateView(CreateView):
    template_name = 'shop/profile_create.html'  # 템플릿은?
    form_class = ProfileCreateForm  # 푸슨 폼 사용? >> 내장 회원가입 폼을 커스터마지징 한 것을 사용하는 경우
    model = Profile
    # form_class = UserCreationForm >> 내장 회원가입 폼 사용하는 경우
    success_url = reverse_lazy('shop:profile')  # 성공하면 어디로?
    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super(ProfileCreateView, self).form_valid(form)




class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['fullname', 'phone', 'address', 'address_detail']
    template_name ='shop/profile_edit.html'
    success_url ='/mypage/'

#---------------CART START-----------------#
class CartListView(ListView):
    template_name =  'shop/cart.html'
    model = CartItem

    def get_context_data(self, *, object_list=None, **kwargs):
        if not self.request.user.is_active:
            return redirect('login')
        carts = self.model.objects.filter(user_id=self.request.user).values()
        context= {}
        objects = []
        for cart in carts :
            info = {}
            product_info = Product.objects.get(pk=cart['product_id'])
            info['cart_id'] = cart['cart_id']
            info['product_name'] = product_info.name
            info['product_id'] = product_info.product_id
            info['price'] = product_info.price
            info['count'] = cart['count']
            info['total'] = cart['price']
            objects.append(info)

        context['objects'] = objects
        # context = super(CartItem, self).get_context_data(**kwargs)
        return context

class CartDeleteView(DeleteView):
    model = CartItem
    success_url = reverse_lazy('shop:cart')

    def get(self, *a, **kw):
        if not self.request.user.is_active:
            return redirect('login')
        return self.delete(*a, **kw)


#---------------CART END----------------------#

#----------------ORDER START------------------#

class OrderCreateView(CreateView):
    template_name = 'shop/order_create.html'  # 템플릿은?
    form_class = OrderCreateForm
    model = Order
    success_url = reverse_lazy('shop:home')  # 성공하면 어디로?

    def get_context_data(self,* , object_list=None, **kwargs):
        if not self.request.user.is_active:
            return redirect('login')
        carts = CartItem.objects.filter(user_id=self.request.user).values()
        context = {}
        objects = []
        for cart in carts:
            info = {}
            product_info = Product.objects.get(pk=cart['product_id'])
            info['cart_id'] = cart['cart_id']
            info['product_name'] = product_info.name
            info['price'] = product_info.price
            info['count'] = cart['count']
            info['total'] = cart['price']
            objects.append(info)
        context['objects'] = objects
        print(objects)
        # context = super(CartItem, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(OrderCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if not request.user.is_active:
            return redirect('login')
        self.object = self.get_object()
        form = self.get_form()
        form.instance.count = request.POST['count']
        form.instance.price = int(self.object.price) * int(form.instance.count)
        # form.instance.price = self.object.price
        print(form.instance.price, form.instance.count)
        form.instance.user = self.request.user
        form.instance.product = self.object
        if form.is_valid():
            return self.form_valid(form)
        else:
            print("form is invalid")
            return self.form_invalid(form)

class OrderCreateByProductView(CreateView):
    template_name = 'shop/order_create.html'  # 템플릿은?
    form_class = OrderCreateForm
    model = Order
    success_url = reverse_lazy('shop:home')  # 성공하면 어디로?

    def get_context_data(self, *, object_list=None, **kwargs):
        if not self.request.user.is_active:
            return redirect('login')
        context = super(OrderCreateByProductView, self).get_context_data(**kwargs)
        product = Product.objects.get(pk=self.kwargs['pk'])
        context['product'] = product
        context['itemform'] =  OrderItemCreateForm
        return context

    def form_valid(self, form):
        return super(OrderCreateByProductView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if not request.user.is_active:
            return redirect('login')
        # self.object = self.get_object()
        order_form = self.get_form()
        order_item = OrderItem()
        order_form.instance.fullname = request.POST['fullname']
        order_form.instance.phone = request.POST['phone']
        order_form.instance.address = request.POST['address']
        order_form.instance.address_detail = request.POST['address_detail']
        order_form.instance.user = self.request.user
        order_form.instance.total = 0
        order_form.instance.status = '0'
        if self.form_valid(order_form):
            current_order = order_form.save()
            order_item.order = current_order
            order_item.product = Product.objects.get(pk = request.POST['product_id'])
            order_item.count = request.POST['count']
            order_item.price = request.POST['price']
            order_item.total = int(request.POST['count']) * int(request.POST['price'])
            current_order.total = order_item.total
            current_order.save()
            item = order_item.save()
            return self.form_valid(order_form)
        else :
            print("form is invalid")
            return self.form_invalid(order_form)



class OrderListView(ListView):
    template_name = 'shop/order_list.html'
    model = Order

    def get_queryset(self):  # 컨텍스트 오버라이딩
        query =  Order.objects.filter(user=self.request.user)
        print(query)
        return query


class OrderDetailView(DetailView):
    template_name = 'shop/order_detail.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = OrderItem.objects.filter(order=context['object'])
        print(context)

        return context

#------------------ORDER END--------------------#

def idCheck(request):
    username = request.POST.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def findPW(request):
    if request.method == 'POST':
        send_email(request)
        return redirect('login')
        #id는 유효한지
    else :
        return render(request, 'registration/findPW.html',{} )


def send_email(request):
    connection = mail.get_connection()  # Use default email connection
    connection.send_messages(messages)

    subject = "THIS MAIL IS FOR TEST"
    message = "this is test mail"
    from_email = "test@test.com"##정용이 메일로 바꾸기
    to_email = "starymate@gmail.com"
    if subject and message and from_email:
        try:
            connection.send_mail(subject, message, from_email, [to_email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')