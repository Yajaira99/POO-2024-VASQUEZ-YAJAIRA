# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for dia in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal que organiza la lógica del programa
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}°C")

# Llamada a la función principal
if __name__ == "__main__":
    main()




POO


class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, dia):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
                self.temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

    def calcular_promedio(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

def main():
    clima = ClimaDiario()
    for dia in range(7):
        clima.ingresar_temperatura(dia)
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
