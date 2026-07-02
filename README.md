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


HackerRank question 4: Electronic Shop
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

HACKERRANK 13: VIRAL ADVERTISING
📘 Question: Viral Advertising

HackerLand Enterprise is adopting a new viral advertising strategy.

On the first day, the advertisement is shared with 5 people.

Each day:

Half of the people who receive the ad like it (floor(shared / 2)).

Each person who likes it shares it with 3 friends the next day.

No person receives the ad more than once.

🔹 Task

Given an integer n, representing the number of days, determine the total cumulative likes after n days.

🔹 Input

A single integer:

n 🔹 Output

An integer representing total likes after n days.

🔹 Example

Input

3

Output

9 🧠 Explanation
Start with shared = 5

Each day:

Compute liked = shared / 2

Add to total

Update shared = liked * 3

⏱ Complexity

Time: O(n)

Space: O(1)

📌 Largest Number

This project solves the Largest Number problem using Java.
It arranges numbers to form the maximum possible number.
All integers are first converted into strings.
A custom comparator is used to sort numbers.
Sorting is based on (b + a) and (a + b) comparison.
This ensures correct ordering for maximum result.
If the first element is "0", return "0".
This handles the edge case of all zeros.
Finally, all strings are concatenated.
The result is returned as a single string.
Time complexity is O(n log n) due to sorting.

HACKERRANK 14 : SAVE THE PRISONERS
📘 Question: Save the Prisoner!

A jail has n prisoners sitting in a circle, numbered from 1 to n.

There are m sweets to distribute. Distribution starts from chair s, and sweets are given one by one in order around the circle.

The last sweet is bad, so you must determine which prisoner gets it.

🎯 Output

For each test case, print the chair number of the prisoner who receives the last sweet.

🧠 Logic

Use modulo to avoid simulation:

result
( 𝑠 + 𝑚 − 2 )   m o d   𝑛 + 1 result=(s+m−2)modn+1 🧪 Sample Input 2 5 2 1 5 2 2 ✅ Sample Output 2 3


---->>>>..Minimum distance to target element
Implemented an efficient solution to find the minimum distance between a target element and a given start index in an array.
Developed using Java with a focus on clean and optimized logic.
Utilized linear traversal to identify all occurrences of the target value.
Applied mathematical computation using absolute difference to calculate distances.
Ensured optimal performance with O(n) time complexity.
Handled edge cases such as multiple occurrences of the target element.
Used built-in functions like Math.min() and Math.abs() for accuracy and efficiency.
Designed a simple and readable method structure for easy understanding and maintenance.
Demonstrated problem-solving skills in array manipulation and algorithm design.
Suitable for competitive programming and coding interview practice scenarios

----->>>>Minimum distance travel 
Implemented an optimized solution to minimize total travel distance between robots and factories.
Developed using Java with Dynamic Programming (DP) and recursion with memoization.
Sorted robot positions and factory data to ensure efficient processing.
Designed a 2D DP array to store intermediate results and avoid recomputation.
Applied recursive decision-making to either skip or assign robots to factories.
Handled factory capacity constraints while assigning multiple robots.
Used greedy accumulation of distance cost for optimal assignment.
Achieved efficient time complexity by reducing overlapping subproblems.
Incorporated built-in methods like Collections.sort() and Arrays.sort().
Demonstrated strong problem-solving skills in DP, optimization, and real-world logistics scenarios

------>>>.Shortest distance to ttarget
Developed a Java-based solution to find the shortest distance between a target element and a given start index in an array.
Implemented a linear search approach to traverse the array efficiently.
Calculated distances using absolute difference between indices.
Used Math.min() to track and update the minimum distance dynamically.
Ensured optimal time complexity of O(n) for fast execution.
Handled cases with multiple occurrences of the target element.
Designed a clean and simple function for easy readability and maintenance.
Focused on accurate and efficient computation with minimal space usage.
Suitable for coding interviews and competitive programming practice.
Demonstrated strong understanding of array manipulation and basic algorithms.


----->>..Box.it
This project implements a Box class in C++ demonstrating object-oriented programming concepts.
It includes constructors such as default, parameterized, and copy constructor.
The class encapsulates dimensions: length, breadth, and height as private members..
Getter functions are provided to access each dimension safely.
A function is implemented to calculate the volume of the box.
Operator overloading is used to compare two boxes using the < operator.
The << operator is overloaded to print box dimensions in a clean format.
The program processes multiple queries to perform operations on boxes.
It supports creating, copying, comparing, and displaying box details dynamically.
This project is useful for understanding classes, encapsulation, and operator overloading in C++.
It supports operations like creating, updating, comparing, copying, and printing boxes.
The design ensures clean encapsulation and modular code structure.
Input-driven execution makes it suitable for competitive programming practice.


--->>>HACKERRANK 15 : CIRCULAR ARRAY ROTATION
Given an array of integers, perform right circular rotation k times. In one rotation, the last element moves to the front. After performing all rotations, answer q queries. Each query asks: what is the value at index i in the rotated array? 📥 Input n k q array elements queries (each on new line) 📌 Example Input 3 2 3 1 2 3 0 1 2

🔄 Step 1: Perform Rotations

Initial array:

[1, 2, 3]

After 1 rotation:

[3, 1, 2]

After 2 rotations:

[2, 3, 1] 🔍 Step 2: Answer Queries Query Index Value 0 2 1 3 2 1 📤 Output 2 3 1 💡 Optimized Logic (No Rotation Needed)

Instead of rotating, use:

index = (q - k + n) % n

HACKERRANK 16 : SEQUENCE EQUATION
Given a permutation p of size n, for each x from 1 to n, find y such that:

p[p[y]] = x

Return all values of y. Input: p = [2, 3, 1] Output: 2 3 1 ⏱ Complexity Time: O(n) Space: O(n)

We want:

p[p[y]] = x

Break it:

Let

p[y] = k

Then:

p[k] = x

So:

First find k such that p[k] = x Then find y such that p[y] = k 💡 Key Idea (Position Array)

Create an array:

pos[value] = index of that value in p

Now:

k = pos[x] (because p[k] = x) y = pos[k] (because p[y] = k)

👉 So:

y = pos[pos[x]] 🧪 Full Example Input: p = [4, 3, 5, 1, 2] Step 1: Build pos[] value index 1 4 2 5 3 2 4 1 5 3

So:

pos = [_, 4, 5, 2, 1, 3] Step 2: Compute for each x x pos[x] pos[pos[x]] y 1 4 1 1 2 5 3 3 3 2 5 5 4 1 4 4 5 3 2 2 ✅ Output: 1 3 5 4 2 ⚡ Why This Works Fast

Instead of searching every time:

We precompute positions Then each answer is O(1) ⏱ Complexity Time: O(n) Space: O(n)

HACKERRANK 17 : Jumping on the Clouds: Revisited
Jumping on the Clouds: Revisited (HackerRank)

A character is playing a cloud game.

You are given:

An array c[] where: 0 → cumulus cloud (safe) 1 → thundercloud (danger) An integer k (jump size)

The character:

Starts at index 0 with energy = 100

Jumps in steps of k using circular indexing:

(i + k) % n 🔹 Rules Each jump → -1 energy If landing on thundercloud → extra -2 energy Game ends when character returns to index 0 🔹 Task

Return the final energy level.

🔹 Example

Input:

c = [0,0,1,0,0,1,1,0], k = 2

Output:

92

HACKERRANK 19 : EXTRA LONG FACTORIALS
HackerRank Question: Extra Long Factorials The factorial of an integer n, written as n!, is defined as: n! = n × (n − 1) × (n − 2) × ... × 2 × 1 Example: 5! = 5 × 4 × 3 × 2 × 1 = 120 🎯 Task: Calculate and print the factorial of a given integer n. 📥 Function Description: Complete the function:
extraLongFactorials(int n) It should compute and print the factorial of n. 📌 Input Format: A single integer n 📌 Constraints: Factorials can be very large (bigger than long can store) 📤 Output Format: Print the factorial of n 🧪 Sample Input: 25 🧪 Sample Output: 15511210043330985984000000


HACKERRANK 20: APPEND AND DELETE
Problem: Append and Delete

You are given two strings s and t consisting of lowercase English letters, and an integer k.

You can perform the following operations on string s:

Append a lowercase English letter to the end of the string. Delete the last character of the string. If the string is empty, deleting still results in an empty string. 🎯 Task

Determine whether it is possible to convert string s into string t using exactly k operations.

