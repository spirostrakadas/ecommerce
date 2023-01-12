from django.db import models

# Create your models here.
from django.db import models
import uuid
from users.models import Profile
# Create your models here.







class Products(models.Model):
    owner=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE) #connect the product with the owner with the foreign key!
    title=models.CharField(max_length=20)
    description=models.TextField(null=True, blank=True)
    featured_image=models.ImageField(null=True,blank=True,default='default.jpg')
    demo_link=models.CharField(max_length=300,null=True,blank=True)
    source_link=models.CharField(max_length=3000,null=True,blank=True)
    created=models.DateField(auto_now_add=True)
    vote_total=models.IntegerField(default=0,null=True,blank=True)
    vote_ratio=models.IntegerField(default=0,null=True,blank=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True ,primary_key=True,editable=False)
    tags=models.ManyToManyField('Tag',blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-vote_ratio','-vote_total','title']   
        #ordering the sequence by the dated the products have been crated

    @property
    def reviewers(self):
        queryset=self.review_set.all().values_list('owner__id',flat=True)
        return queryset




    @property # @property so in my views i can trigger this function!
    def getVoteCount(self):
        reviews=self.review_set.all()
        upVotes=reviews.filter(value='up').count()
        totalVotes=reviews.count()

        ratio=(upVotes / totalVotes) * 100
        self.vote_total=totalVotes
        self.vote_ratio=ratio

        self.save()

class Review(models.Model):
    owner=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    VOTE_TYPE=(('up','Up Vote'),('down','Down Vote'))
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    body=models.TextField(null=True, blank=True)
    value=models.CharField(max_length=20,choices=VOTE_TYPE)
    id=models.UUIDField(default=uuid.uuid4, unique=True ,primary_key=True,editable=False)

    class Meta:
        unique_together=[['owner','product']]



    def __str__(self):
        return self.value




  

class Tag(models.Model):
    name=models.CharField( max_length=50)
    created=models.DateField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True ,primary_key=True,editable=False)

    def __str__(self):
        return self.name



