#This function will rotate a 2D list clockwise as if it is an image

def rotate(matrix):
    copy = matrix.copy()
    copy.reverse()
    length = len(matrix)
    for i in range(length):
        new = []
        for k in range(length):
            new.append(copy[k][i])
        matrix[i] = new

    return matrix


print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))