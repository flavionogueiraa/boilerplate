from django.shortcuts import render


def home(request):
    """Docstring here."""
    context = {
        "section_id": "home",
    }

    return render(
        request,
        "home/home.html",
        context,
    )
