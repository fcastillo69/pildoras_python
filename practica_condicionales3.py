print("Asignatras de este año")
print("Asignaturas optativas: Informtaica grafica -  pruebas de software - usabilidad y accesibilidad")
opcion=input("Escriba la asignatura escogida: ")
asignatura=opcion.lower()

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatra elegida: " +  asignatura)

else:

    print("La asignatura no eta contemplada")

