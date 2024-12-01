
from multiprocessing import Pool


def sumarTodo(id, num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
        
    suma = sum(range(num1, num2 + 1))
    print(f"Comienza el proceso numero {id}")
    print(f"El resultado de la suma de los numeros entre: {num1} y {num2} es de: {suma}")
    
if __name__ == "__main__":
    with Pool(processes = 5) as poolEjercicio6:
        variablesParaElPool = [(1,1,5),(2,2,4),(3,6,2),(4,2,7),(5,3,3)] # Contiene (id, num1, num2)
        
        resultados = poolEjercicio6.starmap(sumarTodo, variablesParaElPool)
        
        print(f"Resultados: {resultados}")
        