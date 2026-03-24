LEFT ROTATION DSA PROBLEM 
A left rotation operation on a circular array shifts each of the array's elements 1 unit to the left. The elements that fall off the left end reappear at the right end. Given an integer d, rotate the array that many steps to the left and return the result

Example

d=2

arr = [1,2,3,4,5

After 2 rotations, arr = [3,4,5,1,2).

Function Description

Complete the rotate Left function with the following parameters:

int d the amount to rotate by

int arr[n]: the array to rotate

Returns

int n) the rotated array

Input Format

The first line contains two space-seperated integens that denote n., the number of integers, and d the number of left rotations to perform

The second line contains in space separated integers that describe arr

Constraints

1<n<10^5

1<d<n

1≤ i ≤ 10^6
Sample Output

51234

Explanation

To perform d = 4 left rotations, the array undergoes the following sequence of changes:

[1, 2, 3, 4, 5] -> [2, 3, 4, 5, 1] -> [3, 4, 5, 1, 2] -> [4, 5, 1, 2, 3] -> [5, 1, 2, 3, 4]
 CODE:
 #include <bits/stdc++.h>
using namespace std;

vector<int> rotateLeft(int d, vector<int> arr) {
    int n = arr.size();
    vector<int> result;

    for(int i = d; i < n; i++)
        result.push_back(arr[i]);

    for(int i = 0; i < d; i++)
        result.push_back(arr[i]);

    return result;
}

int main() {
    int n, d;
    cin >> n >> d;

    vector<int> arr(n);
    for(int i = 0; i < n; i++)
        cin >> arr[i];

    vector<int> result = rotateLeft(d, arr);

    for(int x : result)
        cout << x << " ";

    return 0;
}
