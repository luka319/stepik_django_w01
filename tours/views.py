from django.shortcuts import render
# from django.http import HttpResponseNotFound

# Create your views here.
"""
главной main_view;
– направления departure_view;
– тура tour_view.
"""


def main_view(request):

    return render(request, "index.html", )


def departure_view(request, departure):

    return render(request, "departure.html", )


def tour_view(request, id):

    return render(request, "tour.html", )
