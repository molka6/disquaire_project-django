from django.http import HttpResponse
from .models import Album, Artist, Contact, Booking


def index(request):
    # request albums
    # Album.objects.filter(available=True)
    albums = Album.objects.all()
    formatted_albums = ["<li>{}</li>".format(album.id) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    return HttpResponse(message)


def listing(request):
    albums = Album.objects.filter(available=True)
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    return HttpResponse(message)