# Asymptotic Analysis
1. Tool to describe time complexity of an algorithm.
2. Provide Mathematical models.
3. As a function of input size independent of architecture and language.
4. compare various algorithms for same probles.


## Asymptotic Notation
1. Big-Oh (O) notation: Denote upper bound of an algorithm.Worst case analysis.

![title](Images/BigO1.png)

![title](Images/BigO2.png)

2. Omega Notation: Denote Lower bound of an algorithm. Best case analysis.

![title](Images/Omega1.png)

![title](Images/Omega2.png)

3. Theta Notation: Exact asymptotic behavior.Average case analysis.

![title](Images/Theta1.png)

![title](Images/Theta2.png)

# Tuple
1. tuple as list collection of an heterogeneous objects.
2. tuple are immutable.
3. In tupe we use curly parentheses. 
4. It represent as ().

# dictionary
1. Dictionary are very useful data structure in python there are also known as associative arrays.
2. Dictionary are essentialy mutable key value pair.
3. Tuple can be keys, list can't be keys, values can be mutable or immutable.
4. It represent as {}.

# Sets
1. Sets is a collection of immutable objects which are unorder and unique.
2. Sets itself can be mutable.
3. It represent as {}.


# Data Structure and Algorithms

## Divide and Conquer 
The problem solving strategy that involves breaking down a complex problem into smaller, more manageable parts, solving each part individually, and then combining the solution to solve the original problem.
#### Stages of Divide and Conquer Algorithm:
1. Divide: Break down the original problem into smaller subproblems.
Each subproblem should represent a part of the overall problem.
The goal is to divide the problem until no further division is possible.

2. Conquer: Solve each of the smaller subproblems individually.
If a subproblem is small enough (often referred to as the “base case”), we solve it directly without further recursion.
The goal is to find solutions for these subproblems independently.

3. Merge: Combine the sub-problems to get the final solution of the whole problem.
Once the smaller subproblems are solved, we recursively combine their solutions to get the solution of larger problem.
The goal is to formulate a solution for the original problem by merging the results from the subproblems.

#### Applications of Divide and Conquer Algorithm:
1. Merge Sort: Merge sort is a classic example of a divide and conquer sorting algorithm. It breaks down the array into smaller subarrays, sorts them individually, and then merges them to obtain the sorted array.

2. Median Finding: The median of a set of numbers can be found using a divide and conquer approach. By recursively dividing the set into smaller subsets, the median can be determined efficiently.

3. Min and Max Finding: Divide and Conquer algorithm can be used to find both the minimum and maximum elements in an array simultaneously. By splitting the array into halves and comparing the min-max pairs from each half, the overall min and max can be identified in logarithmic time complexity.

4. Matrix Multiplication: Strassen’s algorithm for matrix multiplication is a divide and conquer technique that reduces the number of multiplications required for large matrices by breaking down the matrices into smaller submatrices and combining their products.

5. Closest Pair problem: The closest pair problem involves finding the two closest points in a set of points in a multidimensional space. A divide and conquer algorithm, such as the “divide and conquer closest pair” algorithm, can efficiently solve this problem by recursively dividing the points and merging the solutions from the subproblems.


## Recursion 
The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called a recursive function. Using a recursive algorithm, certain problems can be solved quite easily.

## Greedy
A greedy algorithm is a type of optimization algorithm that makes locally optimal choices at each step to find a globally optimal solution. It operates on the principle of “taking the best option now” without considering the long-term consequences.

## Dynamic Programming
Dynamic Programming (DP) is a method used in mathematics and computer science to solve complex problems by breaking them down into simpler subproblems. By solving each subproblem only once and storing the results, it avoids redundant computations, leading to more efficient solutions for a wide range of problems.

####When to use DP
1. Optimal Substructure: Optimal substructure means that we combine the optimal results of subproblems to achieve the optimal result of the bigger problem.

2. Overlapping Subproblems: The same subproblems are solved repeatedly in different parts of the problem.

# List
1. List in python are mutable sequences of heteroginious patterns i.e. you can add, remove, and modify the list.

