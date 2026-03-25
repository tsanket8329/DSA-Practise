Hackerank - 2   DRAWING BOOK
A teacher asks the class to open their books to a page number. A student can start turning pages either from the front of the book or from the back. They always turn pages one at a time. When the book is opened, page 1 is always on the right side.

When a page is flipped, two new pages become visible (except possibly the last page). Each page except the last page is printed on both sides.

If the book has n pages and the student wants to reach page p, determine the minimum number of page turns required. The student may start turning pages either from the front or the back of the book.

Function Description

Complete the function:

int pageCount(int n, int p)

Parameters

n : total number of pages in the book

p : target page number

Returns

Minimum number of pages that must be turned.

Input Format

First line: integer n (number of pages in the book)

Second line: integer p (page number to turn to)

Example

Input

6
2

Output

1

Explanation:
Turning from the front requires 1 page turn, while turning from the back requires 2 page turns. The minimum is 1.
CODE: 
#include <iostream>
#include <algorithm>
using namespace std;

int pageCount(int n, int p) {
    int frontTurns = p / 2;
    int backTurns = (n / 2) - (p / 2);
    return min(frontTurns, backTurns);
}

int main() {
    int n, p;
    cin >> n;
    cin >> p;

    cout << pageCount(n, p);

    return 0;
}