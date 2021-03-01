from django.db import models
from apps.user.models import StoreUser

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

class Products(models.Model):
    product_name=models.CharField(max_length=255)
    description=models.TextField()
    mrp=models.DecimalField(max_digits=20,decimal_places=2)
    sale_price=models.DecimalField(max_digits=20,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'

class Store(models.Model):
    name=models.CharField(max_length=255)
    address=models.TextField()
    products = models.ManyToManyField(Products,blank=True)
    # store_link=models.CharField(max_length=400,primary_key=True,unique=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Store'
        verbose_name_plural='Stores'

    def get_absolute_url(self):
        return f"/view_store/{self.id}/"




class Customer(models.Model):
    user=models.OneToOneField(StoreUser,on_delete=models.CASCADE)
    address=models.TextField()
    store = models.ManyToManyField(Store,blank=True)

    def __str__(self):
        return self.user.phone_number

    class Meta:
        verbose_name='Customer'
        verbose_name_plural='Customers'

class Orders(models.Model):
    choices=(
        ('PENDING','PENDING'),
        ('APPROVED','APPROVED'),
        ('CANCELED','CANCELED')
    )
    

    status=models.CharField(choices=choices,default='PENDING',max_length=8)
    order_created=models.DateTimeField(auto_now_add=True)
    amount=models.DecimalField(max_digits=20,decimal_places=2)
    quatity=models.IntegerField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name='Order'
        verbose_name_plural='Orders'