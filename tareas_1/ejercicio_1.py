def run1():
    t = int(input())

    for i in range(t):
        n = int(input())
        notas = list(map(int, input().split()))
        
        for j in range(n):
            if notas.count(notas[j])==1:
                print(notas.index(notas[j]))
                break

from datetime import datetime
def run2():
    n = int(input())
    for i in range(n):
        minutes = list(map(int,input().split(':')))
        if minutes[0] >= 24 or minutes[1] >= 64:
            continue
        hours = minutes+[0]
        minutes = [0] + minutes
        #transforming to string
        minutes = ':'.join(str(i).zfill(2) for i in minutes)
        hours = ':'.join(str(i).zfill(2) for i in hours)


        hour_1 = datetime.strptime(hours, '%H:%M:%S')
        hour_2 = datetime.strptime(minutes, '%H:%M:%S')

        hours_difference = hour_1-hour_2
        base = datetime(1900, 1, 1)

        result = base + hours_difference

        print(result.strftime('%H:%M:%S'))


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


def run4():
    phrase = list(input().split(' '))
    result = [word.strip('.,;!?') for word in phrase if "o" in word]
    for elem in result:
        print(elem)


def run5():
    m = int(input())
    k = int(input())
    n = (m + 1) * 2**(k-1) - 1
    print(n)

if __name__ == "__main__":
    run5()