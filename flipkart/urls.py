"""flipkart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website.views import logout,error,log,sign,login,signup,updateQuantity,homepage,addtocart,removefromcart,cartpage,about,contact,product,blog,\
    productdetail,blogdetail,removefromcart
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    path('addtocart/',addtocart),
    path('removefromcart/',removefromcart),
    path('cartpage/',cartpage),
    path('about/',about),
    path('contact/',contact),
    path('shop/',product),
    path('product-detail/',productdetail),
    path('blog-detail/',blogdetail),
    path('blog/',blog),
    path('removefromcart/',removefromcart),
    path('updatequantity/',updateQuantity),
    path('signup/',signup),
    path('login/',login),
    path('sign/',sign),
    path('log/',log),
    path('error/',error),
    path('logout/',logout)
]