📥 Input First line: string s (initial string) Second line: string t (target string) Third line: integer k (number of operations) 📤 Output Print "Yes" if it is possible Otherwise, print "No" 🧾 Example Input: hackerhappy hackerrank 9 Output:Yes

HACKERRANK 21: SHERLOCK AND SQUARES
Problem: Sherlock and Squares

Sherlock and Squares

Watson likes to challenge Sherlock's math ability. He gives Sherlock a starting value and an ending value that define a range of integers (inclusive).

Sherlock must determine how many square integers exist within that range.

📌 Definition

A square integer is a number that is the square of an integer.

Examples:

1 = 1 2 1 2 4 = 2 2 2 2 9 = 3 2 3 2 16 = 4 2 4 2 🧾 Function Description

Complete the function:

static int squares(int a, int b) Parameters: a: lower bound (inclusive) b: upper bound (inclusive) Returns: An integer → number of perfect squares between a and b 📥 Input Format First line: integer q (number of test cases) Next q lines: each contains two integers a and b 📤 Output Format For each test case, print the number of square integers in the range 🔢 Constraints 1 ≤ 𝑞 ≤ 100 1≤q≤100 1 ≤ 𝑎 ≤ 𝑏 ≤ 10 9 1≤a≤b≤10 9 🧪 Sample Input 2 3 9 17 24 ✅ Sample Output 2 0 📖 Explanation Test Case 1: (3, 9)

Square numbers in range:

4 ( 2 2 2 2 ) 9 ( 3 2 3 2 )

→ Total = 2

Test Case 2: (17, 24)

No perfect squares in this range

→ Total = 0

🎯 Goal Efficiently count how many numbers between a and b are perfect squares.

HACKERRANK 22: LIBRARY FINE
Problem: Library Fine (Advanced Version)

A library charges fines based on how late a book is returned.

💰 Fine Rules: If returned after the due year → fine = 12000 Else if returned in the same year but after the due month → fine = 400 × number of months late Else if returned in the same month and year but after the due day → fine = 20 × number of days late If returned on time or early → fine = 0 📥 Input

Two lines:

d1 m1 y1 (return date) d2 m2 y2 (due date) 📤 Output

Print the total fine.

🧪 Example Input: 10 7 2022 5 7 2022 Output: 100 Explanation: Same month & year 5 days late → 5 × 20 = 100 🧠 Your Task

👉 Write a function like:

int calculateFine(int d1, int m1, int y1, int d2, int m2, int y2) 🔥 Challenge Twist
After solving, try this:

👉 Add a rule:

Maximum fine = 5000 🎯 Goal You should be able to instantly think: Year > Month > Day (priority order)

HACKERRANK 23: CUT THE STICKS
Cut the Sticks – Problem Statement

You are given an array of integers representing the lengths of sticks.

🔁 Task:

Perform the following operation repeatedly until no sticks remain:

ind the shortest stick length Cut that length from all sticks Remove sticks that become 0 length Before each cut, print the number of sticks present 📥 Input Integer n → number of sticks Array arr → stick lengths 📤 Output Print number of sticks before each iteration 📌 Example Input: 6 5 4 4 2 2 8 Output: 6 4 2 1 💡 Explanation Start with 6 sticks Cut smallest (2) → 4 sticks remain Cut again → 2 sticks remain Cut again → 1 stick Done 🎯 Goal Return a list of integers showing how many sticks remain before each cut

---->>> Minimum Operations to Make a Uni-Value Grid:
Each operation consists of adding or subtracting a fixed value x to any element.
The solution flattens the grid into a single list and sorts it.
The median value is chosen as the target to minimize total operations.
For each element, the difference from the target is checked.
If the difference is not divisible by x, the task is impossible.
Otherwise, operations are counted as (difference / x) for each element.
The total number of operations is returned as the final result.
Time complexity is efficient due to sorting and linear traversal.
This approach ensures optimal transformation with minimal cost.

--->>>HACKERRANK 24: NON DIVISIBLE SUSBET
Problem (Non-Divisible Subset – HackerRank)

Given:

Array s Integer k

👉 Find the maximum subset size such that:
(a + b) % k ≠ 0 for any pair 💡 Final Approach (Short) Count frequency of remainders: freq[i] = count of numbers with remainder i Add: 1 if freq[0] > 0 For i = 1 → k/2: If i == k - i → add 1 Else → add max(freq[i], freq[k - i]) 📌 Sample Input: 4 3 1 7 2 4 Output: 3 🔥 Final One-Line Concept

Use remainders and never pick both r and k-r.

HACKERRANK 25: REPEATED STRING
Repeated String – Problem Statement

There is a string s consisting of lowercase English letters. This string is repeated infinitely many times.

You are given a number n. Your task is to find how many times the letter 'a' appears in the first n characters of the infinitely repeated string.


📥 Input A string s A long integer n 📤 Output Return a long integer representing the count of 'a' in the first n characters 🔍 Example 1

Input:

s = "aba" n = 10

Explanation: Infinite string → abaabaabaa... First 10 characters → abaabaabaa Number of 'a' → 7

Output:

7 🔍 Example 2
nput:

s = "a" n = 1000000000000

Output:

1000000000000 ⚠️ Constraints 1 ≤ ∣ 𝑠 ∣ ≤ 100 1≤∣s∣≤100 1 ≤ 𝑛 ≤ 10 12 1≤n≤10 12

HACKERRANK 26: JAVA STRINGS DOCUMENTATION
HackerRank – Java Strings Introduction

A string is a sequence of characters.

You are given two strings A and B consisting of lowercase English letters.

🔹 Your task is to perform 3 operations: 1️⃣ Sum of lengths

Print the sum of the lengths of string A and B.


2️⃣ Lexicographical comparison

Check if string A is lexicographically greater than B.

👉 If A > B, print:

Yes

Otherwise print:

No 3️⃣ Capitalization
Capitalize the first letter of both strings and print them on one line separated by a space.

📥 Input Format A B First line → string A Second line → string B 📤 Output Format (sum of lengths) Yes/No Capitalized A + space + Capitalized B ✅ Example Input: hello java Output: 9 No Hello Java


---->>CLASS SOLUTION
.This project implements a solution to count “good numbers” after digit rotation.
A number is considered valid if it remains a number after rotation and changes to a different number.
Digits 0, 1, and 8 remain the same, while 2, 5, 6, and 9 transform into other digits.
Digits 3, 4, and 7 invalidate the number when rotated.
The function iterates from 1 to n and checks each number individually.
Each digit is processed using modulo and integer division operations.
A flag ensures the number contains at least one transforming digit.
Another flag ensures no invalid digits are present.
Valid transformed numbers are counted and returned as the result.
This solution is simple, efficient, and suitable for beginner-level problem solving

HACKERRANK 28: JAVA STRING TOKEN
Problem: Java String Tokens 📌 Problem Statement

Given a string s, split it into tokens. A token is defined as a sequence of one or more English alphabetic letters.

Print:

Total number of tokens Each token on a new line 🔹 Input
A single line string s

He is a very very good boy, isn't he? 🔹 Output 10 He is a very very good boy isn t he ⚙️ Constraints String contains letters + special characters: ! , ? . _ ' @ and spaces 💡 Hint

Split using:

[^A-Za-z]+

🧠 Key Concept

👉 Token = only letters 👉 So remove everything else
✔️ Split by:

[^A-Za-z]+ 🚀 Quick Trick

👉 “Keep letters → break at non-letters” String:

H e l l o w o r l d 0 1 2 3 4 5 6 7 8 9

From index 3 to 7, the substring is:

lowo

HACKERRANK 28: JAVA STRING TOKEN
Problem: Java String Tokens 📌 Problem Statement

Given a string s, split it into tokens. A token is defined as a sequence of one or more English alphabetic letters.

Print:

Total number of tokens Each token on a new line 🔹 Input

A single line string s

He is a very very good boy, isn't he? 🔹 Output 10 He is a very very good boy isn t he ⚙️ Constraints String contains letters + special characters: ! , ? . _ ' @ and spaces 💡 Hint
Split using:

[^A-Za-z]+

🧠 Key Concept

👉 Token = only letters 👉 So remove everything else

✔️ Split by:

[^A-Za-z]+ 🚀 Quick Trick

👉 “Keep letters → break at non-letters” String:

H e l l o w o r l d 0 1 2 3 4 5 6 7 8 9

From index 3 to 7, the substring is:

