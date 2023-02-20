def solution(numbers, direction):
    if direction == 'right':
        numbers.insert(0, numbers[len(numbers)-1])
        numbers.pop()
        return numbers
    else:
        numbers.insert(len(numbers), numbers[0])
        numbers.pop(0)
        return numbers