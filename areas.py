def areaCuadrado(): #La primera versión se hizo con el pass sin líneas de código
    lado=float(input("Ingrese el valor del lado: ")) #Esta es la segunda versión
    return (print("El área del cuadrado es: ", lado**2))
areaCuadrado()    

def areaRectangulo(): #Esta es la tercera versión
    base=float(input("Ingrese el valor de la base: "))
    altura=float(input("Ingrese el valor de la altura: "))
    return (print("El área del rectángulo es: ", base*altura))
areaRectangulo()  

pi=3,1416

def areaCirculo(): #Esta es la cuarta versión
    radio=float(input("Ingrese el valor del radio: "))
    altura=float(input("Ingrese el valor de la altura: "))
    return (print("El área del círculo es: ", pi * radio ** 2))
areaCirculo()  