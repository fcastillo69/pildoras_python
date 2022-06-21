print("Programa de becas")

distancia_escuela=int(input("Introduce la dicstancia a la escuela en km "))
print(distancia_escuela)

numero_hermanos=int(input("Intrudice el no. de hermanos en el centro "))
print(numero_hermanos)

salario_familiar=int(input("Introduce el salario familiar bruto "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<20000:
    print("Tienes derecho a beca")

else:
    print("No tienes derecho a beca")
