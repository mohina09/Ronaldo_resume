from django.shortcuts import render, redirect
from .models import Portfolio, About, Service, Resume_work, Resume_education
from .forms import ContactForm


def index(request):
    about = About.objects.all()
    service = Service.objects.all()
    resume_work = Resume_work.objects.all()
    resume_education = Resume_education.objects.all()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(".")
    portfolio = Portfolio.objects.all().order_by("-id")
    contex = {
        "portfolios": portfolio,
        "abouts": about,
        "services": service,
        "work": resume_work,
        "education": resume_education,
        "forms": form
    }
    return render(request, "index.html", contex)


from django.shortcuts import render

# Create your views here.
