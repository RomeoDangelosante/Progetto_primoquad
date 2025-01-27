```mermaid
classDiagram
    class Film {
    + titolo: str
    + regista: str
    + anno: int
    + genere: str
    + valutazione:int
    }

    class Libreria {
    + film: list[Film]
    }

Film "*" -- "1" Libreria : contiene
