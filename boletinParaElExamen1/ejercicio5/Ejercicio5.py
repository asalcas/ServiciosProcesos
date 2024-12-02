
from multiprocessing import Process


def sumaTodo(num1, num2):
    if num1 > num2: # Si num1 es mayor que num2
        num1, num2 = num2, num1 # Entonces (num1 = num2) y (num2 = num1)
    
    suma = sum(range(num1 , num2 + 1))
    print(f"La suma de todos lo valores entre {num1} y {num2} da como resultado: {suma}")
    
if __name__ == "__main__":
    p1 = Process(target=sumaTodo, args=(3, 2))
    p2 = Process(target=sumaTodo, args=(1, 5))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()