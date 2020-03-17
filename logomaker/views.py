from django.shortcuts import render,HttpResponse
from .models import category,product,logo
# Create your views here.


def index(request):
    
    if request.method=="POST":
        logoname=request.POST['logoname']
        cat=request.POST['cat']
        company=request.POST['companyname']
        price=request.POST['price']
        data=product(logoname=logoname,category=category.objects.get(cid=cat),price=price,companyname=company)
        data.save()
        # logoall= logo.objects.all()
        mydata=logo.objects.filter(category_id=cat)
        # return render(request,'listing-grid.html',{'category':cat})
        return render(request,'listing-grid.html',{'cat':mydata})
        

    data=category.objects.all()
    return render(request,'index-2.html',{'data':data})
      
    

def listing(request):
    return render(request,'listing-grid.html')

def listingdetails(request):
    
    return render(request,'listing-detail.html')

