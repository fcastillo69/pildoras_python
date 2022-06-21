nota_alumno=int(input("introduce la nota, por favor "))

if nota_alumno<5:
    print("Insuficiene")

elif nota_alumno<6:
    print("Suficiente")

elif nota_alumno<7:
    print("Bien")

elif nota_alumno<9:
    print("notable")

else:
    print("Sobresaliente")
