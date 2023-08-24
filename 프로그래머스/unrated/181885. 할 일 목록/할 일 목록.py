def solution(todo_list, finished):
    return [x for x, y in zip(todo_list, finished) if y==False]