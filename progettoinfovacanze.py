import random

class Cartella:
    def __init__(self):
        self.numeri = self.genera_cartella()

    def genera_cartella(self):
        """
        Genera una cartella con 15 numeri distribuiti su una griglia 3x9.
        Ogni riga contiene 5 numeri e 4 spazi vuoti, con numeri da 1 a 90 distribuiti su 9 colonne.
        """
        cartella = [[0] * 9 for _ in range(3)]
        numeri_disponibili = random.sample(range(1, 91), 15) 
        numeri_disponibili.sort()

        for num in numeri_disponibili:
            riga = (num - 1) // 10
            colonna = (num - 1) % 9
            while cartella[riga][colonna] != 0:
                colonna = (colonna + 1) % 9
            cartella[riga][colonna] = num
        return cartella

    def stampa_cartella(self):
        """ Stampa la cartella in modo leggibile. """
        for riga in self.numeri:
            print(" ".join([f"{n if n != 0 else ' '}" for n in riga]))


class Tombola:
    def __init__(self, numero_giocatori):
        self.giocatori = [Cartella() for _ in range(numero_giocatori)]
        self.numeri_estratti = random.sample(range(1, 91), 90)
        self.num_estratti = 0
        self.vincite = {}

    def estrai_numero(self):
        """ Estrae un numero casuale e aumenta il contatore degli estratti. """
        numero = self.numeri_estratti[self.num_estratti]
        self.num_estratti += 1
        return numero

    def controlla_vincite(self):
        """ Controlla se un giocatore ha vinto (ambo, terna, quaterna, cinquina, tombola). """
        for i, giocatore in enumerate(self.giocatori):
            numeri_trovati = [num for riga in giocatore.numeri for num in riga if num != 0 and num in self.numeri_estratti[:self.num_estratti]]
            self.vincite[i] = numeri_trovati

            if len(numeri_trovati) >= 6:
                if len(numeri_trovati) == 15:
                    return f"Giocatore {i+1} ha fatto Tombola!"
                if len(numeri_trovati) >= 5:
                    return f"Giocatore {i+1} ha fatto Cinquina!"
                if len(numeri_trovati) >= 4:
                    return f"Giocatore {i+1} ha fatto Quaterna!"
                if len(numeri_trovati) >= 3:
                    return f"Giocatore {i+1} ha fatto Terna!"
                if len(numeri_trovati) >= 2:
                    return f"Giocatore {i+1} ha fatto Ambo!"
        return None

    def stampa_tavolo(self):
        """ Stampa la situazione attuale dei giocatori con i numeri estratti. """
        print(f"\nNumeri estratti: {self.numeri_estratti[:self.num_estratti]}")
        print("\nSituazione dei giocatori:")
        for i, giocatore in enumerate(self.giocatori):
            print(f"Giocatore {i+1}: {self.vincite[i]} numeri trovati.")
            giocatore.stampa_cartella()
            print()

def main():
    numero_giocatori = int(input("Inserisci il numero di giocatori: "))
    tombola = Tombola(numero_giocatori)

    while tombola.num_estratti < 90:
        numero_estratto = tombola.estrai_numero()
        print(f"Numero estratto: {numero_estratto}")
        tombola.stampa_tavolo()

        vincita = tombola.controlla_vincite()
        if vincita:
            print(vincita)
            break

if __name__ == "__main__":
    main()