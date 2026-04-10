HACKERRANK: Save the Prisoner!

A jail has n prisoners sitting in a circle, numbered from 1 to n.

There are m sweets to distribute. Distribution starts from chair s, and sweets are given one by one in order around the circle.

The last sweet is bad, so you must determine which prisoner gets it.

🎯 Output

For each test case, print the chair number of the prisoner who receives the last sweet.

🧠 Logic

Use modulo to avoid simulation:

result
=
(
𝑠
+
𝑚
−
2
)
 
m
o
d
 
𝑛
+
1
result=(s+m−2)modn+1
💻 Final Java Code (Ready to Submit)
import java.io.*;
import java.util.*;

public class Solution {

    static int saveThePrisoner(int n, int m, int s) {
        return (s + m - 2) % n + 1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        for (int i = 0; i < t; i++) {
            String[] input = bufferedReader.readLine().split(" ");
            int n = Integer.parseInt(input[0]);
            int m = Integer.parseInt(input[1]);
            int s = Integer.parseInt(input[2]);

            int result = saveThePrisoner(n, m, s);
            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();
        }

        bufferedReader.close();
        bufferedWriter.close();
    }
}
🧪 Sample Input
2
5 2 1
5 2 2
✅ Sample Output
2
3