In **vector math** and **linear algebra**, the **determinant** is a scalar value that is calculated from a **square matrix**. It provides important information about the matrix, such as whether it is invertible, and it has geometric interpretations, like scaling factors for transformations. Determinants are especially useful for solving systems of **simultaneous linear equations**.

### Determinant Overview
For a **2x2 matrix**:
\[
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
\]
the determinant of \( A \), denoted as \( \det(A) \) or \( |A| \), is calculated as:
\[
\det(A) = ad - bc
\]

For **3x3 matrices** and higher dimensions, the determinant calculation is more complex, involving the use of minors and cofactors, but the concept remains similar.

### Determinants in Solving Simultaneous Equations
Consider a system of two simultaneous linear equations:
\[
a_1 x + b_1 y = c_1
\]
\[
a_2 x + b_2 y = c_2
\]

This system can be written in matrix form as:
\[
\begin{bmatrix} a_1 & b_1 \\ a_2 & b_2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} c_1 \\ c_2 \end{bmatrix}
\]

Let’s call the coefficient matrix \( A \):
\[
A = \begin{bmatrix} a_1 & b_1 \\ a_2 & b_2 \end{bmatrix}
\]

The solution to this system can be found using **Cramer's Rule**, which involves determinants.

### Cramer’s Rule
Cramer’s Rule states that for a system of linear equations \( A \mathbf{x} = \mathbf{b} \), if \( \det(A) \neq 0 \), the system has a unique solution given by:
\[
x = \frac{\det(A_x)}{\det(A)} \quad \text{and} \quad y = \frac{\det(A_y)}{\det(A)}
\]
where:
- \( A_x \) is the matrix formed by replacing the first column of \( A \) with the constants vector \( \mathbf{b} \).
- \( A_y \) is the matrix formed by replacing the second column of \( A \) with \( \mathbf{b} \).

### Example: Solving Two Simultaneous Equations
Let’s solve the system:
\[
2x + 3y = 8
\]
\[
4x - y = -2
\]

#### Step 1: Write the Coefficient Matrix and Constants
The coefficient matrix \( A \) and constants vector \( \mathbf{b} \) are:
\[
A = \begin{bmatrix} 2 & 3 \\ 4 & -1 \end{bmatrix} \quad \text{and} \quad \mathbf{b} = \begin{bmatrix} 8 \\ -2 \end{bmatrix}
\]

#### Step 2: Calculate the Determinant of \( A \)
Using the formula for the determinant of a 2x2 matrix:
\[
\det(A) = (2)(-1) - (3)(4) = -2 - 12 = -14
\]

Since \( \det(A) \neq 0 \), the system has a unique solution.

#### Step 3: Form Matrices \( A_x \) and \( A_y \)
1. **Matrix \( A_x \)**: Replace the first column of \( A \) with \( \mathbf{b} \):
   \[
   A_x = \begin{bmatrix} 8 & 3 \\ -2 & -1 \end{bmatrix}
   \]
   
2. **Matrix \( A_y \)**: Replace the second column of \( A \) with \( \mathbf{b} \):
   \[
   A_y = \begin{bmatrix} 2 & 8 \\ 4 & -2 \end{bmatrix}
   \]

#### Step 4: Calculate \( \det(A_x) \) and \( \det(A_y) \)
1. **Determinant of \( A_x \)**:
   \[
   \det(A_x) = (8)(-1) - (3)(-2) = -8 + 6 = -2
   \]

2. **Determinant of \( A_y \)**:
   \[
   \det(A_y) = (2)(-2) - (8)(4) = -4 - 32 = -36
   \]

#### Step 5: Solve for \( x \) and \( y \)
Using Cramer’s Rule:
\[
x = \frac{\det(A_x)}{\det(A)} = \frac{-2}{-14} = \frac{1}{7}
\]
\[
y = \frac{\det(A_y)}{\det(A)} = \frac{-36}{-14} = \frac{18}{7}
\]

### Solution
The solution to the system is:
\[
x = \frac{1}{7}, \quad y = \frac{18}{7}
\]

### Summary
The **determinant** allows us to determine if a system of equations has a unique solution (if \( \det(A) \neq 0 \)), and Cramer’s Rule provides a straightforward way to find this solution using determinants. This method is particularly useful for small systems of equations and is a classic application of determinants in vector math and linear algebra.

