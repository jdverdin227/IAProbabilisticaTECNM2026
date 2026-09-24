import pandas as pd
from conexion import conectar


def clientes():

    conexion = conectar()

    datos = pd.read_sql(
        "SELECT * FROM Clientes",
        conexion
    )

    conexion.close()

    return datos


def restaurantes():

    conexion = conectar()

    datos = pd.read_sql(
        "SELECT * FROM Restaurantes",
        conexion
    )

    conexion.close()

    return datos


def preferencias():

    conexion = conectar()

    datos = pd.read_sql(
        "SELECT * FROM Preferencias",
        conexion
    )

    conexion.close()

    return datos


def visitas():

    conexion = conectar()

    datos = pd.read_sql(
        "SELECT * FROM Visitas",
        conexion
    )

    conexion.close()

    return datos