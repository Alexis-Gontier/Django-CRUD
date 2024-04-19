from django.shortcuts import render, redirect
from .models import Member

def index(request):

    members = Member.objects.all()

    return render(request, "crud/index.html", {
        'members': members
    })

def add(request):
    return render(request, "crud/add.html", {})

def addrec(request):
    x = request.POST['firstname']
    y = request.POST['lastname']
    z = request.POST['email']
    members = Member(firstname = x, lastname = y, email = z)
    members.save()
    return redirect('/')

def delete(request,id):
    members = Member.objects.get(id = id)
    members.delete()
    return redirect("/")

def update(request,id):

    members = Member.objects.get(id = id)

    return render(request,'crud/update.html',{
        'members': members
    })

def uprec(request,id):
    x = request.POST['firstname']
    y = request.POST['lastname']
    z = request.POST['email']
    members=Member.objects.get(id = id)
    members.firstname = x
    members.lastname = y
    members.email = z
    members.save()
    return redirect("/")