from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import TestDB
from .test_serializers import TestSerializer
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter


# show data
@extend_schema(
        request=TestSerializer,
        responses={200:TestSerializer},
        examples=[],
        description='show all data'
)
@api_view(['GET'])
def test_get_data(request):
    items = TestDB.objects.all()
    serializer = TestSerializer(items, many=True)
    return Response(serializer.data)


@extend_schema(
        request=TestSerializer,
        responses={200:TestSerializer},
        examples=[],
        description='show single data'
)
@api_view(['GET'])
def test_get_single_data(request, pk):
    items = TestDB.objects.get(id=pk)
    serializer = TestSerializer(items, many=False)
    return Response(serializer.data)



# add data
@extend_schema(
        request=TestSerializer,
        responses={200:TestSerializer},
        examples=[
            OpenApiExample(
                'Example',
                value={
                    "name": "YOUR_NAME",
                }
            )
        ],
        description='add data',
        parameters=[
            OpenApiParameter(
                "NAME",
                type=str,
                description='YOUR_NAME'
            )
        ]
)
@api_view(['POST'])
def test_add_data(request):
    serializer = TestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# update data
@extend_schema(
        request=TestSerializer,
        responses={200:TestSerializer},
        examples=[],
        description='update data',
        parameters=[]
)
@api_view(['POST'])
def test_update_data(request,pk):
    item = TestDB.objects.get(id=pk)
    serializer = TestSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# delete data
@extend_schema(
        request=TestSerializer,
        responses={200:TestSerializer},
        examples=[
            OpenApiExample(
                'Example',
                value={
                    "delete_name": "DELETING NAME",
                }
            )
        ],
        description='add data',
        parameters=[
            OpenApiParameter(
                "delete_name",
                type=str,
                description='name you want to delete'
            )
        ]
)
@api_view(['POST'])
def test_delete_data(request):
     data = request.data
     item = TestDB.objects.get(name = data['delete_name'])
     item.delete()
     return Response("record was deleted successfully")

# delete data alt
@extend_schema(
        request=TestSerializer,
        responses={200:TestSerializer},
        examples=[],
        description='delete data alt',
        parameters=[])
@api_view(['DELETE'])
def test_delete_data_alt(request, pk):
     item = TestDB.objects.get(id=pk)
     item.delete()
     return Response("record was deleted successfully")