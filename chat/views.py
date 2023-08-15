
from django.contrib import messages

from django.shortcuts import render, redirect

from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def chatpage(request, *args, **kwargs):

	if not request.user.is_authenticated:
		return redirect("signin")
	context = {}
	return render(request, "chat/chatpage.html", context)




def signin(request):

    if request.method=='POST':
          username = request.POST['username']
          pass1 = request.POST['pass1']

          user = authenticate( username= username, password = pass1 )

          if user is not None:
              login( request, user)
              fname = user.first_name

              #return render(request, "blog/home.html", {"fname": fname})
              #messages.success(request, "Logged In Sucessfully!!")
              return redirect('chatpage')
          else:
              messages.error(request, "bad credentials")
              return redirect('signin')

    return render(request, "chat/signin.html")


def signout(request):
    logout(request)

    return redirect('chatpage')
    messages.success(request, "Logged Out Successfully!!")

def signup(request):
    if request.method=='POST':
         fname = request.POST['fname']
         lname = request.POST['lname']
         email = request.POST['email']
         username = request.POST['username']
         pass1 = request.POST['pass1']
         pass2 = request.POST['pass2']

         myuser = User.objects.create_user(first_name=fname, last_name=lname, email=email, username=username, password=pass1)
         myuser.save()
         messages.success(request, " Your account is created .")
         return redirect('signin')

    return render(request, "chat/signup.html")

