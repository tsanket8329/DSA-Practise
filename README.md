DSA-Practice
HackerRank 1: Left Rotation
This repository contains a solution for the Left Rotation problem from HackerRank
Problem Statement
A left rotation operation on a circular array shifts each of the array's elements 1 unit to the left. The elements that fall off the left end reappear at the right end.
Given an integer d, rotate the array that many steps to the left and return the result.
Example
text d = 2 arr = [1, 2, 3, 4, 5] After 2 rotations: [3, 4, 5, 1, 2]

HackerRank 2: Drawing Book
This repository contains a solution for the Drawing Book problem from HackerRank.

Problem Statement
A teacher asks the class to open their books to a page number. A student can start turning pages either from the front of the book or from the back. They always turn pages one at a time. When the book is opened, page 1 is always on the right side. When a page is flipped, two new pages become visible (except possibly the last page). Each page except the last page is printed on both sides. Given a book with n pages and a target page p, determine the minimum number of page turns required to reach page p. The student may start turning pages from either the front or the back of the book. Example n = 6 p = 2 Turning from the front: 1 page turn Turning from the back: 2 page turns Minimum page turns required: 1

HackerRank 3: Counting Valleys
This repository contains a solution for the Counting Valleys problem from HackerRank.
Problem Statement
An avid hiker records their hike using uphill (U) and downhill (D) steps. The hike always starts and ends at sea level, and each step changes the altitude by one unit. A valley is defined as a sequence of steps below sea level, starting with a step down from sea level and ending with a step up to sea level. Given the number of steps and the path taken, determine the number of valleys walked through. Example Input: steps = 8
path = UDDDUDUU Output: 1 Explanation: The hiker goes below sea level once and returns back to sea level, completing one valley. Here are the exact lines written in the picture:


HackerRank 4: Electronic Shop
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return -1. Example b = 60 keyboards = [40, 50, 60] drives = [5, 8, 12] The person can buy a 40 keyboard + 12 USB drive = 52, or a 50 keyboard + 8 USB drive = 58. Choose the latter as the more expensive option and return 58. Function Description Complete the getMoneySpent function in the editor below. getMoneySpent has the following parameter(s):
int keyboards[n]: the keyboard prices int drives[m]: the drive prices int b: the budget Returns int: the maximum that can be spent, or -1 if it is not possible to buy both items Input Format The first line contains three space-separated integers b, n, and m, the budget, the number of keyboard models and the number of USB drive models. The second line contains n space-separated integers keyboard[i], the prices of each keyboard model. The third line contains m space-separated integers drives, the prices of the USB drives.
Constraints 1 ≤ n, m ≤ 1000 1 ≤ b ≤ 10⁶ The price of each item is in the inclusive range [1, 10⁶]. Sample Input 0 10 2 3 3 1 5 2 8 Sample Output 0 9 Explanation 0 Buy the 2nd keyboard and the 3rd USB drive for a total cost of 8 + 1 = 9. 
 Sample Input 1 5 1 1 4 5 Sample Output 1 -1 Explanation 1 There is no way to buy one keyboard and one USB drive because 4 + 5 > 5, so return -1.

HACKERRANK 5 – Cats and a Mouse
Problem Statement Two cats and a mouse are at various positions on a straight line. You are given their starting positions. Your task is to determine which cat will reach the mouse first, assuming: The mouse does not move. Both cats travel at the same speed. If both cats reach the mouse at the same time, they fight and the mouse escapes. Function Description Complete the function catAndMouse. catAndMouse has the following parameters: int x: position of Cat A int y: position of Cat B int z: position of Mouse C Returns string:

"Cat A" if Cat A reaches first

"Cat B" if Cat B reaches first

"Mouse C" if both reach at the same time
Input Format

The first line contains an integer q, the number of queries.

Each of the next q lines contains three space-separated integers:

x y z

Constraints

1 ≤ q ≤ 100

1 ≤ x, y, z ≤ 100

Sample Input 5 4 1 2 3 1 3 2 4 2 5 2 6 4 Sample Output 5 Cat B Mouse C Cat A Mouse C Explanation 5 Query 1:

|1 − 3| = 2 |2 − 3| = 1 Cat B is closer → Cat B

