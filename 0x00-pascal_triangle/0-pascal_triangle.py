'''
A function that returns a list of lists of integers 
representing the Pascal’s triangle of n
'''

def pascal_triangle(n):
    if n <= 0:
        return []
    result = [[1]]
    for i in range(n - 1):
        temp = [0] + result[i] + [0]
        row = []
        for j in range(len(temp) -1 ):
            row.append(temp[j] + temp[j+1])
        result.append(row)
    return result
