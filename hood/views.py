from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreateProfileForm
from .models import MyUser,Neighborhood,Post,Business

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    test = "Working!!"
    current_user = request.user
    profile = MyUser.get_user()
    post = Post.get_post()
    return render(request,'index.html',{"test":test,
                                        "current_user":current_user,
                                        "profile":profile,
                                        "post":post})

@login_required(login_url='/accounts/login/')
def create_profile(request):
    test = "Working!!"
    current_user = request.user
    if request.method == 'POST':
        form = CreateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = current_user
            new.save()
            return redirect(index)
    else:
        form = CreateProfileForm()
    return render(request,'profile/create.html',{"test":test,"upload_form":form})