Query 2:

|1 − 2| = 1 |3 − 2| = 1 Equal → Mouse C

Query 3:

|4 − 5| = 1 |2 − 5| = 3 Cat A is closer → Cat A

Query 4:

|2 − 4| = 2 |6 − 4| = 2 Equal → Mouse C


ACKERRANK 6 - Forming a Magic Square
Problem We define a magic square to be a 3 × 3 matrix of distinct positive integers from 1 to 9 where the sum of any row, column, or diagonal is always equal to the same number (called the magic constant).
You will be given a 3 × 3 matrix s of integers in the range 1–9. You can change any value a to another value b with a cost of |a − b|. Your task is to convert the matrix into a magic square with the minimum possible cost.The resulting magic square must contain distinct integers from 1 to 9. Function Description Complete the function:
formingMagicSquare(s) Parameter s[3][3] → a 3×3 integer matrix Returnint → minimum cost required to convert the matrix into a magic square Input Format Three lines of input containing three integers each representing the rows of the matrix. Example input: 5 3 4 1 5 8 6 4 2
 Example Input matrix: 5 3 4 1 5 8 6 4 2 One possible magic square: 8 3 4 1 5 9 6 7 2 Cost calculation: |5-8| + |5-5| + |8-9| + |4-7| = 3 Minimum cost = 3 Sample Input 0 4 9 2 3 5 7 8 1 5 Output 1 Explanation: Change 5 → 6 in the last cell with cost 1. CODE: def formingMagicSquare(s): magic_squares = [ [[8,1,6],[3,5,7],[4,9,2]], [[6,1,8],[7,5,3],[2,9,4]], [[4,9,2],[3,5,7],[8,1,6]], [[2,9,4],[7,5,3],[6,1,8]], [[8,3,4],[1,5,9],[6,7,2]], [[4,3,8],[9,5,1],[2,7,6]], [[6,7,2],[1,5,9],[8,3,4]], [[2,7,6],[9,5,1],[4,3,8]] ]

min_cost = float('inf')

for magic in magic_squares:
    cost = 0
    for i in range(3):
        for j in range(3):
            cost += abs(s[i][j] - magic[i][j])
    min_cost = min(min_cost, cost)

    return min_cost
s = [] for _ in range(3): s.append(list(map(int, input().split())))

print(formingMagicSquare(s)) Time Complexity O(1)

Because only 8 possible magic squares are checked.


HackerRank 7: Picking Numbers
This repository contains a solution for the Picking Numbers problem from HackerRank.

Problem Statement

Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

You may choose any elements from the array, but the difference between every pair of numbers in the chosen subarray must be ≤ 1.

Return the maximum possible length of such a subarray.

Example arr = [1, 1, 2, 2, 4, 4, 5, 5, 5]

Possible valid subarrays:

[1, 1, 2, 2] [4, 4, 5, 5, 5]

Explanation:

In [1,1,2,2] → difference between elements is at most 1

In [4,4,5,5,5] → difference between elements is at most 1

The longest valid subarray is:

[4, 4, 5, 5, 5]

Output:
5 Approach

Count the frequency of each number in the array.

For each number i, check the total count of numbers i and i+1.

The maximum of these sums gives the longest valid subarray.

Time Complexity:

O(n)

Space Complexity:

O(1)

HACKERRANK 8 : Designer Pdf viewer
HACKERRANK: Designer PDF Viewer
Problem

Each letter a–z has a height stored in array h[26].

Given a word, highlight it in a PDF viewer. Each letter width = 1 unit.

Area of highlight =

max letter height × length of word Example

Input

1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 abc

Output

9

Explanation

a = 1 b = 3 c = 1 max height = 3 word length = 3

Area = 3 × 3 = 9

HACKERRANK 8 : Designer Pdf viewer
HACKERRANK: Designer PDF Viewer

Problem

Each letter a–z has a height stored in array h[26].

Given a word, highlight it in a PDF viewer. Each letter width = 1 unit.

Area of highlight =
max letter height × length of word Example

Input

1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 abc

Output

9

Explanation

a = 1 b = 3 c = 1 max height = 3 word length = 3

