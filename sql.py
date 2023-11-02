import sqlite3
from constantes import *
conexion = sqlite3.connect(DATA_BASE)
cursor = conexion.cursor()