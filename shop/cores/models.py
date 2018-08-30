from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


#---------------- PRODUCT START --------------------#
class Product(models.Model):
    CATEGORY = (
        ('Gu', '거문고'),
        ('Hae', '해금'),
        ('Ah', '아쟁'),
        ('Ga', '가야금'),
        ('Dae', '대금'),
        ('etc', '소품'),
    )
    product_id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    content = models.TextField()
    name = models.CharField(max_length=20, default="거문고")
    category = models.CharField(choices=CATEGORY, max_length=10, default='Gu')
    recommend = models.BooleanField(default=False)
    main_img = models.ImageField(upload_to="Products/mainImg")

    def __str__(self):
        return  self.name

    def count_of_category(self):
        categories = {'Gu':0, 'Hae':0, 'Ah':0, 'Ga':0, 'Dae':0 , 'etc':0}

        for key in categories :
            categories[key] = self.objects.filter(category=key).count()
        return categories

    def count_of_best(self):
        return self.objects.filter(recommend=True).count()


class ProductImgs(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="Products/subImg")

#---------------- PRODUCT END --------------------#


#---------------- USER RELATED START --------------------#
class Profile(models.Model):
    user_id =  models.OneToOneField(User , primary_key=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    ### 주소 검색 : http://www.juso.go.kr/CommonPageLink.do?link=/addrlink/jusoSearchSolutionIntroduce
    address = models.CharField(max_length=40 , default=None)
    address_detail = models.CharField(max_length=40, default=None)
    fullname = models.CharField(max_length=20)
    def __str__(self):
        return  self.fullname

        
class Cart(models.Model):
    user_id =  models.OneToOneField(User , primary_key=True, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.IntegerField()

#---------------- USER RELATED END --------------------#



class Order(models.Model):
    STATUS = (
        ('0', '결제 대기'),
        ('1', '결제 완료'),
        ('2', '준비 중'),
        ('3', '배송 중'),
        ('4', '배송 완료'),
        ('5', '구매 완료'),
    )
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    ### 주소 검색 : http://www.juso.go.kr/CommonPageLink.do?link=/addrlink/jusoSearchSolutionIntroduce
    address = models.CharField(max_length=40, default=None)
    address_detail = models.CharField(max_length=40, default=None)
    fullname = models.CharField(max_length=20)
    total = models.IntegerField()
    status = models.CharField(choices=STATUS, max_length=20, default=0)
    order_date = models.DateTimeField(default=datetime.now, blank=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField()

