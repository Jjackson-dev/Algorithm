def solution(numbers):
    numbers = list(map(str, numbers))
    #string * 3 => stringstringstring
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
    
