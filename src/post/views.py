from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound

# Create your views here.

#def index(request):
    #print(request)
    #print(request.scheme)
    #print(request.path)
    #print(request.encoding)
   # return HttpResponse('<h1>Hello World!</h1>')

#def index_2(request):
   # return HttpResponse('<h1>Hello World! index_2</h1>')

#def about(request):
    #print('http://127.0.0.1:8000'+request.get_full_path())
   # return HttpResponse('<a href="#"> About page! </a>')

#def contacts(request):
   # print(request.path)
    #return HttpResponse('<h2> Contacts page </h2>')

#def ggg(request):
   # return HttpResponse('<h2> GGG page </h2>')

#def archive(request):
   # return HttpResponse('Archive page')

#def archive_2(request):
   # return HttpResponse('Archive page 2')

#def group(request):
   # group_number = request.path
   # return HttpResponse('group #{group_number}')

#def home_1(request):
   # header = 
   # return HttpResponse(page_content)

def posts(request):
    return HttpResponse('<h1> ALL Posts: </h1>')
def post_detail(request, post_id):
    return HttpResponse(f'detial: {post_id}')

def post_archive(request, year):
    if int(year) > 2024 or int(year) < 1995:
        raise Http404
    return HttpResponse(f'archive for: {year}')

def get_post_handler(request):
    if request.POST:
        return HttpResponse('POST request')
    return HttpResponse('GET request')

def page_404(request, exception):
    return HttpResponseNotFound('<h3>Page not found :^</h3>')

def error_404(request, exception):
   context = {}
   return render(request,'admin/404.html', context)