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
