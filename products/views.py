from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Products,Tag
from .forms import ProductForm,ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import SearchProduct,paginateproducts

# Create your views here.

def products(request):  
    products,search_query=SearchProduct(request)
    custom_range,products=paginateproducts(request,products,6)

    context={'products':products,'search_query':search_query,'custom_range':custom_range}
    return render(request,'products/products.html',context)

def product(request,pk):
    product = Products.objects.get(id=pk)
    tags=product.tags.all()
    form=ReviewForm()

    if request.method == 'POST':
        form=ReviewForm(request.POST)
        review=form.save(commit=False)
        review.product=product
        review.owner=request.user.profile
        review.save()

        product.getVoteCount
        messages.success(request,"Your review was succesfully submitted!")
        return redirect('product', pk=product.id) #refresh form !! redirect the user to the same page but the review form will by empty!!

    print('product:',product)
    return render(request,'products/singleproducts.html',{'product':product,'tags':tags,'form':form})

@login_required(login_url='login')
def createproduct(request):
    form=ProductForm()
    profile=request.user.profile

    if request.method =='POST':
        newtags=request.POST.get('newtags').replace(',', " ").split()
        form=ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.owner=profile
            product.save()
            for tag in newtags:
                tag, created=Tag.objects.get_or_create(name=tag)
                product.tags.add(tag)
                
            return redirect('products')
    
    context={'form':form}
    return render(request,'products/product_form.html',context)

@login_required(login_url='login')
def updateproduct(request,pk):
    profile=request.user.profile             
    product=profile.products_set.get(id=pk) 
    form=ProductForm(instance=product)

    if request.method == 'POST':
        newtags=request.POST.get('newtags').replace(',', " ").split()
        
        form=ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            product=form.save()
            for tag in newtags:
                tag, created=Tag.objects.get_or_create(name=tag)
                product.tags.add(tag)


            return redirect('products')
    
    context = {'form': form}
    return render(request,'products/product_form.html',context)

@login_required(login_url='login')
def deleteproduct(request,pk):
    profile=request.user.profile
    product=profile.products_set.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('account')  
    context={'product':product}
    return render(request,'delete_product.html',context)