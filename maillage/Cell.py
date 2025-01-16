from dataclasses import dataclass
from shapely.geometry import Polygon

@dataclass
class Cell:
    latitude: float      # Latitude du centre de la cellule
    longitude: float     # Longitude du centre de la cellule
    size: float          # Taille de la cellule (en degrés)
    data: float = 0.0    # Donnée associée (valeur par défaut à 0.0)
    data_size: int = 0

    def to_dict(self) -> dict:
        """
        Retourne la cellule sous forme de dictionnaire.
        """
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'size': self.size,
            'data': self.data,
            'data_size' : self.data_size
        }

    def to_polygon(self) -> Polygon:
        """
        Retourne la cellule sous forme de polygone (carré).
        """
        half_size = self.size / 2
        return Polygon([
            (self.longitude - half_size, self.latitude - half_size),  # Bas-gauche
            (self.longitude + half_size, self.latitude - half_size),  # Bas-droite
            (self.longitude + half_size, self.latitude + half_size),  # Haut-droite
            (self.longitude - half_size, self.latitude + half_size)   # Haut-gauche
        ])

    def __str__(self):
        return (f"Cellule au centre ({self.latitude}, {self.longitude}) "
                f"avec taille {self.size}° et donnée {self.data}")
