from django.shortcuts import render

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from rest_framework.viewsets import ViewSet

from rest_framework import authentication,permissions

from rest_framework.generics import ListAPIView,CreateAPIView

from budget.serializers import UserSerializer,ExpenseSerializer,IncomeSerializer

from budget.models import Expense,Income

from rest_framework.generics import RetrieveAPIView,CreateAPIView

from django.contrib.auth.models import User



class SignUpView(CreateAPIView):

    serializer_class=UserSerializer

    queryset=User.objects.all()

   


class ExpenseViewSetView(ViewSet):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):

        qs=Expense.objects.filter(owner=request.user)

        serializer_instance=ExpenseSerializer(qs,many=True)

        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
    
    def create(self,request,*args,**kwargs):

        serializer_instance=ExpenseSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(owner=request.user)

            return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
   

class ExpenseDetailView(RetrieveAPIView):

    serializer_class=ExpenseSerializer

    queryset=Expense.objects.all()
    
    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]














    


