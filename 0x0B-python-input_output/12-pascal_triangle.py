#!/ussr/bin/python3
"""Defines a Pascal's triangle function"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n
    Return:
        a list of lists of integers representing the triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
