#Ejercicio 2: SIN RESOLVER

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

if __name__ == "__main__":
    run2()