lowo

HACKERRANK 29: PATTERN SYNTAX CHECKER
Problem: Pattern Syntax Checker

Using regular expressions (regex), we can match patterns in text. Before using a regex, we must ensure that its syntax is valid.

📌 Task

You are given several strings representing regex patterns. For each pattern:

Print "Valid" if the regex syntax is correct Print "Invalid" if the regex syntax is incorrect

👉 A regex is considered valid if it can be successfully compiled using:

Pattern.compile(pattern) 📥 Input Format First line contains an integer T → number of test cases Next T lines each contain a string → the regex pattern 📤 Output Format

For each test case:

Print "Valid" or "Invalid" on a new line 🔢 Constraints 1 ≤ T ≤ 100 Pattern consists of printable ASCII characters

Print "Valid" or "Invalid" on a new line 🔢 Constraints 1 ≤ T ≤ 100 Pattern consists of printable ASCII characters 🧪 Sample Input 3 ([A-Z])(.+) [AZa-z batcatpat(nat ✅ Sample Output Valid Invalid Invalid 💡 Explanation ([A-Z])(.+) → correct grouping → ✅ Valid [AZa-z → mismatched brackets → ❌ Invalid batcatpat(nat → missing ) → ❌ Invalid

HACKERRANK 30 : JAVA REGEX
Problem: Validate Floating Point Number

Write a regular expression to check whether a given string is a valid floating point number.

A valid floating point number:

May be positive or negative May contain digits before and/or after decimal point Must contain at least one digit Decimal point . is optional ✅ Valid Examples 12.34 -12.34 0.5 .25 10 -0.99 ❌ Invalid Examples . abc 12. --12.3 12..34 🔹 Input Format


Multiple lines of input, each containing a string.

🔹 Output Format

For each input, print:

true

or

false 🔹 Constraints String may contain any ASCII characters

HACKERRANK 31: REGEX SUPLICATE WORD REMOVAL
Problem Summary

You are given N sentences. For each sentence, remove duplicate words such that:

Matching is case-insensitive Only the first occurrence of each word is kept The final output must preserve the original casing of the first occurrence 📥 Input Format First line: Integer N → number of sentences Next N lines: Each line contains a sentence 📤 Output Format Print each sentence after removing repeated words 🔒 Constraints Sentences contain only: English letters (a–z, A–Z) Whitespaces Length is within reasonable bounds 🔍 Approach

We solve this using Regular Expressions (RegEx) with backreferences.

✅ Step 1: Match Repeated Words

Use this regex:

"\b(\w+)(\b\W+\b\1\b)+" 🔎 Explanation \b → word boundary (\w+) → captures a word → Group 1 ( ... )+ → matches repeated occurrences \1 → refers to the same word captured before

👉 This matches patterns like:
"to To tO" "bye bye bye" ✅ Step 2: Case-Insensitive Matching Pattern.CASE_INSENSITIVE

👉 Ensures:

"Hello hello" → duplicate "Ab aB" → duplicate ✅ Step 3: Replace Duplicates input.replaceAll(m.group(), m.group(1)); 🔎 Meaning

m.group() → entire matched sequence

"to To tO"

m.group(1) → first word

"to"

👉 Replace full sequence with first occurrence

🔁 Algorithm Flow

For each sentence:

Create matcher using regex Find duplicate word sequences Replace them with first occurrence Repeat until no duplicates remain 🧪 Sample Walkthrough Input 1 Hello hello Ab aB Matching "Hello hello" → duplicate "Ab aB" → duplicate Output Hello Ab ⚠️ Important Notes Do NOT change original structure of code Only fill: Regex Pattern flag replaceAll arguments Matching must be case-insensitive Output must preserve original casing of first word 🎯 Final Code Snippet String regex = "\b(\w+)(\b\W+\b\1\b)+"; Pattern p = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);

while (m.find()) { input = input.replaceAll(m.group(), m.group(1)); }

HACKERRANK 32: STRING STREAM
Problem: Parse Comma-Separated Integers (StringStream)

You are given a string containing integers separated by commas. Your task is to extract these integers and store them in a vector.

Function Signature vector parseInts(string str); Input A single string str consisting of integers separated by commas. Example: "23,4,56" Output Return a vector of integers parsed from the string. Each integer should be printed on a new line. Example


Input:

23,4,56

Output:

23 4 56 Explanation The input string contains numbers separated by commas. You need to split the string and convert each number into an integer. Constraints The length of the string is less than 1000. All values in the string are valid integers.

HACKERRANK 33: STRINGS CPP
Question

You are given two strings a and b, consisting of lowercase English letters.

Perform the following operations:

Print the length of string a and string b, separated by a space. Print the concatenation of a and b. Swap the first characters of both strings and print the modified strings separated by a space. 📥 Input Format First line: string a Second line: string b 📤 Output Format Line 1: Length of a and b Line 2: Concatenated string Line 3: Modified strings after swapping first characters 🧪 Sample Input abcd ef ✅ Sample Output 4 2 abcdef ebcd af

---->>>>Jump Game IX 
It is a Java-based array processing problem solution.
The program uses prefix maximum and suffix minimum concepts.
A Solution class is implemented with the maxValue() method.
Prefix array stores the maximum value from the left side.
Suffix array stores the minimum value from the right side.
The algorithm compares prefix and suffix values efficiently.
Result values are stored in a separate result array.
The solution works in linear time complexity O(n).
The program is optimized for efficient array traversal operations.
The final output returns an integer array with computed maximum values.

HACKERRANK 34: JUMPING ON THE CLOUDS
Jumping on the Clouds (HackerRank)

There is a game with clouds placed in a line.

Each cloud is either:

0 → safe (you can land here) 1 → thunderhead (you must avoid) 🎯 Goal

Starting from the first cloud (index 0), reach the last cloud in the minimum number of jumps.

🪜 Rules You can jump: 1 step forward, or 2 steps forward You can only land on clouds with 0 It is guaranteed that reaching the end is always possible 📥 Input An integer n → number of clouds An array c of size n containing only 0s and 1s 📤 Output Return the minimum number of jumps needed to reach the last cloud 📌 Example Input: n = 7
c = [0, 0, 1, 0, 0, 1, 0] Explanation:

Avoid indices with 1 → (2 and 5)

Possible paths:

0 → 1 → 3 → 4 → 6 (4 jumps) ✅ 0 → 2 ❌ (not allowed) Output: 4 📌 Another Example Input: n = 6
c = [0, 0, 0, 0, 1, 0] Output: 3

HACKERRANK 35: EQUALIZE THE ARRAY
Equalize the Array (HackerRank)

Given an array of integers, determine the minimum number of elements to delete so that all remaining elements are equal.

📥 Input An integer n — size of the array An array arr of n integers 📤 Output Return an integer representing the minimum deletions required 📌 Example

Input:

n = 5 arr = [3, 3, 2, 1, 3]

Output:

2
Explanation:

The number 3 appears most frequently (3 times) Remove 2 and 1 Remaining array → [3, 3, 3] 🔒 Constraints 1 ≤ 𝑛 ≤ 100 1≤n≤100 1 ≤ 𝑎 𝑟 𝑟 [ 𝑖 ] ≤ 100 1≤arr[i]≤100 💡 Key Idea

Keep the most frequent element and delete all others.

HACKERRANK 36: VALID USERNAME REGULAR EXPRESSION
Valid Username Regular Expression 📌 Problem Summary

You are given a list of usernames. For each username, determine whether it is Valid or Invalid based on the rules below.

📏 Valid Username Rules

A username is considered valid if:
Length Constraint The username must contain 8 to 30 characters (inclusive)
Allowed Characters The username can only contain: Lowercase letters: a–z Uppercase letters: A–Z Digits: 0–9 Underscore: _
First Character Rule The first character must be an alphabet (a–z or A–Z) ❌ Invalid Cases
A username is invalid if:

Length < 8 or > 30 Contains characters other than [a-zA-Z0-9_] Starts with a digit or underscore 🧠 Approach

Instead of checking each rule separately, use a regular expression to enforce all rules at once.

✅ Regular Expression ^[a-zA-Z][a-zA-Z0-9_]{7,29}$ 🔍 Explanation of Regex Part Meaning ^ Start of string [a-zA-Z] First character must be a letter [a-zA-Z0-9_] Allowed characters {7,29} Remaining length (total = 8–30) $ End of string 💻 Implementation class UsernameValidator { public static final String regularExpression = "^[a-zA-Z][a-zA-Z0-9_]{7,29}$"; } 📌 Example Input 8 Julia Samantha Samantha_21 1Samantha Samantha?10_2A JuliaZ007 Julia@007 _Julia007 Output Invalid Valid Valid Invalid Invalid Valid Invalid Invalid 🎯 Key Insight

👉 Convert all conditions into a single regex pattern instead of writing multiple checks.

HACKERRANK 37: BOX IT!
Problem: Box It!

Design a class named Box whose dimensions are integers and private to the class. The dimensions are:

length (l) breadth (b) height (h) 🔧 Requirements

Constructors Box() → Initializes l = b = h = 0 Box(int l, int b, int h) → Initializes the box with given dimensions Box(Box B) → Copy constructor (copies dimensions from another box)
Member Functions int getLength() → returns length int getBreadth() → returns breadth int getHeight() → returns height long long CalculateVolume() → returns volume of box
Operator Overloading 🔹 Overload < operator
A box A is considered less than box B if:

A.l < B.l OR if A.l == B.l AND A.b < B.b OR if A.l == B.l, A.b == B.b AND A.h < B.h 🔹 Overload << operator

Printing a box should display:

l b h

(on a single line, space-separated)


🧪 Input Format First line: integer n (number of operations) Next n lines: each contains a query of type: Type Operation 1 Print current box 2 l b h Create new box and assign to current 3 l b h Compare new box with current 4 Print volume of current box 5 Copy current box and print 📌 Example

Input:

5 2 2 3 4 1 4 5 3 3 4 5

Output:

2 3 4 2 3 4 24 2 3 4 Greater ⚠️ Constraints Dimensions are integers No two boxes compared will have all dimensions equal

HACKERRANK 38: STRUCTS
Problem: Structs (HackerRank)

In C++, a structure (struct) is a way to group variables of different types under a single name.

You are required to define a structure named Student that contains the following fields:

age (integer) first_name (string) last_name (string) standard (integer) 📥 Input Format

Input consists of 4 lines
Integer → age String → first_name String → last_name Integer → standard 📤 Output Format

Print all the values in a single line separated by spaces:

age first_name last_name standard 📌 Sample Input 15 john carmack 10 📌 Sample Output 15 john carmack 10


HACKERRANK 39: TAG CONTENT EXTRACTOR
Problem: Tag Content Extractor

In a tag-based language like XML or HTML, contents are enclosed between a start tag and an end tag:

content

The end tag always starts with /, and the tag names must match.

📌 Task

Given multiple lines of text containing tag-based expressions, extract and print the content enclosed within valid matching tags.

✅ Rules The start tag and end tag must have the same name ❌

HACKERRANK 40:JAVA BIG DECIMAL
Question (Java BigDecimal – HackerRank)

Given an array s of real number strings, sort the array in descending numerical order using Java’s BigDecimal class.

🔹 Important Conditions: Do not change the original format of the numbers Example: "02.34" should remain "02.34" Example: ".12" should remain ".12" If two numbers are numerically equal, keep them in the same order as input (stable sorting). 🔹 Input Format: First line: integer n (size of array) Next n lines: real number strings 🔹 Output: Print the sorted array in descending order 🔹 Example:

Input:

9 -100 50 0 56.6 90 0.12 .12 02.34 000.000

Output:

90 56.6 50 02.34 0.12 .12 0 000.000 -100

HACKERRANK 41: CLASS IN CPP (STUDENT CLASS)
Problem: Class in C++ (Student Class)

Create a class named Student to store student details:

age (int) first_name (string) last_name (string) standard (int) ⚙️ Requirements Make all data members private. Create public getter and setter functions for each variable: get_age(), set_age() get_first_name(), set_first_name() get_last_name(), set_last_name() get_standard(), set_standard()

Implement a function:

string to_string();

It should return a string in this format:

string to_string();

It should return a string in this format:

age,first_name,last_name,standard 📥 Input age first_name last_name standard 📤 Output

The main function will:

Print age Print last name, first name Print standard Print formatted string 🧪 Example

Input

15 john carmack 10

Output 15 carmack, john 10 15,john,carmack,10

HACKERRANK 42: JAVA PRIMALITY TEST
Java Primality Test

A prime number is a natural number greater than 1 whose only positive divisors are 1 and itself.

📝 Problem

Given a large integer n, determine whether it is prime or not prime using Java’s BigInteger class.

📥 Input Format A single line containing an integer n 📤 Output Format Print: "prime" → if the number is prime "not prime" → otherwise 📌 Constraints The number n can have up to 100 digits 📊 Example

Input

13

Output

prime 💡 Explanation 13 has only two divisors: 1 and 13 So, it is a prime number 🎯 Requirement You must use Java’s BigInteger.isProbablePrime() method

HACKERRANK 43: CLASSES AND OBJECTS
Classes and Objects (HackerRank)

A class defines a blueprint for objects. You are required to implement a class to help compare student scores.

Kristen wants to know how many students scored higher than her in the exams this semester.

📌 Task
Create a class named Student with the following:

Data Member vector scores → stores 5 exam scores Member Functions void input() Reads 5 integers from input Stores them in scores int calculateTotalScore() Returns the sum of all scores 📥 Input Format First line: integer n → number of students Next n lines: each contains 5 integers (scores of a student) 📤 Output Format Print the number of students who scored strictly higher total marks than Kristen 🧠 Important Notes Kristen is the first student (index 0) Compare all other students with her total score 🧪 Sample Input 3 30 40 45 10 10 40 40 40 10 10 50 20 30 10 10 ✅ Sample Output 1 🔍 Explanation Kristen’s total = 30 + 40 + 45 + 10 + 10 = 135 Only one student has a higher total → output = 1

HACKERRANK 44: JAVA BIGINTEGER
Java BigInteger

In this problem, you have to add and multiply huge numbers! These numbers are so big that you can't contain them in any ordinary data types like a long integer.

Use the power of Java's BigInteger class and solve this problem.

Input Format

There will be two lines containing two numbers:

The first line contains integer a The second line contains integer b Constraints a and b are non-negative integers Each number can have up to 200 digits Output Format

Print two lines:
First line: a + b Second line: a × b

Do not print any leading zeros.

Sample Input 1234 20 Sample Output 1254 24680


Hacker45: Jva integer
print two lines


HACKERRANK 45: INHERITED CODE
Inherited Code (HackerRank)

You are given a piece of inherited code that validates usernames for a website.

The function checkUsername(string username):

Throws an exception if the username length is less than 5 Returns: true → if valid false → if invalid (contains "ww" as consecutive characters)

However, the exception BadLengthException is not defined.

🎯 Your Task

Define the class:

BadLengthException

such that:

It stores the length of the username When caught, calling what() returns the length as a string 📥 Input Format First line: integer T (number of test cases) Next T lines: each contains a username string 📤 Output Format

For each test case, output:
For each test case, output:

"Valid" → if username is valid "Invalid" → if username contains "ww" "Too short: n" → if length < 5 (where n is length) 📌 Constraints Username contains only English letters 1 ≤ T ≤ ? (typical constraint) 1 ≤ length(username) 🧪 Sample Input 3 Peter Me Arxwwz ✅ Sample Output Valid Too short: 2 Invalid 💡 Explanation "Peter" → length ≥ 5, no "ww" → Valid "Me" → length = 2 → Exception → Too short: 2 "Arxwwz" → contains "ww" → Invalid

HACKERRANK 46: EXCEPTIONAL SERVER
Problem: Exceptional Server (C++)

You are given a server that performs computations using a function:

static int compute(long long A, long long B);

This function may throw different types of exceptions depending on the input.

🎯 Your Task
For each test case:

Call Server::compute(A, B) Handle exceptions and print the correct message: 📌 Expected Behavior Situation Output Function runs successfully Print result Memory allocation fails (bad_alloc) Not enough memory Standard exception (exception) Exception: Any other exception Other Exception 📥 Input Format First line: integer T (number of test cases) Next T lines: two integers A and B 📤 Output Format For each test case, print the appropriate message After all test cases, print server load using: Server::getLoad() 🧪 Sample Input 2 -8 5 1435434255433 5 ✅ Sample Output Exception: A is negative Not enough memory

HackerRank 46— Java Method Overriding

When a subclass inherits from a superclass, it also inherits its methods. However, the subclass can override inherited methods to provide its own implementation.

Consider the following class:

class Sports {
    String getName() {
        return "Generic Sports";
    }

    void getNumberOfTeamMembers() {
        System.out.println("Each team has n players in " + getName());
    }
}

Now consider a subclass:

class Soccer extends Sports {
    @Override
    String getName() {
        return "Soccer Class";
    }
}
Task

Complete the Soccer class by writing an overridden getNumberOfTeamMembers() method.

The method should print the same message as the superclass method, except it should replace n with 11, since a soccer team has 11 players.

Expected Output
Generic Sports
Each team has n players in Generic Sports
Soccer Class
Each team has 11 players in Soccer Class
Function to Complete
class Soccer extends Sports {
    @Override
    String getName() {
        return "Soccer Class";
    }

    // Write your overridden getNumberOfTeamMembers method here
}

HACKERRANK 47: JAVA 1D ARRAY
Question: Java 1D Array

You are given an integer n, which represents the size of an array. Then you are given n integers, each on a new line.

Your task: Create an array a of size n. Read the n integers from input. Store each integer in the array at its correct index. First value → a[0] Second value → a[1] and so on… Note:
You do not need to print anything — the given code already prints the array elements.

Example Input: 5 10 20 30 40 50 Example Output: 10 20 30 40 50

HACKERRANK 48: JAVA 2D ARRAY
Problem: Java 2D Array (Hourglass)

You are given a 6×6 2D array of integers. You need to find the maximum hourglass sum.

🔍 What is an Hourglass?

An hourglass is a subset of values with indices forming this pattern:

a b c d e f g 🎯 Task
Calculate the maximum sum of any hourglass in the given 6×6 array.

📥 Input Format There are exactly 6 lines of input Each line contains 6 space-separated integers Each integer is in the range -9 to 9 📤 Output Format Print a single integer → the maximum hourglass sum ✅ Sample Input 1 1 1 0 0 0 0 1 0 0 0 0 1 1 1 0 0 0 0 0 2 4 4 0 0 0 0 2 0 0 0 0 1 2 4 0 ✅ Sample Output 19 💡 Explanation

The hourglass with the largest sum is:
### HACKERRANK 48: JAVA SUBARRAY

Java Subarray – Problem Statement

A subarray of an array is a sequence of contiguous elements from the array.

For example, if the array is:

[1, -2, 4]

Then valid subarrays are:

[1], [1, -2], [1, -2, 4], [-2], [-2, 4], [4] 📌 Task

Given an array of integers, find the number of subarrays whose sum is negative.

📥 Input Format First line: An integer n (size of array) Second line: n space-separated integers 📤 Output Format Print a single integer → number of subarrays having negative sum 🔒 Constraints 1 ≤ n ≤ 100 -10^4 ≤ arr[i] ≤ 10^4 🧪 Example

Input:

5 1 -2 4 -5 1

Output:

9 🧠 Explanation There are 9 subarrays whose total sum is negative.

2 4 4 2 1 2 4

Sum(addition) = 19

!!Constraints Array size is fixed: 6 × 6 Values range: -9 ≤ arr[i][j] ≤ 9
### HACKERRANK 49: import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            int x = sc.nextInt();
            int y = sc.nextInt();

            System.out.println(x / y);
        }
        catch (InputMismatchException e) {
            System.out.println("java.util.InputMismatchException");
        }
        catch (ArithmeticException e) {
            System.out.println(e);
        }
    }
}
### HACKERRANK 50: Messages Order
Problem Statement

