#!/usr/bin/python3
'''
def increasing_list_of_lists(n):
    result = []
    for i in r ange(1, n + 1):
        row = list(range(1, i + 1))
        result.append(row)
    return '\n'.join(str(row) for row in result)

n = 3
answer = increasing_list_of_lists(n)
print(answer)
'''

def increasing_list_of_lists(n):
    result = []
    get = 0
    for i in range(1, n + 1):
        row = list(range(1, i + 1))
        if i == 2:
            row[1] = 1
        elif i > 2:
            for j in range(1, n - 3):
                get = row[j] + row[j-1]
                row[j] = get
        result.append(row)
        print(get)
    return result

answer = increasing_list_of_lists(5)
print(answer)
