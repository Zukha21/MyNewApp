from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import (get_object_or_404,
                              render,
							  HttpResponseRedirect)
# Create your views here.
def index(request):
    return render(request, 'index.html')
   

# relative import of forms
from .models import GeeksModel
from .forms import GeeksForm


def create_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = GeeksForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/')

	context['form']= form
	return render(request, "index.html", context)

    
# relative import of forms
from .models import GeeksModel

def update_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, pk = pk)
 
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+pk)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)

 
 
def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()
         
    return render(request, "list_view.html", context)
from django.shortcuts import render

# relative import of forms
from .models import GeeksModel


def delete_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, pk = pk)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)