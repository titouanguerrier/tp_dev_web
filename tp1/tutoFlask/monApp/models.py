from .app import db
class Auteur(db.Model):
    idA = db.Column( db.Integer, primary_key=True )
    Nom = db.Column( db.String(100) )
    def __init__(self, Nom):
        self.Nom = Nom
class LIVRE(db.Model):
    idL = db.Column( db.Integer, primary_key=True )
    Prix = db.Column( db.Integer )
    Titre=db.Column( db.String(255) )
    Url=db.Column( db.String(255) )
    Img=db.Column( db.String(255) )
    auteur_id = db.Column (db.Integer , db.ForeignKey ("auteur.idA") )
    auteur = db.relationship ("Auteur", backref =db.backref ("livres", lazy="dynamic") )
    def __init__(self, Prix,Titre,Url,Img):
        self.Prix = Prix
        self.Titre = Titre
        self.Prix = Prix
        self.Url = Url
        self.Img = Img
