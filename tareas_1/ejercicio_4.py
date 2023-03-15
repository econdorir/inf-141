#Ejercicio 4: Resuelto

def run4():
    phrase = list(input().split(' '))
    result = [word.strip('.,;!?') for word in phrase if "o" in word]
    for elem in result:
        print(elem)

if __name__ == "__main__":
    run4()