from django.shortcuts import render, redirect
from django.http import FileResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .groq_api import generate_ai_content
from .pdf_generator import create_pdf
from .models import AIHistory
from .forms import RegisterForm, LoginForm


# ---------------- HOME ----------------

def home(request):

    total_notes = AIHistory.objects.filter(feature="Notes").count()
    total_quiz = AIHistory.objects.filter(feature="Quiz").count()
    total_flashcards = AIHistory.objects.filter(feature="Flashcards").count()
    total_studyplan = AIHistory.objects.filter(feature="Study Plan").count()

    if request.method == "POST":

        topic = request.POST.get("topic")
        feature = request.POST.get("feature")

        if feature == "notes":
            return redirect(f"/notes/?topic={topic}")

        elif feature == "quiz":
            return redirect(f"/quiz/?topic={topic}")

        elif feature == "flashcards":
            return redirect(f"/flashcards/?topic={topic}")

        elif feature == "study_plan":
            return redirect(f"/study-plan/?topic={topic}")

    return render(request, "index.html", {
        "total_notes": total_notes,
        "total_quiz": total_quiz,
        "total_flashcards": total_flashcards,
        "total_studyplan": total_studyplan,
    })


# ---------------- NOTES ----------------

@login_required
def notes(request):

    content = ""
    topic = request.GET.get("topic", "")

    if request.method == "POST":
        topic = request.POST.get("topic")

    if topic:

        prompt = f"Generate detailed study notes about {topic}"

        content = generate_ai_content(prompt)

        AIHistory.objects.create(
            user=request.user,
            topic=topic,
            feature="Notes",
            content=content
        )

    return render(request, "notes.html", {
        "content": content,
        "topic": topic
    })


# ---------------- QUIZ ----------------

@login_required
def quiz(request):

    content = ""
    topic = request.GET.get("topic", "")

    if request.method == "POST":
        topic = request.POST.get("topic")

    if topic:

        prompt = f"Generate 10 MCQ quiz questions with answers about {topic}"

        content = generate_ai_content(prompt)

        AIHistory.objects.create(
            user=request.user,
            topic=topic,
            feature="Quiz",
            content=content
        )

    return render(request, "quiz.html", {
        "content": content,
        "topic": topic
    })
# ---------------- FLASHCARDS ----------------

@login_required
def flashcards(request):

    content = ""
    topic = request.GET.get("topic", "")

    if request.method == "POST":
        topic = request.POST.get("topic")

    if topic:

        prompt = f"Generate flashcards for {topic}"

        content = generate_ai_content(prompt)

        AIHistory.objects.create(
            user=request.user,
            topic=topic,
            feature="Flashcards",
            content=content
        )

    return render(request, "flashcards.html", {
        "content": content,
        "topic": topic
    })


# ---------------- STUDY PLAN ----------------

@login_required
def study_plan(request):

    content = ""
    topic = request.GET.get("topic", "")

    if request.method == "POST":
        topic = request.POST.get("topic")

    if topic:

        prompt = f"Generate a 7-day study plan for {topic}"

        content = generate_ai_content(prompt)

        AIHistory.objects.create(
            user=request.user,
            topic=topic,
            feature="Study Plan",
            content=content
        )

    return render(request, "study_plan.html", {
        "content": content,
        "topic": topic
    })


# ---------------- DOWNLOAD PDF ----------------

@login_required
def download_pdf(request):

    latest = AIHistory.objects.filter(
        user=request.user
    ).order_by("-created_at").first()

    if latest:
        title = f"{latest.feature} - {latest.topic}"
        content = latest.content
    else:
        title = "Vetri AI Study Buddy"
        content = "No AI generated content available."

    file_path = create_pdf(title, content)

    return FileResponse(
        open(file_path, "rb"),
        as_attachment=True,
        filename="study_notes.pdf"
    )


# ---------------- HISTORY ----------------

@login_required
def history(request):

    history = AIHistory.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "history.html",
        {
            "history": history
        }
    )


# ---------------- REGISTER ----------------

def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            login(request, user)

            return redirect("/")

    else:
        form = RegisterForm()

    return render(
        request,
        "register.html",
        {
            "form": form
        }
    )


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



# ---------------- LOGOUT ----------------

def user_logout(request):

    logout(request)

    return redirect("/") 