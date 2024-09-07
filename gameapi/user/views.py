from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import (UserDetailedSerializer, UserListSerializer)


@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    if users:
        serializer = UserListSerializer(
            instance=users, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'message': "No user data available!"},
                    status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_user(request):
    serializer = UserDetailedSerializer(
        data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserDetailedSerializer(
            instance=user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = UserDetailedSerializer(
            instance=user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
