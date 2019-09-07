from django.db import models

# Create your models here.


class MySiteUser(models.Model):
    uid=models.AutoField(primary_key=True)
    uname=models.CharField(max_length=200)
    upass=models.CharField(max_length=300)
    uemail=models.EmailField(default='')

    def __str__(self):
        return self.uname


    class Meta:
        db_table="users"



class MySiteProduct (models.Model):
    pid =models.AutoField(primary_key=True)
    proname=models.TextField()
    prodes=models.TextField()
    proimg=models.CharField(max_length=300)
    proprice=models.CharField(max_length=300)

    def __str__(self):
        return self.proname

    class Meta:
        db_table="products"


class Cart(models.Model):
    uid=models.CharField(max_length=2000)
    pid=models.CharField(max_length=3005)
    quan=models.IntegerField(default=1)

    def __str__(self):
        return self.pid
    class Meta:
        db_table = "cart"

