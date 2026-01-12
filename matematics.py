def suma(a: float, b: float) -> float:
    return float(a + b)


def resta(a: float, b: float) -> float:
    return float(a - b)


def suma_lista(numeros: list) -> float:
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    return float(sum(numeros))


def resta_multiple(a: float, *args: float) -> float:

    resultado = a
    for num in args:
        resultado -= num
    return float(resultado)    