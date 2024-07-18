from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework import status
from client.models import Client
from .serializers import ClientSerializers, ClientGetSerializers

class ClientAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={200: ClientGetSerializers(many=True)},
    )
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientGetSerializers(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=ClientSerializers,
        responses={201: ClientSerializers},
    )
    def post(self, request):
        serializer = ClientSerializers(data=request.data)
        if serializer.is_valid():
            client = serializer.save()
            client.created_by = request.user
            client.save()
            return Response(
                {"message": "Client successfully added",
                 "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ClientUpdateAPIView(APIView):

    @extend_schema(
        request=ClientSerializers,
        responses={200: ClientSerializers},
    )
    def put(self, request, pk):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response(
                {"error": "Client not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ClientSerializers(client, data=request.data)
        if serializer.is_valid():
            client = serializer.save()
            client.modified_by = request.user
            client.save()
            return Response(
                {"message": "Client successfully updated", 
                 "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @extend_schema(
        request=None,
        responses={200: "Client successfully deleted"},
    )
    def delete(self, request, pk):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response(
                {"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if client.created_by != request.user:
            return Response(
                {"error": "You do not have permission to delete this client"},
                status=status.HTTP_403_FORBIDDEN,
            )

        client.delete()
        return Response(
            {"message": "Client successfully deleted"}, status=status.HTTP_200_OK
        )