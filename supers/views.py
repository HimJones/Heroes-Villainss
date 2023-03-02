from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import Super

# Create your views here.

@api_view(['GET'])
def supers_list(request):
    if request.method == 'GET':
        
        super_name = request.query_params.get(super)
        print(super_name)
        
        supers = Super.objects.all()

        if super_name:
            supers = supers.filter(super__name=super_name)
        serializer = SuperSerializer(supers, many= True)
        return Response(serializer.data)
    
@api_view(['GET'])
def super_detail(request, pk):
    super = get_object_or_404 (Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
