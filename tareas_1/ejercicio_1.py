#Ejercicio 1: RESUELTO

def run1():
    t = int(input())

    for i in range(t):
        n = int(input())
        notas = list(map(int, input().split()))
        
        for j in range(n):
            if notas.count(notas[j])==1:
                print(notas.index(notas[j]))
                break

if __name__ == "__main__":
    run1()