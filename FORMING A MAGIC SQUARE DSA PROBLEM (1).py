HACKERRANK - FORMING A MAGIC SQUARE
Forming a Magic Square
Problem

We define a magic square to be a 3 × 3 matrix of distinct positive integers from 1 to 9 where the sum of any row, column, or diagonal is always equal to the same number (called the magic constant).

You will be given a 3 × 3 matrix s of integers in the range 1–9.
You can change any value a to another value b with a cost of |a − b|.

Your task is to convert the matrix into a magic square with the minimum possible cost.

The resulting magic square must contain distinct integers from 1 to 9.

Function Description

Complete the function:

formingMagicSquare(s)

Parameter

s[3][3] → a 3×3 integer matrix

Return

int → minimum cost required to convert the matrix into a magic square

Input Format

Three lines of input containing three integers each representing the rows of the matrix.

Example input:

5 3 4
1 5 8
6 4 2
Example

Input matrix:

5 3 4
1 5 8
6 4 2

One possible magic square:

8 3 4
1 5 9
6 7 2

Cost calculation:

|5-8| + |5-5| + |8-9| + |4-7| = 3

Minimum cost = 3

Sample Input 0
4 9 2
3 5 7
8 1 5
Output
1

Explanation:
Change 5 → 6 in the last cell with cost 1.

CODE: 
def formingMagicSquare(s):
    magic_squares = [
        [[8,1,6],[3,5,7],[4,9,2]],
        [[6,1,8],[7,5,3],[2,9,4]],
        [[4,9,2],[3,5,7],[8,1,6]],
        [[2,9,4],[7,5,3],[6,1,8]],
        [[8,3,4],[1,5,9],[6,7,2]],
        [[4,3,8],[9,5,1],[2,7,6]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[2,7,6],[9,5,1],[4,3,8]]
    ]

    min_cost = float('inf')

    for magic in magic_squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(s[i][j] - magic[i][j])
        min_cost = min(min_cost, cost)

    return min_cost


s = []
for _ in range(3):
    s.append(list(map(int, input().split())))

print(formingMagicSquare(s))
Time Complexity
O(1)

Because only 8 possible magic squares are checked.