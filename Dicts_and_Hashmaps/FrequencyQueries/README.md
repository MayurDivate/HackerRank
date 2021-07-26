# Medium

You are given q queries. Each query is of the form two integers described below: 
- 1x : Insert x in your data structure. 
- 2y : Delete one occurence of y from your data structure, if present. 
- 3z : Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.

The queries are given in the form of a 2-D array queries of size q where queries[i][0] contains the operation, and queries[i][1] contains the data element.
Example 

queries = [(1,1),(2,2),(3,3),(1,1),(1,1),(2,1),(3,2)]

The results of each operation are:

```buildoutcfg
Operation   Array   Output
(1,1)       [1]
(2,2)       [1]
(3,2)                   0
(1,1)       [1,1]
(1,1)       [1,1,1]
(2,1)       [1,1]
(3,2)                   1
```

Return an array with the output: [0,1].

**Function Description**

Complete the freqQuery function.

freqQuery has the following parameter(s):
- int queries[q][2]: a 2-d array of integers

**Returns**
- int[]: the results of queries of type

**Constraints**
- 0 < q <= 10^5
- 0 < x,y,z <= 10^9
- all querries [i][0] E {1,2,3}
- 0 < queries[i][1] <= 10^9


**Sample Input 0**
```buildoutcfg
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2
```
**Sample Output 0**
```
0
1
```

**Explanation 0**
```
For the first query of type 3, there is no integer whose frequency is 2 (array=[5,6]). So answer is 0. 
For the second query of type 3, there are two integers in  array = [6, 10,10, 6] whose frequency is  2 (integers = 6 and 10 ). So, the answer is 1.
```

**Sample Input 1**
```
4
3 4
2 1003
1 16
3 1
```
**Sample Output 1**
```
0
1 
```


**Sample Input 2**
```
10
1 3
2 3
3 2
1 4
1 5
1 5
1 4
3 2
2 4
3 2
```

**Sample Output 2**
```
0
1
1
```