In a messaging system, messages are sent from a sender to a recipient through a network. The network does not guarantee that messages will arrive in the same order in which they were sent. For example, if the sender sends:

hello
hi
what's up

the recipient might receive them as:

what's up
hello
hi

Your task is to implement the classes Message and MessageFactory so that the recipient can restore the original order of messages before printing them.

Requirements
Class Message
Store a text message of type string.
Provide the method:
const string& get_text()

which returns the stored text.

Overload the < operator so that messages can be sorted into their original sending order.
You may add additional constructors, methods, or data members as needed.
An empty constructor must be provided.
Class MessageFactory
Provide an empty constructor.
Implement:
Message create_message(const string& text)

which creates and returns a Message object containing the given text.

You may add additional methods or data members as needed.
Input Format

Several lines of text messages are provided as input in the order they are sent.

Output Format

Print all messages in the same order as they were originally sent.
### HACKERRANK 51: JAVA EXCEPTION HANDLING
HackerRank - Java Exception Handling

You are required to compute the power of a number by implementing a calculator.

Create a class MyCalculator which contains a method:

long power(int n, int p)

The method should return n^p.

Exception Conditions

If either n or p is negative, throw an exception with the message:

n or p should not be negative.

If both n and p are zero, throw an exception with the message:

n and p should not be zero.

