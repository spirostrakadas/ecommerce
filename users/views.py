from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .models import Profile,Message
from django.contrib.auth.models import User
from .forms import CustomCreationForm,ProfileForm,MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .utils import searchProfiles,paginateprofiles
# Create your views here.

def profiles(request):
    profiles, search_query=searchProfiles(request)
    custom_range,profiles=paginateprofiles(request,profiles,3)

    context={'profiles':profiles,' search_query': search_query,'custom_range':custom_range}
    return render(request,'users/profiles.html',context)



def userProfile(request,pk):
    profile=Profile.objects.get(id=pk)
    context={'profile':profile}
    return render(request,'users/user_profile.html',context)
    
@login_required(login_url='login')
def userAccount(request):
    profile=request.user.profile
    
    products=profile.products_set.all()

    context={'profile':profile,'products':products}
    return render(request, 'users/account.html',context)


def Loginuser(request):
    page='login'
    #if user is already logged in cant see the login page
    #so create this if statement to redirect him to another page!
    if request.user.is_authenticated:
        return redirect('profiles')


    if request.method == "POST":
        username=request.POST['username'].lower()
        password=request.POST['password'].lower()
        #test if the username exists in my database
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'user doesnt exist')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.error(request,'logged in')
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')

        else:
            messages.error(request,'username or password is incorect')

    return render(request,'users/login_register.html')



def Logoutuser(request):    
    logout(request)
    messages.info(request,'user wad logged out')
    
    return redirect('login')


def RegisterUser(request):
    page='register' #page == register gia na anaferthw sto html se auto!
    form =CustomCreationForm()

    if request.method =='POST':
        form=CustomCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()

            messages.success(request,"account was created!")

            login(request,user)
            return redirect('edit_account')
        
        else:
            messages.success(request,"error has occured during registration!")


    context={'page':page,'form':form}
    return render(request,'users/login_register.html',context)


@login_required(login_url="login")
def editaccount(request):
    profile=request.user.profile
    form=ProfileForm(instance=profile)
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context={'form':form}
    return render(request,'users/profile_form.html',context)

@login_required(login_url="login")
def inbox(request):
    profile =request.user.profile
    messagerequest= profile.messages.all()
    unreadcount=messagerequest.filter(is_read=False).count()
    context={'messagerequest':messagerequest,'unreadcount':unreadcount}
    return render(request,'users/inbox.html',context)



@login_required(login_url="login")
def viewMessage(request,pk):
    profile=request.user.profile
    message=profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read=True
        message.save()
    context={'message':message}
    return render(request,'users/message.html',context)

def createMessage(request,pk):
    recipient= Profile.objects.get(id=pk)
    form= MessageForm()

    try:
        sender=request.user.profile
    except:
        sender=None
    
    if request.method =='POST':
        form=MessageForm(request.POST) #request.post in the form to pass the context from the form to proceed to save()
        if form.is_valid():
            message=form.save(commit=False)
            message.sender=sender
            message.recipient=recipient

            if sender:
                message.name=sender.name
                message.email=sender.email
            message.save()

        messages.success(request,"your message was succesfully sent!")
        return redirect('user_profile',pk=recipient.id)        

    context={'recipient':recipient,'form':form}
    return render(request,'users/message_form.html',context)