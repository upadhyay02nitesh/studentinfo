from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

# This Function Will Add new Item and Show All Items
def add_show(request):
 if request.method == 'POST':
  fm = StudentRegistration(request.POST,request.FILES)
  if fm.is_valid():
   nm = fm.cleaned_data['name']
   hm = fm.cleaned_data['Fathername']
   em = fm.cleaned_data['email']
   pw = fm.cleaned_data['password']
   im = fm.cleaned_data['image']
   reg = User(name=nm,Fathername=hm, email=em, password=pw,image=im)
   reg.save()
   fm = StudentRegistration()
 else:
  fm = StudentRegistration()
 stud = User.objects.all()
 return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

# This Function will Update/Edit
def update_data(request, id):
 if request.method == 'POST':
  pi = User.objects.get(pk=id)
  fm = StudentRegistration(request.POST,request.FILES, instance=pi)
  if fm.is_valid():
   fm.save()
 else:
  pi = User.objects.get(pk=id)
  fm = StudentRegistration(instance=pi)
 return render(request, 'enroll/updatestudent.html', {'form':fm})

# This Function will Delete
def delete_data(request, id):
 if request.method == 'POST':
  pi = User.objects.get(pk=id)
  pi.delete()
  return HttpResponseRedirect('/')