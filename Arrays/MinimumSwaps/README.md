#Medium

You are given an unordered array consisting of consecutive integers [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.

**Example**
arr = [7,1,3,2,4,5,6]

Perform the following steps:

```
i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]
```

It took 5 swaps to sort the array.

**Function Description**
Complete the function minimumSwaps. 
minimumSwaps has the following parameter(s):
- int arr[n]: an unordered array of integers
**Returns**
- int: the minimum number of swaps to sort the array

**Input Format**
The first line contains an integer, n, the size of arr. 
The second line contains n space-separated integers arr[i].

**Constraints**
- 1 <= n <= 10^5
- 1 <= arr[i] <=n

**Sample Input**
```
5
2 3 4 1 5
```
**Sample Output**
```
3
```
**Explanation**
```
Given array arr:[2,3,4,1,5] 
After swapping (2,3) we get arr : [2,3,1,4,5]   
After swapping (0,1) we get arr : [3,2,1,4,5] 
After swapping (0,2) we get arr : [1,2,3,4,5]
```
So, we need a minimum of 3 swaps to sort the array in ascending order.
