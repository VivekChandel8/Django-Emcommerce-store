from django.shortcuts import render,HttpResponse,redirect
from .models import MySiteProduct,Cart,MySiteUser
# Create your views here.
def  homepage(request):
    cartquan = []
    qnty = Cart.objects.all()
    for t in qnty:
        cartquan.append((Cart.objects.filter(pid=t.pid)[0].quan))
    c = sum(cartquan)
    request.session["cartquan"] = c
    


    prolist = MySiteProduct.objects.all()

    return render(request,"index.html",{'path':'http://localhost:8000/static/','obj':prolist})



def addtocart(request):

     uidf = request.GET.get("uid")
     pidf = request.GET.get("pid")

     query=Cart.objects.filter(pid=pidf)

     if(len(query) == 0):
         obj = Cart(uid=uidf,pid=pidf)
         obj.save()

     else :

         count=int(query[0].quan)+1
         Cart.objects.filter(pid=pidf).update(quan=count)


     return redirect("http://localhost:8000/cartpage/")


def  removefromcart(request):
    pidfg = request.POST.get("pid")
    Cart.objects.filter(pid=pidfg).delete()
    return redirect("http://localhost:8000/cartpage/")



def cartpage(request):

    obj = Cart.objects.all()
    items=[]
    quantlist=[]
    cartquan = []
    qnty = Cart.objects.all()
    for t in qnty:
        cartquan.append((Cart.objects.filter(pid=t.pid)[0].quan))
    c = sum(cartquan)
    request.session["cartquan"] = c

    for m in obj:
      items.append(MySiteProduct.objects.filter(pid=m.pid)[0])
      quantlist.append(Cart.objects.filter(pid=m.pid)[0].quan)
    i=[]
    p=[]
    f=[]
    for k in obj:
        i.append(MySiteProduct.objects.filter(pid=k.pid)[0].proprice)
        p.append(Cart.objects.filter(pid=k.pid)[0].quan)
    for m,z in zip(i,p):
        a = (int(m)*int(z))
        f.append(a)
    Total = sum(f)
    return render(request,"cart.html",{'path':'http://localhost:8000/static/','obj':zip(items,quantlist),'objt':Total})

def  updateQuantity(request):

    pidf = request.POST.get("pid")
    quant=request.POST.get("quanty")

    Cart.objects.filter(pid=pidf).update(quan=quant)
    return redirect("http://localhost:8000/cartpage/")

def sign(request):
    nam = request.POST.get("name")
    pwrd = request.POST.get("password")
    eml = request.POST.get("email")
    obj = MySiteUser(uname=nam,upass=pwrd,uemail=eml)
    obj.save()
    return redirect("http://localhost:8000/login/")
def log(request):
    uname = request.POST.get("uname")
    psd = request.POST.get("password")
    check =MySiteUser.objects.filter(uname=uname,upass=psd)

    if(len(check)==0):
        return redirect("http://localhost:8000/error/")

    else:
        request.session["uid"] = uname
        return redirect("http://localhost:8000/shop/")

def error(request):
    return render(request,"error.html", {'path': 'http://localhost:8000/static/'})
def signup(request):
    return render(request, "Signup.html", {'path': 'http://localhost:8000/static/'})
def login(request):
    return render(request, "Login.html", {'path': 'http://localhost:8000/static/'})
def about(request):
    return render(request,"about.html", {'path':'http://localhost:8000/static/'})
def contact(request):
    return render(request,"contact.html",{'path':'http://localhost:8000/static/'})
def product(request):
    ojjp = MySiteProduct.objects.all()
    return render(request,"product.html",{'path':'http://localhost:8000/static/','cat':ojjp})
def productdetail(request):
    return render(request,"product-detail.html",{'path':'http://localhost:8000/static/'})
def blogdetail(request):
    return render(request,"blog-detail.html",{'path':'http://localhost:8000/static/'})
def blog(request):
    return render(request,"blog.html",{'path':'http://localhost:8000/static/'})
def logout(request):
    del(request.session["uid"])
    return redirect("http://localhost:8000/login")