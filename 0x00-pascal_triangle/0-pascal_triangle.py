#!/usr/bin/python3

def pascal_triangle(n):
    """pascals triangle, returns an empty list if n <= 0."""

    res = []

    if n <= 0:
        return res

    for i in range(n):
        temp_list = []

        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(res[i-1][j-1] + res[i-1][j])
        res.append(temp_list)

    return res
