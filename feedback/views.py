from django.shortcuts import render
from .models import Opinion
from .forms import OpinionModelForm
from django.http import HttpResponse

def f(request):

   if request.method == "POST":
       # save to DB
       form = OpinionModelForm(request.POST)
       if form.is_valid():
           form.save()
           # re-direct to a html (show success information)
           context = {'form': form}
           return render(request, "apply_success.html", context)           
  
   form = OpinionModelForm()

   context = {
       'form': form
   }

   # field the form
   return render(request, "apply.html", context)

