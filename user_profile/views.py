from re import template
from django.shortcuts import render,redirect
from django.contrib import  messages
from django.http import HttpResponse
from django.template import loader
from.forms import RegisterUserForm,UpdateUserForm,UserProfileUpdateForm
from django.contrib.auth.decorators import login_required

def out(request):
    template=loader.get_template('registration/logout.html')
    context={}
    return HttpResponse(template.render(context,request))


def register(request):
    if request.method=='POST':
        
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f'Your Account has been created you are now able to login')
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request,'registration/register.html',{'form':form})


@login_required
def profile(request):
    if request.method=="POST":
        u_form=UpdateUserForm(request.POST,instance=request.user)
        p_form=UserProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('profile')


    else:
        u_form=UpdateUserForm(instance=request.user)
        p_form=UserProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html',context)