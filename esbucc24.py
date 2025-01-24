class Film:
    def __init__(self, titolo, regista, anno, genere, valutazione):
        self.titolo = titolo
        self.regista = regista
        self.anno = anno
        self.genere = genere
        self.valutazione = valutazione

    def __repr__(self):
        return f"{self.titolo} ({self.anno}), Regia: {self.regista}, Genere: {self.genere}, Valutazione: {self.valutazione}/10"
    class Libreria:
    def __init__(self):
        self.film = []

    def aggiungi_film(self, film):
        self.film.append(film)

    def cerca_per_titolo(self, titolo):
        risultati = [f for f in self.film if titolo.lower() in f.titolo.lower()]
        return risultati

    def cerca_per_regista(self, regista):
        risultati = [f for f in self.film if regista.lower() in f.regista.lower()]
        return risultati

    def visualizza_tutti_i_film(self):
        if self.film:
            for f in self.film:
                print(f)
        else:
            print("Nessun film nella libreria.")

    def calcola_valutazione_media(self):
        if self.film:
            media = sum(f.valutazione for f in self.film) / len(self.film)
            return round(media, 2)
        return 0
libreria = Libreria()

film1 = Film("Inception", "Christopher Nolan", 2010, "Azione", 9)
film2 = Film("The Dark Knight", "Christopher Nolan", 2008, "Azione", 10)
film3 = Film("Pulp Fiction", "Quentin Tarantino", 1994, "Drammatico", 8)
film4 = Film("The Exorcist", "William Friedkin", 1973, "Horror", 7)

libreria.aggiungi_film(film1)
libreria.aggiungi_film(film2)
libreria.aggiungi_film(film3)
libreria.aggiungi_film(film4)

print("Tutti i film nella libreria:")
libreria.visualizza_tutti_i_film()

print("\nRisultati ricerca per titolo 'dark':")
film_trovati = libreria.cerca_per_titolo("dark")
for f in film_trovati:
    print(f)

print("\nRisultati ricerca per regista 'Nolan':")
film_trovati = libreria.cerca_per_regista("Nolan")
for f in film_trovati:
    print(f)

media = libreria.calcola_valutazione_media()
print(f"\nValutazione media dei film: {media}/10")
    