The exception should be thrown using:

throw new Exception("message");
Input Format

Each line contains two integers n and p.

Output Format
Print n^p if both values are valid.
Otherwise print the exception message.
Sample Input
3 5
2 4
0 0
-1 -2
-1 3
Sample Output
243
16
java.lang.Exception: n and p should not be zero.
java.lang.Exception: n or p should not be negative.
java.lang.Exception: n or p should not be negative.
Explanation
3^5 = 243
2^4 = 16
(0,0) is invalid → throw exception.
Negative values are invalid → throw exception.

Task: Complete the power(int n, int p) method in the MyCalculator class.

Sample Input
Alex
Hello Monique!
What'up?
Not much :(
Sample Output
Alex
Hello Monique!
What'up?
Not much :(
Key Idea

Since the network can shuffle messages, assign a sequence number (ID) to every message when it is created. Store this ID in the Message object and implement operator< to compare IDs. When the recipient sorts the received messages, they will be restored to the original sending order.

Difficulty: Easy–Medium
Concepts Used: Classes, Constructors, Operator Overloading, Sorting, OOP in C++
### HackerRank 52: Java Varargs - Simple Addition

You are given a class Solution and its main method.

Your task is to create a class Add with a method add that can accept a variable number of integer arguments and print their sum in the following format:

num1+num2+...+numN=sum
Input

Six integers are provided as input, one per line.

Output

The main method will call your add method four times:

ob.add(n1,n2);
ob.add(n1,n2,n3);
ob.add(n1,n2,n3,n4,n5);
ob.add(n1,n2,n3,n4,n5,n6);

For each call, print the expression and its sum.

Sample Input
1
2
3
4
5
6
Sample Output
1+2=3
1+2+3=6
1+2+3+4+5=15
1+2+3+4+5+6=21
Important Constraint
You must use Varargs (int...).
Method overloading is not allowed.
The checker will throw an exception if more than one method named add exists.
What You Need to Write

Only the Add class:

class Add {
    public void add(int... nums) {
        // your code here
    }
}

Concept Tested: Java Varargs (int... args) and Reflection (to ensure no overloading).
### HACKERRANK 52: JAVA REFLECTION-ATTRIBUTES
HackerRank Java Reflection - Attributes (Question)

You are given a class Student. Using Java Reflection, print all the method names of the Student class in alphabetical order.

Example Student class:

class Student{
    private String name;
    private String id;
    private String email;

    public String getName() { return name; }
    public void setId(String id) { this.id = id; }
    public void setEmail(String email) { this.email = email; }
    public void anothermethod() { }
}
Expected Output
anothermethod
getName
setEmail
setId
...
Complete the Following Code
import java.lang.reflect.*;
import java.util.*;

public class Solution {

    public static void main(String[] args){
        Class student = ____________;
        Method[] methods = ____________;

        ArrayList<String> methodList = new ArrayList<>();

        for(____________){
            methodList.add(____________);
        }

        Collections.sort(methodList);

        for(String name : methodList){
            System.out.println(name);
        }
    }
}

### HACKERRANK 53: ACCESSING INHERITED FUNCTIONS
Accessing Inherited Functions — Question

You are given three classes A, B, and C. Each class has a protected function func(int &a) that multiplies a by:

A::func() → multiplies by 2
B::func() → multiplies by 3
C::func() → multiplies by 5

Each class also keeps track of how many times its func() is called.

You are also given the following class:

class D
{
    int val;

public:
    D()
    {
        val = 1;
    }

    void update_val(int new_val)
    {
        // Implement this
    }

    void check(int);
};
Task

Modify class D and implement update_val(int new_val) such that:

val is updated from 1 to new_val
You may change val only by calling the inherited func() methods from classes A, B, and C
new_val is guaranteed to have only 2, 3, and 5 as prime factors
Example

Input:

30

Output:

Value = 30
A's func called 1 times
B's func called 1 times
C's func called 1 times

Explanation:

1 × 2 = 2
2 × 3 = 6
6 × 5 = 30

Implement only the update_val() function and necessary inheritance for class D.
### HACKERRANK 54: CAN YOU ACCESS
HackerRank: Can You Access?

You are given a class Solution and an inner class Inner.Private.

The method powerof2(int num) inside Inner.Private checks whether a number is a power of 2.

Your task is to call the method powerof2 of the class Inner.Private from the main method of the class Solution, even though Private is a private inner class.

Constraints
Input consists of a single integer num.
Sample Input
8
Sample Output
8 is power of 2
An instance of class: Solution.Inner.Private has been created
Given Code Skeleton
public class Solution {

    public static void main(String[] args) throws Exception {
        DoNotTerminate.forbidExit();

        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int num = Integer.parseInt(br.readLine().trim());

            Object o; // Must be used to hold the reference of the instance
                      // of the class Solution.Inner.Private

            System.out.println("An instance of class: "
                    + o.getClass().getCanonicalName()
                    + " has been created");

        } catch (DoNotTerminate.ExitTrappedException e) {
            System.out.println("Unsuccessful Termination!!");
        }
    }

    static class Inner {
        private class Private {
            private String powerof2(int num) {
                return ((num & num - 1) == 0)
                        ? "power of 2"
                        : "not a power of 2";
            }
        }
    }
}
What You Need to Learn

This problem tests:

Inner Classes
Private Inner Classes
Java Reflection
Accessing private methods using:
getDeclaredMethod()
setAccessible(true)
invoke()

Difficulty: Easy-Medium (Java Reflection)
### HACKERRANK 55: PRIME CHECKER
HackerRank – Prime Checker

You are given a class Solution and its main method. Your task is to create a class Prime.

The class Prime should contain a single method:

checkPrime

The locked code will call checkPrime with one or more integer arguments. Your method should print only the prime numbers among the given arguments.

Requirements
Create a class Prime.
Implement only one method named checkPrime.
Do not use method overloading.
The method should accept a variable number of arguments.
Print all prime numbers passed to the method, separated by spaces.
If no prime number exists among the arguments, print a blank line.
Note

The editor contains the line:

BufferedReader br = new BufferedReader(new InputStreamReader(in));

which may cause a compile-time error. You must identify and fix it.

Input Format

There are five lines of input, each containing one integer.

Output Format

There will be four lines of output. Each line contains the prime numbers from the arguments passed to checkPrime by the main method.

Sample Input
2
1
3
4
5
Sample Output
2
2
2 3
2 3 5
### HACKERRANK 56: MAGIC SPELLS
HackerRank – Magic Spells (Question)

While playing a video game, you are battling a powerful dark wizard. He casts spells from a distance, giving you only a few seconds to react and conjure your counterspells. For a counterspell to be effective, you must first identify what kind of spell you are dealing with.

The wizard uses scrolls to conjure his spells, and sometimes he uses generic spells that restore his stamina. In that case, you can extract the name of the scroll from the spell. Then you need to find out how similar this new spell is to the spell formulas written in your spell journal.

Complete the body of the counterspell function.

Task

For each spell passed to counterspell(Spell *spell):

If the spell is:
Fireball → print its power.
Frostbite → print its power.
Waterbolt → print its power.
Thunderstorm → print its power.
Otherwise, it is a generic Spell.
Get the spell's scroll name using revealScrollName().
Get the journal string using SpellJournal::read().
Find the length of the Longest Common Subsequence (LCS) between the two strings.
Print the LCS length.
Input Format
First line contains an integer T, the number of spells.
For each spell:

If it is a known spell:

fire power
frost power
water power
thunder power

Otherwise:

scrollName power journalString
Output Format

For known spells, print:

Fireball: power
Frostbite: power
Waterbolt: power
Thunderstorm: power
For generic spells, print the length of the LCS on a new line.
Sample Input
3
fire 5
AquaVitae 999 AruTaVae
frost 7
Sample Output
Fireball: 5
6
Frostbite: 7
Explanation
fire 5 → Fireball with power 5.
AquaVitae and AruTaVae have an LCS of length 6.
frost 7 → Frostbite with power 7.
Concepts Used
Inheritance
Runtime Polymorphism
dynamic_cast
Longest Common Subsequence (LCS) using Dynamic Programming
### HACKERRANK 57: JAVA FACTORY PATTERN 
Java Factory Pattern – Question

According to Wikipedia, a factory is simply an object that returns another object from some other method call, which is assumed to be "new".

In this problem, you are given an interface Food. There are two classes Pizza and Cake which implement the Food interface, and they both contain a method getType().

The main function creates an instance of the FoodFactory class. The FoodFactory class contains a method getFood(String) that returns a new instance of Pizza or Cake according to its parameter.

Task: Complete the FoodFactory class by implementing the getFood(String order) method.

Sample Input 1
cake
Sample Output 1
The factory returned class Cake
Someone ordered a Dessert!
Sample Input 2
pizza
Sample Output 2
The factory returned class Pizza
Someone ordered a Fast Food!
Key Concept

This problem demonstrates the Factory Design Pattern, where an object (the factory) creates and returns instances of other classes based on the input provided.
### HACKERRANK 58: JAVA SINGLETON PATTERN
HackerRank – Java Singleton Pattern

Problem Statement

"The singleton pattern is a design pattern that restricts the instantiation of a class to one object. This is useful when exactly one object is needed to coordinate actions across the system."

Complete the Singleton class in your editor which contains the following components:

A private non-parameterized constructor.
A public String instance variable named str.
A static method named getSingleInstance() that returns the single instance of the Singleton class.

Once submitted, the hidden solution will check your code by taking a String as input and then using your Singleton class to print a line.

Input Format

You will not be handling any input in this challenge.

Output Format

You will not be producing any output in this challenge.

Sample Input
hello world
Sample Output
Hello I am a singleton! Let me say hello world to you
Task

Complete the following class:

class Singleton{

}

so that:

Only one object of Singleton can ever be created.
The object can be accessed using Singleton.getSingleInstance().
The class contains a public String variable str.
### HACKERRANK 59: C++ CLASS TEMPLATES
HackerRank – C++ Class Templates

A class template provides a specification for generating classes based on parameters. Class templates are generally used to implement containers. A class template is instantiated by passing a given set of types to it as template arguments.

Example:

template <class T>
class MyTemplate {
    T element;
public:
    MyTemplate(T arg) { element = arg; }
    T divideBy2() { return element / 2; }
};

It is also possible to define a different implementation of a template for a specific type. This is called Template Specialization.

Example:

template <>
class MyTemplate<char> {
    char element;
public:
    MyTemplate(char arg) { element = arg; }

    char printElement() {
        return element;
    }
};
Task

You are given a main() function which takes a set of inputs.

The type of input determines the operation to be performed:

For int and float, perform addition.
For string, perform concatenation.

You need to write:

A class template AddElements that has a function add() for adding two elements of type int or float.
A template specialization for type string that has a function concatenate() to append the second string to the first string.
Input Format
The first line contains an integer n.
The next n lines contain:
A type (int, float, or string)
Followed by two values of that type.
Constraints
Type will be one of:
int
float
string
String length ≤ 100.
Output Format

The provided code will use your class template to perform the required operation and print the result.

Sample Input
3
string John Doe
int 1 2
float 4.0 1.5
Sample Output
JohnDoe
3
5.5
Explanation
"John" concatenated with "Doe" gives "JohnDoe".
1 + 2 = 3.
4.0 + 1.5 = 5.5.
### HACKERRANK 60: JAVA VISITOR PATTERN
HackerRank – Java Visitor Pattern

An important concept in Object-Oriented Programming is the Open/Closed Principle, which states that software entities should be open for extension but closed for modification. This challenge uses the Visitor Design Pattern to extend functionality without modifying existing tree classes.

A tree implementation is provided with the following classes:

Tree
TreeNode
TreeLeaf
TreeVis

Each tree node has:

getValue() – returns the node's value.
getColor() – returns the node's color (RED or GREEN).
getDepth() – returns the node's depth from the root.

The tree is rooted at node 1.

Part I: Implement Three Visitors

Implement the following visitor classes:

1. SumInLeavesVisitor

Return the sum of values stored in all leaf nodes.

2. ProductOfRedNodesVisitor

Return the product of values stored in all red nodes (including leaves), modulo:

1000000007
3. FancyVisitor

Return the absolute difference between:

Sum of values of non-leaf nodes at even depth
Sum of values of green leaf nodes

That is:

| (sum of non-leaf nodes at even depth)
  - (sum of green leaf nodes) |
Part II: Build the Tree

Read the input and construct the tree.

Input Format
First line: Integer n, the number of nodes.
Second line: n integers representing node values.
Third line: n integers representing node colors:
0 → RED
1 → GREEN
Next n-1 lines:
Two integers u and v
Representing an edge between nodes u and v

The tree is always rooted at node 1.

Constraints
1 ≤ n ≤ 10^5

The tree is guaranteed to be valid and connected.

Sample Input
5
4 7 2 5 12
0 1 0 0 1
1 2
1 3
3 4
3 5
Sample Output
24
40
15
Explanation

Tree:

        4(R)
       /   \
    7(G)   2(R)
           /   \
        5(R) 12(G)
Leaves = 7 + 5 + 12 = 24
Red nodes = 4 × 2 × 5 = 40
Even-depth non-leaf nodes = 4
Green leaves = 7 + 12 = 19
|4 - 19| = 15

Output:

24
40
15
### HACKERRANK 61: PREPROCESSOR SOLUTION
Question (Preprocessor Solution - HackerRank):

You are given a partially completed C++ program that is intended to find the difference between the maximum and minimum values in an array. The code does not compile because several preprocessor macros are missing.

Without modifying the existing code, define the required macros so that the program works correctly.

The macros must support:

Converting text to a string.
Reading input into vector elements.
Iterating through a vector.
Creating functions for finding minimum and maximum values using comparison operators.
Defining a large constant value INF.
Input Format
First line: Integer n, the size of the array.
Second line: n space-separated integers.
Output Format

The program should print:

Result = X

where X is the difference between the maximum and minimum element of the array.

Sample Input
5
32 332 -23 -154 65
Sample Output
Result = 486
Explanation

Maximum element = 332
Minimum element = -154

332 - (-154) = 486
Required Macros

Implement the following macros:

toStr(x)
io(v)
foreach(v, i)
FUNCTION(name, op)
INF

so that the locked code compiles and produces the correct output.
### HACKERRANK 62: OPERATOR OVERLOADING
HackerRank - Operator Overloading (Question)

You are given a partially completed program. Your task is to implement a class Matrix that supports matrix addition using operator overloading.

Requirements
Create a class Matrix.

The class should contain a public member:

vector<vector<int>> a;
Overload the + operator so that two Matrix objects can be added.
The overloaded operator should:
Add corresponding elements of the two matrices.
Return a new Matrix object containing the result.
Example

If:

Matrix A =
2 2
2 2

Matrix B =
1 2
3 4

Then:

A + B =
3 4
5 6
Input Format
First line contains T, the number of test cases.
For each test case:
First line contains N and M, the number of rows and columns.
Next line contains N × M integers representing the first matrix in row-major order.
Next line contains N × M integers representing the second matrix in row-major order.
Output Format

For each test case, print the resulting matrix after addition.

Sample Input
1
2 2
2 2 2 2
1 2 3 4
Sample Output
3 4
5 6
Explanation

The matrices are:

2 2      1 2
2 2  +   3 4

Adding corresponding elements:

3 4
5 6
What you need to submit

Only the Matrix class:

class Matrix {
public:
    vector<vector<int>> a;

    Matrix operator+(const Matrix& other) {
        Matrix result;
        int n = a.size();
        int m = a[0].size();

        result.a.resize(n, vector<int>(m));

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                result.a[i][j] = a[i][j] + other.a[i][j];
            }
        }

        return result;
    }
};
### HACKERRANK 63: MODIFIED KAPREKAR NUMBERS
Modified Kaprekar Numbers — Question Summary

