paises = input("Ingrese paises espaceados por coma para no complicarme la vida por favor:")

paisesEnSet = set()

arr = sorted(paises.split(","), reverse=True)


for i in arr:
    paisesEnSet.add(i)

print(arr)
print(paisesEnSet)