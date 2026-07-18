# ---------------- LOGIN ----------------

def user_login(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # Debug
            print("=" * 50)
            print("USERNAME:", username)
            print("PASSWORD:", password)

            user = authenticate(
                request,
                username=username,
                password=password
            )

            print("AUTHENTICATED USER:", user)
            print("=" * 50)

            if user is not None:

                login(request, user)

                print("LOGIN SUCCESS")

                return redirect("/")

            else:

                print("LOGIN FAILED")

                return render(
                    request,
                    "login.html",
                    {
                        "form": form,
                        "error": "Invalid Username or Password"
                    }
                )

        else:

            print("FORM ERRORS:", form.errors)

    else:

        form = LoginForm()

    return render(
        request,
        "login.html",
        {
            "form": form
        }
    )