You are given two integers p and q. Find all Modified Kaprekar Numbers in the inclusive range [p, q].

A number n is a Modified Kaprekar Number if:

Compute n².
Let d be the number of digits in n.
Split the decimal representation of n² into:
Left part = all digits except the last d digits.
Right part = the last d digits.
Convert both parts to integers (empty left part counts as 0).
If left + right = n, then n is a Modified Kaprekar Number.
Example
n = 45
45² = 2025
d = 2
Split: 20 | 25
20 + 25 = 45

Therefore, 45 is a Modified Kaprekar Number.

Input
First line: integer p
Second line: integer q
Output
Print all Modified Kaprekar Numbers between p and q (inclusive), separated by spaces.
If none exist, print:
INVALID RANGE
Sample Input
1
100
Sample Output
1 9 45 55 99
Function Signature
public static void kaprekarNumbers(int p, int q)

Constraints:

1 ≤ p < q ≤ 100000

Expected Approach: Iterate through numbers from p to q, square each number, split according to digit count, and check whether the sum of the two parts equals the original number.
### HACKERRANK 64: COVARIANT RETURN TYPES
HackerRank - Covariant Return Types (Question)

Java allows Covariant Return Types, which means an overridden method in a subclass can return a subtype of the return type declared in the superclass.

You are given partially completed classes representing flowers and regions. Implement the class hierarchy shown below:

