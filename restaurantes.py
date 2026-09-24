from datos import clientes
from datos import preferencias
from datos import restaurantes


clientes = clientes()
preferencias = preferencias()
restaurantes = restaurantes()


datos = preferencias.merge(
    clientes,
    on="ClienteId"
)


datos = datos.merge(
    restaurantes,
    on="RestauranteId"
)


print("\nDATOS COMPLETOS")

print(datos.head())


print("\nPROBABILIDAD POR TIPO DE COMIDA")


resultado = (
    datos
    .groupby("TipoComida")["LeGusta"]
    .mean()
    .sort_values(
        ascending=False
    )
)


print(resultado)