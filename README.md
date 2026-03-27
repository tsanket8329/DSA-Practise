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