Flower is the base class.
Jasmine and Lily extend Flower.

Region contains a method:

Flower yourNationalFlower()
WestBengal extends Region and overrides yourNationalFlower() to return a Jasmine.
AndhraPradesh extends Region and overrides yourNationalFlower() to return a Lily.

Each flower class should implement:

String whatsYourName()

which returns the flower's name.

The hidden code will:

Read a state name (WestBengal or AndhraPradesh).
Create the corresponding object.
Call yourNationalFlower().
Print the result of whatsYourName().

You only need to complete the class definitions.

Sample Input
AndhraPradesh
Sample Output
Lily
Explanation

An AndhraPradesh object returns a Lily object from yourNationalFlower(). Calling whatsYourName() on that object returns "Lily".

Key Concept Tested

Covariant Return Types in Java:

class Region {
    Flower yourNationalFlower() { ... }
}

class AndhraPradesh extends Region {
    @Override
    Lily yourNationalFlower() { ... } // Valid
}

A subclass method may return a subclass of the parent method's return type.
### HACKERRANK 65: JAVA LAMBDA EXPRESSION
Java Lambda Expressions – HackerRank

This Java 8 challenge tests your knowledge of Lambda Expressions.

Write the following methods that return a lambda expression performing a specified action:

PerformOperation isOdd()
Returns true if a number is odd.
Returns false if a number is even.
PerformOperation isPrime()
Returns true if a number is prime.
Returns false if it is composite.
PerformOperation isPalindrome()
Returns true if a number is a palindrome.
Returns false otherwise.
Input Format
The first line contains an integer T (number of test cases).

Each of the next T lines contains two space-separated integers:

ch – the condition to check:
1 → Odd/Even
2 → Prime/Composite
3 → Palindrome/Not Palindrome
num – the number to be checked
Sample Input
5
1 4
2 5
3 898
1 3
2 12
Sample Output
EVEN
PRIME
PALINDROME
ODD
COMPOSITE
Explanation
1 4 → 4 is even → EVEN
2 5 → 5 is prime → PRIME
3 898 → 898 is a palindrome → PALINDROME
1 3 → 3 is odd → ODD
2 12 → 12 is composite → COMPOSITE
Constraints
1 ≤ T ≤ 100
0 ≤ num ≤ 2^31 - 1

The goal is to implement the required methods using Java 8 Lambda Expressions (or equivalent logic if using Java 7).
### HACKERRANK 66: OVERLOAD OPERATOR
HackerRank - Overload Operators (Question)

You are given a class:

class Complex
{
public:
    int a, b;
};

A complex number is represented as:

a+ib

where:

a = real part
b = imaginary part
Your task is to overload the + and << operators for the Complex class.

Operator +

The + operator should add two complex numbers according to:

(a+ib)+(c+id)=(a+c)+i(b+d)

For example:

Complex z = x + y;

should return a new complex number whose:

real part = x.a + y.a
imaginary part = x.b + y.b
Operator <<

The stream insertion operator << should print a complex number in the format:

a+ib

For example:

cout << c << endl;

should print:

a+ib

where a and b are the real and imaginary parts of the complex number.

Input Format

Two complex numbers are given as strings in the format:

a+ib

The provided input() function parses these strings and stores the values in objects of class Complex.

Output Format

Print the sum of the two complex numbers in the format:

