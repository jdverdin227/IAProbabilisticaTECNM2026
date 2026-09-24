from datos import clientes, preferencias


clientes = clientes()
preferencias = preferencias()


datos = preferencias.merge(
    clientes,
    on="ClienteId"
)


bajos = datos[
    datos["Presupuesto"] == "Bajo"
]


probabilidad = bajos["LeGusta"].mean()


print(
    "Probabilidad de que guste"
    " dado que el presupuesto es bajo:"
)

print(
    round(probabilidad, 4)
)