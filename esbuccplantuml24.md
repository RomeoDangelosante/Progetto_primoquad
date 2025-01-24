```mermaid
classDiagram
    class Utente {
    + nome_utente: str
    + email: str
    - password: str
    + immagine_profilo: str
    - foto: list[Foto]

    }

    class Foto {
    + titolo: str
    + descrizione: str
    + utente: str
    + data_caricamento: int
    + album: List[Album]
    }
    
    class Commento {
    + testo: str
    + utente: str
    + foto: str
    }

    class Album {
    + titolo: str
    + descrizione: str
    + data_pubblicazione: int
    + utente: str
    + foto: List[Foto]
    }

    Utente "1" -- "*" Foto : carica
    Foto "1" -- "*" Commento : riceve
    Foto "1" <--  Commento
    Commento <-- Utente : Puo fare
    Album "1" -- "*" Foto
    
