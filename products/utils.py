from .models import Products,Tag
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage



def SearchProduct(request):
    search_query=''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')

    tags=Tag.objects.filter(name__icontains=search_query)

    products=Products.objects.filter(                                       
    Q(title__icontains=search_query) |
    Q(description__icontains=search_query) |
    Q(owner__name__icontains=search_query) |
    Q(tags__in=tags))
    return products,search_query


def paginateproducts(request,products,results):
    page=request.GET.get('page')
    
    paginator=Paginator(products,results)

    try:
     products=paginator.page(page)
    except PageNotAnInteger:
        page=1
        products=paginator.page(page)
    except EmptyPage:
        page= paginator.num_pages
        products=paginator.page(page)

    leftindex=(int(page) - 4)
    if leftindex < 1 :
        leftindex=1
    
    rightindex= (int(page) + 5)
    if rightindex > paginator.num_pages:
        rightindex=paginator.num_pages + 1

    

    custom_range=range(leftindex,rightindex)
    return custom_range,products