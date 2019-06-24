
# Restful Imports
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination


# App Level Imports
from .serialiser import BankSerializer
from .models import Branches,Banks


# class BranhesFilter(django_filters.FilterSet):
#     class Meta:
#         model = Branches
#         fields = ['bank','city']
            


class BankView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Branches.objects.all()
    serializer_class = BankSerializer

    @action(methods=['get'], detail=False)
    def findbank(self, request):
        try:
            data = Branches.objects.get(ifsc = request.GET["ifsc"])
            serialiser = self.serializer_class(data)
            return Response(serialiser.data)
        except Branches.DoesNotExist:
            return Response({"status":"ifsc does not exists"},status.HTTP_404_NOT_FOUND)
        except :
            return Response({"status":"Invaid input"},status.HTTP_404_NOT_FOUND)


    @action(methods=['get'], detail=False)
    def banklist(self, request):
        try:
            bank = request.GET.get('bank')
            city = request.GET.get('city')
            bank = Banks.objects.get(name = bank)
            page = self.paginate_queryset(Branches.objects.filter(bank=bank,city=city))
            serialiser = self.serializer_class(page,many=True)
            return self.get_paginated_response(serialiser.data)
        except Banks.DoesNotExist:
            return Response({"status":"Bank Not Exists"},status.HTTP_404_NOT_FOUND)
        except:
            return Response({"status":"not Found"},status.HTTP_404_NOT_FOUND)






