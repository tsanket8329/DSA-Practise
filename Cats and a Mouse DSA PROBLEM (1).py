HACKERRANK – Cats and a Mouse

Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to determine which cat will reach the mouse first, assuming the mouse does not move and the cats travel at equal speed.

If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.

Function Description

Complete the function catAndMouse.

catAndMouse has the following parameter(s):

int x: Cat A's position

int y: Cat B's position

int z: Mouse C's position

Returns

string: Either "Cat A", "Cat B", or "Mouse C"

Input Format

The first line contains a single integer q, the number of queries.

Each of the next q lines contains three space-separated integers:

x (Cat A position)

y (Cat B position)

z (Mouse position)

Constraints

1 ≤ q ≤ 100

1 ≤ x, y, z ≤ 100

Sample Input 0
2
1 2 3
1 3 2
Sample Output 0
Cat B
Mouse C
Explanation 0
Query 1:

x = 1, y = 2, z = 3

Distance of Cat A from mouse = |1 − 3| = 2
Distance of Cat B from mouse = |2 − 3| = 1

Cat B is closer → print Cat B

Query 2:

x = 1, y = 3, z = 2

Distance of Cat A from mouse = |1 − 2| = 1
Distance of Cat B from mouse = |3 − 2| = 1

Both distances equal → print Mouse C
CODE: 
#!/bin/python3

def catAndMouse(x, y, z):
    distA = abs(x - z)
    distB = abs(y - z)
    
    if distA < distB:
        return "Cat A"
    elif distB < distA:
        return "Cat B"
    else:
        return "Mouse C"

# -------- INPUT --------
q = int(input().strip())

for _ in range(q):
    x, y, z = map(int, input().split())
    result = catAndMouse(x, y, z)
    print(result)