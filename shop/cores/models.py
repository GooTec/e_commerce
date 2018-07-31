from django.db import models
from django.contrib.auth.models import User

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

class ProductImgs(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="Products/subImg")

#---------------- PRODUCT END --------------------#


#---------------- USER RELATED START --------------------#
class Profile(models.Model):
    user_id =  models.OneToOneField(User , primary_key=True, on_delete=models.CASCADE)
    phone = models.TextField(max_length=10)
    ### 주소 검색 : http://www.juso.go.kr/CommonPageLink.do?link=/addrlink/jusoSearchSolutionIntroduce
    address = models.CharField(max_length=40 , default=None)
    address_detail = models.CharField(max_length=40, default=None)
    fullname = models.TextField(max_length=20)

class Cart(models.Model):
    user_id =  models.OneToOneField(User , primary_key=True, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.IntegerField()

#---------------- USER RELATED END --------------------#


#-----------------