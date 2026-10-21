def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):
    # Corrección del error: validamos antes de operar
    if b == 0:
        print("Error: No es posible dividir entre cero.")
        return None
    return a / b

if __name__ == "__main__":
    print("--- Calculadora Ejecutándose ---")
    
    num1 = 10
    num2 = 5
    
    resultado_suma = sumar(num1, num2)
    resultado_resta = restar(num1, num2)
    
    print(f"Suma: {resultado_suma}")
    print(f"Resta: {resultado_resta}")
    
    print("\n--- Probando División Segura ---")
    valor_cero = 0
    
    # Aquí llamamos a la función ya corregida
    resultado_division = dividir(num1, valor_cero)
