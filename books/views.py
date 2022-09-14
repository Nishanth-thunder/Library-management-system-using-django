from django.shortcuts import render
from .models import book,user

# Create your views here.
def home(request):
    return render(request,'books/index.html')
def stu(request):
    return render(request, 'books/student.html')
def ad(request):
    return render(request, 'books/ad.html')
def show(request):
    a=book.objects.all()
    context={
        'book_list':a
    }
    return render(request,'books/ss.html',context)
def log(request):
    e=request.POST.get("email")
    r=request.POST.get("pwd")
    for i in user.objects.all():
        if(i.email==e and i.password==r):
            return render(request, 'books/suc.html')
    return render(request,'books/fail.html')
def de(request):
    s=int(request.POST.get("id"))
    r=int(s)
    for i in book.objects.all():
        if(int(i.book_id)==r):
            t=book.objects.get(book_id=r)
            print(t)
            t.delete()
            return render(request, 'books/complete.html')
    return render(request, 'books/inc.html')
def ins(request):
    a=int(request.POST.get("id"))
    b=request.POST.get("bname")
    c=request.POST.get("bauthor")
    d=request.POST.get("btype")
    for i in book.objects.all():
        if(int(i.book_id)==a):

            return render(request, 'books/inc.html')
    l = book(book_id=a, book_name=b, book_author=c, book_type=d)
    l.save()
    return render(request, 'books/complete.html')
def upt(request):
    e = int(request.POST.get("id"))
    f = request.POST.get("bname")
    g = request.POST.get("bauthor")
    h = request.POST.get("btype")
    for i in book.objects.all():
        if (int(i.book_id) == e):
            q=book.objects.get(book_id=e)
            q.book_name=f
            q.book_author=g
            q.book_type=h
            q.save()
            return render(request, 'books/complete.html')
    return render(request, 'books/inc.html')
def reg(request):
    return render(request, 'books/register.html')
def s(request):
    q=request.POST.get("name")
    p=request.POST.get("email")
    u=request.POST.get("pwd")
    for i in user.objects.all():
        if (i.email == p ):
            return render(request, 'books/fail.html')
    s=user(name=q,email=p,password=u)
    s.save()
    return render(request, 'books/complete.html')


