from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Profile, CartItem, Order, OrderItem

class CreateUserForm(UserCreationForm): # 내장 회원가입 폼을 상속받아서 확장한다.
    email = forms.EmailField(required=True) # 이메일 필드 추가

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True): # 저장하는 부분 오버라이딩
        user = super(CreateUserForm, self).save(commit=False) # 본인의 부모를 호출해서 저장하겠다.
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProfileCreateForm(forms.ModelForm): # 내장 회원가입 폼을 상속받아서 확장한다.
    class Meta:
        model = Profile
        fields = ( "fullname", "phone","address", "address_detail")


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ("count", )
        # count = forms.IntegerField(initial=1)

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("phone", "address", "address_detail", "fullname")

class OrderItemCreateForm(forms.ModelForm):
    class Meta :
        model = OrderItem
        fields = ("count" , )