a+ib
Sample Input
3+i4
5+i6
Sample Output
8+i10
Explanation
(3 + i4) + (5 + i6)
= (3 + 5) + i(4 + 6)
= 8 + i10

You only need to implement the overloaded operators + and <<; the rest of the code is already provided by HackerRank.
### HACKERRANK 67: JAVA MD5
Java MD5

MD5 (Message-Digest Algorithm 5) is a widely used cryptographic hash function.

Given an alphanumeric string S, compute and print its MD5 encryption value.

Input Format
A single alphanumeric string S
Constraints
String S consists only of:
English alphabet letters (a-z, A-Z)
Digits (0-9)
Output Format
Print the MD5 hash of S in hexadecimal format.
Sample Input 0
HelloWorld
Sample Output 0
68e109f0f40ca72a15e05cc22786f8e6
Sample Input 1
Javarmi123
Sample Output 1
2da2d1e0ce7b4951a858ed2d547ef485
### HACKERRANK 68: ATTENDING WORKSHOP
Attending Workshops

A student has signed up for n workshops.
Each workshop has:

start time
duration
end time = start time + duration

The student wants to attend the maximum number of workshops such that no two workshops overlap.

You need to implement:

Structures
struct Workshop {
    int start_time;
    int duration;
    int end_time;
};

struct Available_Workshops {
    int n;
    Workshop* arr;
};
Functions
1. initialize
Available_Workshops* initialize(int start_time[], int duration[], int n)
Create an Available_Workshops object.
Fill all workshops using given arrays.
Compute end_time.
2. CalculateMaxWorkshops
int CalculateMaxWorkshops(Available_Workshops* ptr)
Return maximum number of workshops student can attend.
Workshops must not overlap.
Sample Input
6
1 3 0 5 5 8
1 1 6 2 4 1
Sample Output
4
Explanation

Possible workshops attended without overlap = 4.
### HACKERRANK 69: JAVA SHA-256
Java SHA-256

Cryptographic hash functions are mathematical operations run on digital data. By comparing the computed hash (output of a hashing algorithm) to a known hash value, one can verify data integrity.

SHA-256 is part of the Secure Hash Algorithm 2 (SHA-2) family and produces a 256-bit hash value, typically represented as a 64-character hexadecimal string.

Task

Given a string s, print its SHA-256 hash value
Input Format
A single alphanumeric string s
Constraints
s contains only:
English letters (a-z, A-Z)
Digits (0-9)
Output Format

Print the SHA-256 hash of the input string.

Sample Input 0
HelloWorld
Sample Output 0
872e4e50ce9990d8b041330c47c9ddd11bec6b503ae9386a99da8584e9bb12c4
Sample Input 1
Javarmi123
Sample Output 1
f1d5f8d75bb55c777207c251d07d9091dc10fe7d6682db869106aacb4b7df678
### HACKERRANK 70: C++ CLASS TEMPLATE SPECIALIZATION
C++ Class Template Specialization

You are given a main function which reads the enumeration values for two different types as input, then prints out the corresponding enumeration names.

Write a class template that can provide the names of the enumeration values for both types.

If the enumeration value is not valid, then print unknown.

Input Format
First line contains integer t, the number of test cases.
Each of the next t lines contains two space-separated integers:
First integer = color value
Second integer = fruit value
Output Format

For each test case, print:

color name
fruit name

If value is invalid, print unknown.

Enums Given
enum class Fruit { apple, orange, pear };
enum class Color { red, green, orange };
Mapping:

Fruit

0 → apple
1 → orange
2 → pear

Color

0 → red
1 → green
2 → orange
Sample Input
2
1 0
3 3
Sample Output
green apple
unknown unknown
Explanation
1 0 → Color = green, Fruit = apple
3 3 → Both invalid → unknown unknown

Task: Define specializations for Traits<Color> and Traits<Fruit>.
### HACKERRANK 71: BIGGER IS GREATER
Bigger is Greater — HackerRank

Lexicographical order is often known as alphabetical order when dealing with strings.
A string is greater than another string if it comes later in a lexicographically sorted list.

Given a word, create a new word by swapping some or all of its characters. This new word must satisfy:

It must be greater than the original word
It must be the smallest word that satisfies condition 1

If no such string exists, return "no answer".
Function Description

Complete:

biggerIsGreater(String w)

Parameters:

w → input string

Returns:

String → next lexicographically greater string
"no answer" if impossible
Input Format
First line contains integer T (number of test cases)
Next T lines each contain a string w
Constraints
String contains only lowercase letters a-z
Sample Input 0
5
ab
bb
hefg
dhck
dkhc
Sample Output 0
ba
no answer
hegf
dhkc
hcdk
Sample Input 1
6
lmno
dcba
dcbb
abdc
abcd
fedcbabcd
Sample Output 1
lmon
no answer
no answer
acbd
abdc
fedcbabdc
Example
"ab" → next bigger = "ba"
"bb" → no greater permutation exists → "no answer"
### HACKERRANK 72: MINIMUM DISTANCES
Problem Statement

Given an array a, find the minimum distance between any pair of equal elements.

Distance between two positions i and j is:

|i - j|

If no matching pair exists, return -1.
Example 1

Input:

a = [7, 1, 3, 4, 1, 7]

Equal pairs:

7 at index (0, 5) → distance = 5
1 at index (1, 4) → distance = 3

Minimum distance = 3

Output:

3
Example 2

Input:

a = [1, 2, 3, 4]

No repeated elements.

Output:

-1
Constraints
Array size can be large, so efficient solutions are preferred.
Function Signature
public static int minimumDistances(List<Integer> a)

Return:

Minimum distance between equal elements
-1 if no pair exists.
### HACKERRANK 73: HALLOWEEN SALE
Halloween Sale — Question

You want to buy video games from an online store.

The first game costs p dollars.
Every next game costs d dollars less than the previous one.
The price keeps decreasing until it reaches m dollars.
After that, every game costs exactly m dollars.

You have a budget of s dollars.

Your task is to determine how many games you can buy.

Function

Implement:

int howManyGames(int p, int d, int m, int s)

Returns:

Number of games that can be bought.
Input

Four integers:

p → initial price
d → discount after each purchase
m → minimum possible price
s → total budget
Constraints
Price never goes below m
Can buy games until budget is insufficient
Example 1

Input:

20 3 6 80

Prices:

20, 17, 14, 11, 8, 6

Total spent:

76

Output:

6
Example 2

Input:

20 3 6 85

Output:

7
### HACKERRANK 74: TIME IN WORDS
HackerRank - The Time in Words question:

Given the time in numerals, convert it into words.

Rules:

At 00 minutes, use "o' clock"
For minutes 1–30, use "past"
For minutes 31–59, use "to"
Special words:
15 → quarter
30 → half
Function Description

Complete the function:

public static String timeInWords(int h, int m)

Parameters:

int h → hour
int m → minutes

Returns:

String → time in words
Input Format
First line: integer h (hour)
Second line: integer m (minutes)
Constraints
1 <= h <= 12
0 <= m < 60
Examples
Input
5
47
Output
thirteen minutes to six
Input
3
00
Output
three o' clock
Input
7
15
Output
quarter past seven


Chocolate Feast — Problem Statement

Little Bobby loves chocolate. He frequently goes to his favorite store, Penny Auntie, to buy chocolates. The store has a promotion:

For every m wrappers, Bobby can exchange them for 1 free chocolate.

Given:

n → amount of money Bobby has
c → cost of one chocolate
m → number of wrappers needed for one free chocolate

Find the total number of chocolates Bobby can eat if he uses the promotion optimally.

Function Description

Complete the function:
int chocolateFeast(int n, int c, int m)
Parameters:
int n: initial money
int c: cost of one chocolate
int m: wrappers needed for one free chocolate
Returns:
int: total chocolates Bobby can eat
Input Format
First line contains integer t → number of test cases.
Next t lines contain three integers:
n c m
Constraints
1 ≤ t ≤ 100
1 ≤ n, c, m ≤ 10^5
Sample Input
3
10 2 5
12 4 4
6 2 2
Sample Output
6
3
5
Explanation
Test Case 1:
Money = 10, Cost = 2
Buy 10/2 = 5 chocolates
5 wrappers → exchange for 1 free chocolate
Total = 6
Test Case 2:
Buy 12/4 = 3 chocolates
Only 3 wrappers, need 4
Total = 3
Test Case 3:
Buy 6/2 = 3 chocolates
Exchange wrappers repeatedly
Total = 5
