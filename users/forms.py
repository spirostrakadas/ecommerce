from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Message


class CustomCreationForm(UserCreationForm):
    class  Meta:
        model=User  #user is an already built model from django!(from django.contrib.auth.models import User)
        fields=['first_name','email','username','password1','password2']
        labels={
            "first_name":"Name",
        }



    def __init__(self,*args,**kwargs):
        super(CustomCreationForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=['name','email','username','location','bio',
        'short_intro','profile_image','website'
        ]
        


class MessageForm(ModelForm):
    
    class Meta:
        model = Message
        fields = ["name","email","subject","body"]


    def __init__(self,*args,**kwargs):
        super(MessageForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})