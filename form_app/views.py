from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from .forms import NameForm, NameFormSet
from .models import NameData

# Create your views here.
def index(request):
	formset = NameFormSet()
	if request.method == 'POST':
		print('post')
		formset = NameFormSet(request.POST)
		if formset.is_valid():
		    data = formset.cleaned_data
		    NameData.objects.create(data=data)
		return render(request, 'form_app/show.html', { 'data': data })
	return render(request, 'form_app/index.html', { 'formset': formset })


	
