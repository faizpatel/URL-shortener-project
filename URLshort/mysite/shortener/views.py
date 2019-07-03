from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import shortURL
from .forms import SubmitURLForm


def homeview(request,*args,**kwargs):
    if request.method=='POST':
        return render(request, 'shortener/home.html',{})
    
class home(View):
    def get(self, request, *args, **kwargs):
        the_form=SubmitURLForm
        context={
            'title':'URL Shortener',
            'form':the_form
            }
        
        return render(request, 'shortener/home.html',{})

    def post(self, request, *args, **kwargs):
        form=SubmitURLForm(request.POST)
        context={
            'title':'URL Shortener',
            'form':form
            }
        template='shortener/home.html'
        if form.is_valid():
            new_url=form.cleaned_data
            obj, created= shortURL.objects.get_or_create(url=new_url)
            context={
                'object':obj,
                'created':created,
                }
        
            template='shortener/link.html' 
        return render(request, template ,context)
        
        
def short_redirect_view(request, shortcode=None, *args, **kwargs):
    try:
       obj=shortURL.objects.get(shortcode=shortcode)
    except:
       obj=shortURL.objects.all().first()

    obj_url = None
    qs = shortURL.objects.filter(shortcode__iexact=shortcode.upper())
    print(qs)
    if qs.exists() and qs.count()==1:
        obj=qs.first()
        obj_url= obj.url      
    if obj_url==None:
         return render(request, 'shortener/error.html')

    else:
        return HttpResponseRedirect(obj_url)

