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
