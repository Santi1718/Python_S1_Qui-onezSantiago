def fibonacci(n):

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def fibonacci_pares(n):
    
    fib_sequence = fibonacci(n)
    return [num for num in fib_sequence if num % 2 == 0]

def suma_fibonacci_en_rango(inicio, fin):
    
    fib_sequence = fibonacci(fin + 1)  # Genera secuencia hasta fin + 1 para incluir fin
    return sum(num for num in fib_sequence if inicio <= num <= fin)