from django.contrib import admin
from django.urls import path,include
from container.views import *





urlpatterns = [

    path('',include('accounts.urls')),
    path('api/receipe/',checklistapi.as_view()),
    path('api/categories/',categorylist.as_view()),
    path('api/receipedetail/<uuid:uuid_check>',CategoryListDetail.as_view()),






    
    


]