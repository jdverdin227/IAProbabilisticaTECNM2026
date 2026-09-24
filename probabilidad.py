from datos import clientes, preferencias


clientes = clientes()
preferencias = preferencias()


print("CLIENTES")
print(clientes.head())


print("\nPROBABILIDAD DE PRESUPUESTO")


probabilidad = (
    clientes["Presupuesto"]
    .value_counts(normalize=True)
)


print(probabilidad)


print("\nPROBABILIDAD DE QUE GUSTE")


probabilidad_gusta = preferencias["LeGusta"].mean()


print(
    round(probabilidad_gusta, 4)
)