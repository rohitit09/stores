from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager,PermissionsMixin,AbstractBaseUser

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self,phone,password=None,**kwargs):
        if not phone:
            raise ValueError('user must have phone number')
        usr=self.model(phone=phone,**kwargs)
        usr.set_password(password)
        usr.save()
        return usr

    def create_superuser(self,phone,password):
        user=self.model(phone=phone)
        user.set_password(password)
        user.is_staff=True
        user.is_superuser=True
        user.save()
        return user

class User(AbstractBaseUser,PermissionsMixin):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, unique=True)   # validators should be a list
    name=models.CharField(max_length=255)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD ='phone'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        
        return self.phone


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'


class Seller(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name='Sellar'
        verbose_name_plural='Sellers'


class Store(models.Model):
    name=models.CharField(max_length=255)
    address=models.TextField()
    owner = models.ManyToManyField(Seller,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Store'
        verbose_name_plural='Stores'

    def get_absolute_url(self):
        return f"/view_store/{self.id}/"


class Products(models.Model):
    product_name=models.CharField(max_length=255)
    description=models.TextField()
    mrp=models.DecimalField(max_digits=20,decimal_places=2)
    sale_price=models.DecimalField(max_digits=20,decimal_places=2)
    category= models.CharField(max_length=255)
    store = models.ManyToManyField(Store,blank=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'



class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()

    def __str__(self):
        return self.user.phone

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
    buyer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name='Order'
        verbose_name_plural='Orders'
