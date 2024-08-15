from dataclasses import dataclass

@dataclass
class Movie:
    """ Class representing all properties of a movie """
    title: str
    year: int
    rating: str
    director: str
    
    def details(self):
        return f'{self.title}({self.year}), rated {self.rating}, released {self.year}'
    
    