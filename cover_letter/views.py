from django.shortcuts import render
from cover_letter.models import Reference
from root.utils import get_attribute


def cover_main_view(request, *args):
    return render(request, "components/cover.html", {})


def letter_view_context():
    return {
        'letter': get_attribute("COVER_LETTER")
    }


def references_view_context():
    return {
        'references': Reference.objects.all().order_by("date")
    }


def reference_view_context(reference, wow):
    return {
        'item': reference,
        'wow': wow
    }