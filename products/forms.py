from django.forms import ModelForm
from .models import Products,Review
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model=Products
        fields=['title','description','demo_link','source_link','featured_image']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }
    

    #gia na kanw modify kathe pedio!
    def __init__(self,*args,**kwargs):
        super(ProductForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})



        #self.fields['title'].widget.attrs.update({'class':'input','placeholder':'add title'})

class ReviewForm(ModelForm):
    class Meta:
        model=Review
        fields=['value','body']

    labels={
        'value':'Place your vote',
        'body':'Add comment'
    }    

    def __init__(self,*args,**kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})