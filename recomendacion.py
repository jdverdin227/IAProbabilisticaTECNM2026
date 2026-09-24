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


cliente_id = 10


cliente = clientes[
    clientes["ClienteId"] == cliente_id
].iloc[0]


print("CLIENTE")

print(cliente)