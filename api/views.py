from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializers import ProductSerializer
from products.models import Products,Review


@api_view(['GET'])
def getRoutes(request):

    routes=[
        {'GET':'api/products'},
        {'GET':'api/products/id'},
        {'POST':'api/products/id/vote'},
        {'POST':'api/users/token'},
        {'POST':'api/users/token/refresh'},
    ]
 
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    print('USERS:',request.user)
    products=Products.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(reqeust,pk):
    products=Products.objects.get(id=pk)
    serializer=ProductSerializer(products,many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def productVote(request,pk):
    products=Products.objects.get(id=pk)
    user=request.user.profile
    data=request.data
    
    review,created=Review.objects.get_or_create(
        owner=user,
        product=products,)
    review.value=data["value"]
    review.save()
    products.getVoteCount


    serializer=ProductSerializer(products,many=False)
    return Response(serializer.data)