from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
import random
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

from .models import RestaurantLocation
from .forms import RestaurantCreateForm,RestaurantLocationCreateForm

def restaurant_createview(request):
	form = RestaurantLocationCreateForm(request.POST or None)
	errors = None
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/restaurants/")
	if form.errors:
		errors = form.errors

	template_name = 'restaurants/form.html'
	context = {"form" : form , "errors" : errors}
	return render(request,template_name,context)



def resturant_list_view(request):
	template_name = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context = {
		"object_list" : querysets 
	}
	return render(request, template_name, context)

def resturant_detail_view(request,slug):
	template_name = 'restaurants/restaurantlocation_detail.html'
	obj = get_object_or_404(RestaurantLocation, slug=slug)
	context = {
		"object" : obj 
	}
	return render(request, template_name, context)


class RestaurantListView(ListView):
	template_name = 'restaurants/restaurantlocation_list.html'


	def get_queryset(self):
		print(self.kwargs)
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.all().filter(

				Q(category__iexact=slug) |
				Q(category__icontains=slug)

				)
		else: 
			queryset = RestaurantLocation.objects.all()
		return queryset 


class RestaurantDetailView(DetailView):
	 queryset = RestaurantLocation.objects.all() 

class RestaurantCreateView(CreateView):
	form_class = RestaurantLocationCreateForm
	template_name = 'restaurants/form.html'
	success_url = '/restaurants/'

	# def get_context_data(self,*args,**kwargs):
	# 	print(self.kwargs)
	# 	context = super(RestaurantDetailView,self).get_context_data(*args,**kwargs)
	# 	print(context)
	# 	return context

	# def get_object(self, *args, **kwargs):
	# 	slug = self.kwargs.get('slug')
	# 	print(self.kwargs)
	# 	obj = get_object_or_404(RestaurantLocation, id=slug) # pk = rest_id
	# 	return obj

# class SearchRestaurantListView(ListView):
	
# 	template_name = 'restaurants/restaurants_list.html'

# 	def get_queryset(self):
# 		print(self.kwargs)
# 		slug = self.kwargs.get("slug")
# 		if slug:
# 			queryset = RestaurantLocation.objects.all().filter(

# 				Q(category__iexact=slug) |
# 				Q(category__icontains=slug)

# 				)
# 		else:
# 			queryset = RestaurantLocation.objects.all()
# 		return queryset 


# class HyderabadiRestaurantListView(ListView):
# 	queryset = RestaurantLocation.objects.all().filter(category__iexact='hyderabadi')
# 	template_name = 'restaurants/restaurants_list.html'


# function based view
# def home(request):
# 	a = None
# 	some_list = [random.randint(0,1000), random.randint(0,1000),random.randint(0,1000),random.randint(0,1000) ]
# 	condition_bool = True
# 	if condition_bool :
# 		a = random.randint(1,9999)
# 	context = { 
# 		"num" : a , 
# 		"bool_item" : True,
# 		"some_list" : some_list}
# 	return render(request,'home.html',context)

# class HomeView(TemplateView):
# 	template_name = 'home.html'

# 	def get_context_data(self,*args, **kwargs):
# 		context = super(HomeView,self).get_context_data(*args,**kwargs)
# 		a = None
# 		some_list = [random.randint(0,1000), random.randint(0,1000),random.randint(0,1000),random.randint(0,1000) ]
# 		condition_bool = True
# 		if condition_bool :
# 			a = random.randint(1,9999)
# 		context = { 
# 			"num" : a , 
# 			"bool_item" : True,
# 			"some_list" : some_list}
# 		return context



# def about(request):
# 	context = { 
# 				}
# 	return render(request,'about.html',context)

# class AboutView(TemplateView):
# 	template_name = 'about.html'

# def contact(request):

# 	context = { 
# 		}
# 	return render(request,'contact.html',context)


# class ContactView(View):

#     def get(self, request, *args, **kwargs):
#         return render(request,'contact.html',{})

