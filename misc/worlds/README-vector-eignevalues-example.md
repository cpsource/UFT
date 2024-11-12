Here's how to find the **eigenvalues** and **eigenvectors** of the example matrix in the **Wolfram Language**.

We’ll use the matrix:
\[
A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}
\]

### Step-by-Step Code:

```wolfram
(* Define the matrix *)
A = {{2, 1}, {1, 2}};

(* Calculate the eigenvalues *)
eigenvalues = Eigenvalues[A]

(* Calculate the eigenvectors *)
eigenvectors = Eigenvectors[A]

(* Display eigenvalues and eigenvectors together *)
eigenData = TableForm[Transpose[{eigenvalues, eigenvectors}], 
  TableHeadings -> {None, {"Eigenvalue", "Eigenvector"}}]
```

### Explanation:
- **`Eigenvalues[A]`**: This function calculates the eigenvalues of the matrix \( A \).
- **`Eigenvectors[A]`**: This function calculates the corresponding eigenvectors of the matrix \( A \).
- **`TableForm`**: This command formats the output in a table, displaying each eigenvalue with its corresponding eigenvector.

### Expected Output:
Running this code will yield:
1. The **eigenvalues** of matrix \( A \), which should be \[ \lambda = 3 \text{ and } \lambda = 1 \].
2. The **eigenvectors** associated with each eigenvalue.

### Example Output:
The output should look something like this:

| Eigenvalue | Eigenvector       |
|------------|-------------------|
| 3          | {1, 1}           |
| 1          | {-1, 1}          |

So the **eigenvalues** are \( 3 \) and \( 1 \), with corresponding **eigenvectors** `{1, 1}` and `{-1, 1}`, respectively.

This result confirms that the eigenvalues and eigenvectors we derived earlier are correct.

