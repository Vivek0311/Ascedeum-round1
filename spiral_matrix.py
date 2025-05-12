def sprial_matrix(n: int) -> list[list]:
    sprial_matrix_list = [[None] * n for _ in range(0, n)]

    top = 0
    right = len(sprial_matrix_list[0])
    bottom = len(sprial_matrix_list)
    left = 0
    count = 1

    while count - 1 != len(sprial_matrix_list) ** 2:
        for i in range(top, right):
            sprial_matrix_list[top][i] = count
            count += 1
        top += 1

        for j in range(top, bottom):
            sprial_matrix_list[j][right - 1] = count
            count += 1
        right -= 1

        for k in range(right - 1, left - 1, -1):
            sprial_matrix_list[bottom - 1][k] = count
            count += 1
        bottom -= 1

        for l in range(bottom - 1, top - 1, -1):
            sprial_matrix_list[l][left] = count
            count += 1
        left += 1

    return sprial_matrix_list


resultant_sprial_matrix = sprial_matrix(4)

for row in resultant_sprial_matrix:
    print(row)


