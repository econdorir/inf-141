#Ejercicio 3: RESUELTO

def swap_bits(char):
    binary = format(ord(char), '08b')
    swapped_binary = binary[4:] + binary[:4]
    return swapped_binary

def run3():
    while True:
        try:
            text = input().strip()
            swapped_numbers = [int(swap_bits(char), 2) for char in text]
            print(' '.join(map(str, swapped_numbers)))
        except EOFError:
            break

if __name__ == "__main__":
    run3()