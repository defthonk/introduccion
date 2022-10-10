from multiprocessing import context
#++
from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request, *args, **kwargs): #*args y **kwargs hace referecia a cualquier varibale o parametro, que nuestro request, que el objeto del request pueda tener 
        context = {
            
        }
        return render(request, 'index.html',context)

#+