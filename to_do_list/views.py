from django.shortcuts import render , HttpResponse ,redirect

from .models import Data 
# Create your views here.

def index(request):
    all_data = Data.objects.all()
    if request.method == "POST":
        contents = request.POST['content_data']
        data = Data(content=contents)
        data.save()
        return redirect('/')
    context = {
            'all_data' : all_data,
        }
 
    return render(request , 'index.html',context)

def delete(request,pk):
    content = Data.objects.get(id=pk)
    content.delete()
    return redirect('/')


def edit(request,ak):
    content_edit = Data.objects.get(id=ak)
    if request.method == "POST" :
        content_data = request.POST.get('edited')
        content_edit.content = content_data
        content_edit.save()
        return  redirect('/')
    return render(request,'edit.html',{'content':content_edit})