from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from .models import Customer,Manager
from django.views.generic import( TemplateView,ListView,CreateView,DetailView,DeleteView,UpdateView)
from .forms import CustomerForm
# Create your views here.

class Bill(ListView):
    template_name = 'receipt.html'
    model = Customer

class Receipt(DetailView):
    template_name = 'bill.html'
    model = Customer

class Hotel(TemplateView):
    template_name = 'hotel.html'

class Home(TemplateView):
    template_name = 'home.html'

class Table(ListView):
    model = Customer
    template_name = 'table.html'

def Create(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('hotelapp:customer'))
        else:
            return HttpResponse("<h2>INVALID DATA</h2>")
    else:
        return render(request,'create.html',{'form':form})


class Detail(DetailView):
    model = Customer
    template_name = 'detail.html'

class Update(UpdateView):
    model = Customer
    template_name = 'update.html'
    fields = ['name','age','phoneno']

#def updateconfirm(request):
#    return render(request,'Uconfirm.html')

class Delete(DeleteView):
    model = Customer
    template_name = 'delete.html'
    success_url = reverse_lazy('hotelapp:customer')