Area = 3 × 3 = 9
HACKERRANK 9 : Utopian Tree
The Utopian Tree goes through 2 growth cycles every year:

Spring: The height of the tree doubles.

Summer: The height of the tree increases by 1 meter.
nitially, a sapling is planted with a height of 1 meter at the beginning of spring.

Your task is to determine the height of the tree after n growth cycles.

Function Description

Complete the function:
int utopianTree(int n)

Parameter:

n → number of growth cycles.

Return:

The height of the tree after n cycles.

Input Format

First line contains integer t → number of test cases.

Each of the next t lines contains an integer n.

Sample Input 3 0 1 4 Sample Output 1 2 7 Explanation Cycle Operation Height 0 Initial height 1 1 Spring (×2) 2 2 Summer (+1) 3 3 Spring (×2) 6 4 Summer (+1) 7

So after 4 cycles, height = 7.

HACKERRANK 10: Climbing the Leaderboard
An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked 1.

Players with the same score receive the same rank.

The next player gets the immediately following rank.

Example

Leaderboard scores:

100 100 50 40 40 20 10
Ranks become:

1 1 2 3 3 4 5

If the player scores are:

5 25 50 120

Then their ranks after each game are:

6 4 2 1

Function Description

Complete the function:

climbingLeaderboard

Parameters
ranked[n] → leaderboard scores in descending order

player[m] → player's game scores

Returns

int[m] → player's rank after each game

Input Format n ranked scores m player scores Example: 7 100 100 50 40 40 20 10 4 5 25 50 120

Output 6 4 2 1
Approach

Remove duplicate scores from the leaderboard.

Traverse from the end of leaderboard.

Compare each player score with leaderboard scores.

Move pointer left until the correct rank is found.

Since player scores are ascending, the pointer only moves one direction, making the solution efficient. ⏱ Time Complexity O(n + m) n = leaderboard size m = player scores

2075. Decode the Slanted Cipher Text
This project decodes a slanted (diagonal) cipher text into its original message.
The encoded string is formed by placing characters diagonally in a matrix and reading row-wise.
To decode, we reconstruct the matrix using given rows and columns.
Then, we traverse the matrix diagonally to retrieve the original text.
APPROACH:
Calculate columns using: cols = length / rows
Fill matrix row-wise
Traverse diagonally (top-left to bottom-right)
Remove trailing spaces

---->>>Robot Return to Origin

This project determines whether a robot returns to its original position after executing a sequence of moves.
The robot starts at the origin (0, 0) on a 2D plane.
It can move Up (U), Down (D), Left (L), and Right (R).
Each move updates the robot’s position accordingly.
The program processes a string of movements as input.
After executing all moves, it checks the final coordinates.
If the robot returns to (0, 0), the output is true.
Otherwise, the output is false.
This project demonstrates basic string processing and coordinate tracking.
It is useful for understanding simple logic building and problem-solving.

HACKERRANK 11: HURDLE RACE
HackerRank “The Hurdle Race” in Q & A format:

Question

In a hurdle race game, a character can jump up to k units high naturally. There are n hurdles with different heights.

The character can drink a magic potion, and each dose increases the jump height by 1 unit.
Find the minimum number of potion doses needed so the character can jump over all hurdles.

If the character can already jump the highest hurdle, return 0.

Input

First line: two integers n and k

Second line: n space-separated integers representing hurdle heights.
Example Input 5 4 1 6 3 5 2 Example Output 2 Explanation

Maximum jump height = 4

Tallest hurdle = 6

Potion doses needed = 6 − 4 = 2

HACKERRANK 12: BEAUTIFUL DAYS AT THE MOVIES
Question: Beautiful Days at the Movies

Lily defines a number as beautiful if:

number reverse(number) is divisible by 𝑘 ∣number−reverse(number)∣ is divisible by k

Given three integers:

i → starting day

j → ending day

k → divisor

👉 Count how many numbers from i to j (inclusive) are beautiful. Loop from i to j

For each number:

Reverse it

Find difference with original

Check if divisible by k

Count valid numbers

🧪 Example

Input:

20 23 6

Output:

2 ⏱️ Complexity

Time: O(n × digits)

Space: O(1)
