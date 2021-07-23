from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm
from .models import User


def addInfo(request):
    if request.method == 'POST':
        fm=UserForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            db=User(name=nm, email=em, password=pw)
            db.save()
            # fm=UserForm()
            return HttpResponseRedirect('/')   
    else:
        fm=UserForm()
        db=User.objects.all()
    return render(request, 'stDetails/addInfo.html', {'form':fm,'dbData':db})



def update_data(request,id):
    if request.method == 'POST':
        pi= User.objects.get(pk=id)
        fm=UserForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save() #saving_form_data_into_db
    else:
        pi= User.objects.get(pk=id)
        fm=UserForm(instance=pi)
    return render(request, 'stDetails/updateInfo.html',{'form':fm})


# delete method 
def delete_data(request,id):
    if request.method == 'POST':
        pi= User.objects.get(pk=id)
        pi.delete() #it will delete that primary key data
    return HttpResponseRedirect('/') #after delete it will redirect to homepage

