from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm

def home_page(request):
    # if not request.user.is_authenticated():
    #     return redirect(login_page)
    print(request.session.get('user', 'unknown'))
    context = {
        "title":"Hello World!",
        "content": "Welcome to ecomm world the place of the beast!",
        
    }
    if  request.user.is_authenticated():
        context["premium_content"] = "Yuhuuuu"
    return render(request, "home_page.html", context)
def about_page(request):
    context = {
        "title":"What About!?",
        "content": "tell me more about the pages!"
    }
    return render(request, "home_page.html", context)
def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Who are YOu!!?",
        "content": "We can be a friend if just we still communicate!",
        "form" : contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission!"})
    if contact_form.errors:
        print(contact_form.cleaned_data)
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')           
    #if request.method == "POST":
    #    #print(request.POST)
    #    print(request.POST.get("fullname"))
    #    print(request.POST.get("email"))
    #    print(request.POST.get("message"))
    return render(request, "contact/view.html", context)

def home_page_old(request):
    html_ = """
    <!doctype html>
    <html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">

        <title>Hello, world!</title>
    </head>
    <body>
        <div class="text-center">
            <h1>Hello, world!</h1>
        </div>
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
    </body>
    </html>
    """
    return HttpResponse(html_)