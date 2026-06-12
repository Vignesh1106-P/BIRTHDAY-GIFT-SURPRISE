from django.shortcuts import render, redirect

def login_page(request):
    error = ""

    if request.method == "POST":
        password = request.POST.get("password")

        if password == "28062007":
            request.session["birthday_login"] = True
            return redirect('/loading/')
        else:
            error = "Wrong Password da 😄"

    return render(request, "login.html", {"error": error})


def home(request):
    if not request.session.get("birthday_login"):
        return redirect("login")

    return render(request, "home.html")


def surprise(request):
    if not request.session.get("birthday_login"):
        return redirect("login")

    return render(request, "surprise.html")

def game(request):
    return render(request,'game.html')

def countdown(request):
    return render(request,'countdown.html')

def letter(request):
    return render(request,'letter.html')

def logout_page(request):
    request.session.flush()
    return redirect('login')

def loading(request):
    return render(request,'loading.html')

def slideshow(request):
    if not request.session.get("birthday_login"):
        return redirect("login")
    
    return render(request, 'slideshow.html')