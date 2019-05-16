from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Bookinfo,Heroinfo
# Create your views here.

def index(request):
    # return HttpResponse('首页')
    # 获取模板--参数制定了模板位置为demo2文件夹下面的index.html
    temp=loader.get_template('demo2/index.html')
    # 渲染数据--参数是要发送给模板的数据此处用了{}表示不传数据
    result=temp.render({})
    # 返回
    return HttpResponse(result)

def list(request):

    # if request.method=='GET':
    # 获取模板--参数制定了模板位置为demo2文件夹下面的index.html
    temp = loader.get_template('demo2/list.html')
    # 渲染数据--参数是要发送给模板的数据此处用了{}表示不传数据
    books=Bookinfo.objects.all()    #此处获得bookinfo表中的所有数据 并且保存给books
    result = temp.render({'books':books})   #将数据渲染模板
    # 返回
    return HttpResponse(result)
    # elif request.method=='POST':
    #     book=request.POST['bookname']
    #     b1=Bookinfo()
    #     b1.title=book
    #     b1.save()
    #     return HttpResponseRedirect('/demo2/list/')

def hero(request,bookid):
    # 获取模板--参数制定了模板位置为demo2文件夹下面的index.html
    temp = loader.get_template('demo2/hero.html')
    # 渲染数据--参数是要发送给模板的数据此处用了{}表示不传数据
    book=Bookinfo.objects.get(id=bookid)  #这里从bookinfo表中查询一本书  根据bookid来查询
    result = temp.render({'book':book})
    # 返回
    return HttpResponse(result)

def deletebook(request,id):
    Bookinfo.objects.get(pk=id).delete()
    # return HttpResponse('成功')
    return HttpResponseRedirect('/demo2/list/')

def addbook(request):
    if request.method == 'GET':
        return render(request,'demo2/addbook.html')
    elif request.method=='POST':
        book=request.POST['bookname']
        b1=Bookinfo()
        b1.title=book
        b1.save()
        return HttpResponseRedirect('/demo2/list/')

def deletehero(request,id):
    # return HttpResponse('成功')
    hero=Heroinfo.objects.get(pk=id)

    a=hero.book.id
    hero.delete()
    return HttpResponseRedirect('/demo2/hero/%s/'%(a,))


def addhero(request,bookid):
    if request.method=='GET':
        return render(request,'demo2/addhero.html',{'bookid':bookid})
    elif request.method=='POST':
        obj=Bookinfo.objects.get(pk=bookid)
        h1=Heroinfo()
        h1.name=request.POST['username']
        h1.age=request.POST['age']
        h1.skill=request.POST['skill']
        h1.book=obj
        h1.save()
        return HttpResponseRedirect('/demo2/hero/%s/'%(bookid,))

