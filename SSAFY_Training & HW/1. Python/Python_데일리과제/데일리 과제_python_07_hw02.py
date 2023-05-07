

def collatz(number):
    count = 0
    while number != 1:
        if number % 2 == 0 : number /=2
        else : number = number*3 + 1
        count += 1
        if count >= 500: return print(-1)
    return print(count)



collatz(6)  # => 8
collatz(16)  # => 4
collatz(27)  # => 111
collatz(626331)  # => -1
