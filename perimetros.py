def perCuadrado(): 
    lado=float(input("Ingrese el valor del perímetro: ")) 
    return (print("El períemtro del cuadrado es: ", lado**4))
perCuadrado()    

def perRectangulo(): #Esta es la segunda versión de perímetros
    base=float(input("Ingrese el valor de la base: "))
    altura=float(input("Ingrese el valor de la altura: "))
    return (print("El área del rectángulo es: ", 2 * base + 2 * altura))
perRectangulo()  

pi=3,1416

def perCirculo():
    radio=float(input("Ingrese el valor del radio: "))
    altura=float(input("Ingrese el valor de la altura: "))
    return (print("El área del círculo es: ", 2+pi * radio ** 2))
perCirculo()  