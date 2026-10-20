"""Enumeração CategoriaXP, conforme o Diagrama de Classes da Entrega 02.

A ordem dos valores é a ordem das posições do vetorXP do PetVirtual.
"""

from enum import Enum


class CategoriaXP(Enum):
    INTELECTUAL = 0
    SABEDORIA = 1
    ZEN = 2
    ATLETICO = 3
    HIDRATACAO = 4
