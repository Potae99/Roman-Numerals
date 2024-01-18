# The design of test cases

## Base case
There are 7 base cases covering: I,V,X,L,C,D,M

## Boundary Value Condition
1. Min case:1 | I
2. Max case: 3888 | MMMDCCCLXXXVIII

# 1st approach
### Addition case 
| Hindo-Arabic | Roman
--------- | ---------
2 | II
3 | III
6 | VI
7 | VII

...

### Subtraction case
| Hindo-Arabic | Roman
--------- | ---------
4 | IV
9 | IV
40 | XL
49 | IL
99 | IC

### Mixed case
| Hindo-Arabic | Roman
--------- | ---------
24 | XXIV
42 | XLII

## 2nd Approach
### Unit case
Hindo-Arabic | Roman
---------- | ----------
1 | I
2 | II
3 | III
4 | IX
5 | V
6 | VI
7 | VII
8 | VIII
9 | IX


### Tens case
| Hindo-Arabic | Roman
--------- | ---------
10 | X
11 | XI
12 | XII
...

### Hundreds case
| Hindo-Arabic | Roman
--------- | ---------

100 | C
101 | CI
110 | CX
