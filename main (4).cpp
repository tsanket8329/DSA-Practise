class Solution {
  public:
    int maxSumWithK(vector<int>& arr, int k) {
        int n = arr.size();

        vector<int> maxEndHere(n);

        // Kadane: maximum subarray sum ending at each index
        maxEndHere[0] = arr[0];
        for (int i = 1; i < n; i++) {
            maxEndHere[i] = max(arr[i], maxEndHere[i - 1] + arr[i]);
        }

        // Sum of first k elements
        int windowSum = 0;
        for (int i = 0; i < k; i++)
            windowSum += arr[i];

        int ans = windowSum;

        // Slide the window
        for (int i = k; i < n; i++) {
            windowSum += arr[i] - arr[i - k];

            ans = max(ans, windowSum);

            ans = max(ans, windowSum + maxEndHere[i - k]);
        }

        return ans;
    }
};