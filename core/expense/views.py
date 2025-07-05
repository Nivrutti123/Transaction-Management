from django.shortcuts import render
from .models import Transactions
from rest_framework.response import Response
from .serializers import TransactionsSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView

@api_view(["GET","POST"])
def get_transactions(request):
    queryset = Transactions.objects.all()
    serializer = TransactionsSerializer(queryset,many =True)
    return Response({
        "data" : serializer.data
    })


class TransactionAPI(APIView):
    def get(self,request):
        queryset = Transactions.objects.all()
        serializer = TransactionsSerializer(queryset,many =True)
        return Response({
            "data" : serializer.data
        })

    def post(self,request):
        data = request.data
        print(data)
        serializer = TransactionsSerializer(data = data)
        if not serializer.is_valid():
             return Response({
            "message" : "data not saved",
            "error" : serializer.errors
        })
        serializer.save()
        return Response({
            "message" : "This is post",
            "data" : serializer.data
        })

    def put(self,request):
        queryset = Transactions.objects.all()
        serializer = TransactionsSerializer(queryset,many =True)
        return Response({
            "data" : serializer.data
        })

    def patch(self,request):
        data = request.data
        print(data)
        #serializer = TransactionsSerializer(data = data)
        if not data.get('id'):
            return Response({
                "message": "data not update",
                "error": "id is required"
            })

        transactions = Transactions.objects.get(id = data.get('id'))
        serializer = TransactionsSerializer(
            transactions,data = data,partial = True)
        if not serializer.is_valid():
             return Response({
            "message" : "data not saved",
            "error" : serializer.errors
        })
        serializer.save()
        return Response({
            "message" : "This is patch",
            "data" : serializer.data
        })
    
    def delete(self,request):
        data = request.data
        print(data)
        #serializer = TransactionsSerializer(data = data)
        if not data.get('id'):
            return Response({
                "message": "data not update",
                "error": "id is required"
            })
        
        transactions = Transactions.objects.get(id = data.get('id')).delete()       
        return Response({
            "message" : "This is patch",
            "data" :{}
        })
