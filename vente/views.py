from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from .models import Album, Artist, Contact, Booking
from django.template import loader
from .forms import ContactForm

# get les album de la table (Album)
def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    context = {
        'albums': albums
    }
    return render(request, 'vente/index.html', context)
######## 
def detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    artists = [artist.name for artist in album.artists.all()]
    artists_name = " ".join(artists)
    context = {
        'album_title': album.title,
        'artists_name': artists_name,
        'album_id': album.id,
        'thumbnail': album.picture
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
                email = form.cleaned_data['email']
                name = form.cleaned_data['name']
                contact = Contact.objects.filter(email=email)
                if not contact.exists():
                    # If a contact is not registered, create a new one.
                    contact = Contact.objects.create(
                        email=email,
                        name=name
                    )
                context = {
                'form': form
                }
                return render(request, 'vente/merci.html', context)
        else:
        #    Si le formulaire n'est pas valide, cela signifie qu'il contient des erreurs 
            context['errors'] = form.errors.items()


    else:
        form = ContactForm()
        context['form'] = form    

    return render(request, 'vente/detail.html', context)




































def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        # title contains the query is and query is not sensitive to case.
        albums = Album.objects.filter(title__icontains=query)
    if not albums.exists():
        albums = Album.objects.filter(artists__name__icontains=query)
    title = "Résultats pour la requête %s"%query
    context = {
        'albums': albums,
        'title': title
    }
    return render(request, 'vente/search.html', context)





















# # afficher tous les album
# def listing(request):
#     albums = Album.objects.filter(available=True)
#     formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
#     message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
#     return HttpResponse(message)


    
 