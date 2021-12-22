#Write a function that takes n as parameter and return true if and only if n is an happy number, false otherwise.
def numeroFeliz(numero):
    if numero == 1 or numero == 7:
        return True      
    nuevoNumero = numero
    while len(str(nuevoNumero)) > 1:
        nuevoNumero = 0
        while numero > 0:
            ultimoDigito = numero % 10
            nuevoNumero += ultimoDigito * ultimoDigito
            numero = int(numero / 10)
        if nuevoNumero == 1:
            return True      
        numero = nuevoNumero 
    if nuevoNumero == 7:
        return True      
    return False

if __name__ == "__main__":
    assert numeroFeliz(1) == True
    assert numeroFeliz(2) == False
    assert numeroFeliz(7) == True
    assert numeroFeliz(16) == False
    assert numeroFeliz(23) == True
    assert numeroFeliz(86) == True