from django.shortcuts import render


def meme_generator_view(request):
    """Docstring here."""
    context = {
        "section_id": "meme-generator",
    }

    return render(
        request,
        "home/meme_generator.html",
        context,
    )
