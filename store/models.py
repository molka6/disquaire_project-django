from django.db import models


# Relation plusieurs à un(entre reservation et contact)

# Une reservation appartient a un seul contact 
# Un contact peut avoir plusieurs reservation 

# on_delete=models.CASCADE: si une réservation est supprimée, le contact reste dans la base
                            # si un contact est supprimer , tous les reservation est suprimer aussi :

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)


class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
# -------------------------------------------------------------------
# Relation plusieurs à un (artistes et les albums)

class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Album(models.Model):
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)  #*****
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture = models.URLField()
    # foreignkey
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)


class Artist(models.Model):

    def __str__(self):
        return self.name


class Contact(models.Model):

    def __str__(self):
        return self.name


class Album(models.Model):

    def __str__(self):
        return self.title


class Booking(models.Model):

    def __str__(self):
        return self.contact.name
# ------------------------------------------------------------------------------------------------------------------
                    # pfa

# class Utlisateur(models.Model):
#       name = models.CharField(max_length=200)
#       adresse= models.CharField(max_length=200)

# class Matricule(models.Model):
#         created_at = models.DateTimeField(auto_now_add=True)
#         utlisateur= models.ForeignKey(Utlisateur, on_delete=models.CASCADE)


# --------------------------------------------------------------------------------------------------------------------------------