

class Utente:
    def __init__(self, nome_utente: str, email: str, password: str, immagine_profilo: str = None, biografia: str = None):
        self.nome_utente = nome_utente
        self.email = email
        self.password = password
        self.immagine_profilo = immagine_profilo
        self.biografia = biografia
        self.foto: list[Foto] = []
        self.album: list[Album] = []

    def carica_foto(self, foto: 'Foto') -> None:
        self.foto.append(foto)

    def crea_album(self, album: 'Album') -> None:
        self.album.append(album)


class Foto:
    def __init__(self, titolo: str, descrizione: str, utente: Utente, album : list['Album'] = None):
        self.id = id(self)
        self.titolo = titolo
        self.descrizione = descrizione
        self.utente = utente
        self.album = album
        self.commenti: list[Commento] = []

        utente.carica_foto(self)

        if album:
            album.aggiungi_foto(self)

    def aggiungi_commento(self, commento: 'Commento') -> None:
        self.commenti.append(commento)


class Album:
    def __init__(self, titolo: str, descrizione: str, utente: Utente):
        self.titolo = titolo
        self.descrizione = descrizione
        self.utente = utente
        self.foto: list[Foto] = []

        utente.crea_album(self)

    def aggiungi_foto(self, foto: Foto) -> None:
        if foto not in self.foto:
            self.foto.append(foto)
            foto.album = self


class Commento:
    def __init__(self, testo: str, utente: Utente, foto: Foto):
        self.testo = testo
        self.utente = utente
        self.foto = foto

        foto.aggiungi_commento(self)

if __name__ == "__main__":
    utente1 = Utente("Mirko alessandrini", "mirkozeb@gmail.com", "paguri08@", "immagine.jpg", "Appassionato di cornetti")

    album1 = Album("Ilzebby", "Foto del pesce mio", utente1)

    foto1 = Foto("ilpescemio", "Un bellissimo pesce di meozb", utente1, album1)

    commento1 = Commento("Bellissima mamma!", utente1, foto1)

    print(f"Utente: {utente1.nome_utente}, Album: {[album.titolo for album in utente1.album]}, Foto: {[foto.titolo for foto in utente1.foto]}")
    print(f"Foto '{foto1.titolo}' commenti: {[commento.testo for commento in foto1.commenti]}")