from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import EventSerializer,RegisterSerializer
from .models import Event
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
def welcome(request):
    return Response("welcome to events apis...")

@api_view(['POST'])
def addEvent(request):

    ser = EventSerializer(data = request.data)

    if (ser.is_valid()):
        ser.save()

        return Response(ser.data)

    return Response(ser.erroes)

@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all()
    serData = EventSerializer(events,many=True)
    return Response (serData.data)    

@api_view(['GET'])
def getEventByID(request,id):
    try:
        event=Event.objects.get(id=id)
        serData = EventSerializer(event)

        return Response({
            "data":serData.data,
            "message":"Event fetch successfully"
        })

    except  Event.DoesNotExist:  
        return Response({
            "data":[],
            "message":"Event not found"
        })    

@api_view(['PUT'])
def updateEvent(request,id):
    try:
        event=Event.objects.get(id=id)
        

    except  Event.DoesNotExist:  
        return Response({
            "data":[],
            "message":"Event not found"
        })  
    serData = EventSerializer(event, data=request.data, partial=True)

    if(serData.is_valid()):
        serData.save()

        return Response({
            "message":"Event updated successfully",
            "event":serData.data
        })   
    return Response({
        "message":"Event not updated",
        "errors":serData.errors
    }) 

@api_view(['DELETE'])
def deleteEvent(request,id):
    try:
        event=Event.objects.get(id=id)
        

    except  Event.DoesNotExist:  
        return Response({
            "message":"Event not found"
        }) 
    event.delete()     
    return Response({
            "message":"Event deleted successfully"
        })      
@api_view(['GET'])
def getEventByPaginate(request):
    page = int(request.GET.get('page',1))
    per_page = int(request.GET.get('per_page',5))

    events = Event.objects.all()

    paginater =Paginator (events,per_page)
    page_obj = Paginator.get_page(page)

    serData = EventSerializer(pagr_obj.object_list, many=True)


    return Response({
        "Events":serData.data,
        "pagination":{
            "current_page":page_obj.number,
            "per_page":per_page,
            "total":paginater.count,
            "last_page":paginater.num_pages,
            "has_next_page":page_obj.has_next(),
            "has_previous_page":page_obj.has_previous()
        }    
    })

@api_view(['POST'])
def register(request):

    serData = RegisterSerializer(data = request.data)
    
    if(serData.is_valid()):
        serData.save()

        return Response({
            "message":"Register Successfully",
            "user":serData.data
        })
    return Response(serData.errors) 

@api_view(['POST'])
def login(request):

    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(
        username=username,
        password=password

    )

    if user:

        token, created = Token.objects.get_or_create(user=user)
        return Response({
        "token":token.key,
        "username":user.username
        })
    return Response({
    "message":"Invalid cred"
    }) 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response({
        "id":request.user.id,
        "username":request.user.username,
        "email":request.user.email
    })
