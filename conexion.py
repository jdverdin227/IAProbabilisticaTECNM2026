import pyodbc
import config


def conectar():

    conexion = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={config.SERVIDOR};"
        f"DATABASE={config.BASE_DATOS};"
        f"UID={config.USUARIO};"
        f"PWD={config.PASSWORD};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )

    return conexion