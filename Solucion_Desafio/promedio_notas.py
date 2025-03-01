import os

suma = 0
promedio = 0

for i in range(5):
    while True:
        os.system('cls')
        print(f'Promedio actual: {promedio:.2f}')
        try:
            num = int(input(f'Por favor ingrese la calificación número {i + 1}: '))
            if 0 <= num <= 100:
                break
            else:
                print("Error: La calificación debe estar entre 0 y 100. Intente nuevamente.")
                input("Presiona Enter para reintentar...")
        except ValueError:
            print("Error: Ingrese un número válido.")
            input("Presiona Enter para reintentar...")
    
    suma += num
    promedio = suma / (i + 1)

os.system('cls')
print(f'Promedio final: {promedio:.2f}')

if promedio < 40:
    print('Reprobado')
elif 40 <= promedio < 60:
    print('En Recuperación')
else:
    print('Aprobado')



    