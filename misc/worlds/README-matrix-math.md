Yes, Ubuntu offers several matrix math libraries that support matrix operations, including **inversion**, **multiplication**, **determinant calculation**, **eigenvalues**, and more. Here are some of the most popular matrix math packages available on Ubuntu:

### 1. **Eigen**

- **Description**: Eigen is a high-performance C++ library for linear algebra, including matrix and vector operations. It's well-suited for applications that require efficient and reliable matrix math.
- **Features**:
  - Supports matrix inversion, multiplication, decomposition, and more.
  - Optimized for speed with templates and expression templates.
  - Provides dense and sparse matrix capabilities.
- **Installation**:
  ```bash
  sudo apt install libeigen3-dev
  ```
- **Documentation**: [Eigen Documentation](https://eigen.tuxfamily.org/dox/)

### 2. **Armadillo**

- **Description**: Armadillo is a C++ linear algebra library that focuses on ease of use and high performance. It is built on top of LAPACK and BLAS, and it supports a variety of matrix operations.
- **Features**:
  - Matrix inversion, multiplication, decomposition, and eigenvalue calculations.
  - Provides a simple syntax similar to MATLAB.
  - Fast and efficient with automatic linking to LAPACK and BLAS.
- **Installation**:
  ```bash
  sudo apt install libarmadillo-dev
  ```
- **Documentation**: [Armadillo Documentation](http://arma.sourceforge.net/docs.html)

### 3. **NumPy (Python)**

- **Description**: NumPy is the foundational package for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a large library of mathematical functions.
- **Features**:
  - Matrix inversion, determinants, and a variety of linear algebra functions.
  - Part of the SciPy ecosystem, which provides additional functionality.
  - Easy to use with a simple syntax for matrix operations.
- **Installation**:
  ```bash
  sudo apt install python3-numpy
  ```
- **Documentation**: [NumPy Documentation](https://numpy.org/doc/stable/)

### 4. **SciPy (Python)**

- **Description**: SciPy is a Python library built on top of NumPy that provides additional scientific and mathematical functions, including advanced linear algebra operations.
- **Features**:
  - Includes functions for matrix inversion, solving linear systems, decompositions, and more.
  - Works well with NumPy arrays, making it ideal for complex scientific computations.
- **Installation**:
  ```bash
  sudo apt install python3-scipy
  ```
- **Documentation**: [SciPy Documentation](https://docs.scipy.org/doc/scipy/)

### 5. **GSL (GNU Scientific Library)**

- **Description**: The GNU Scientific Library (GSL) is a C library for numerical computations, including matrix operations.
- **Features**:
  - Supports matrix inversion, multiplication, and decomposition.
  - Provides a wide array of scientific computing functions, including statistics, integration, and Fourier transforms.
- **Installation**:
  ```bash
  sudo apt install libgsl-dev
  ```
- **Documentation**: [GSL Documentation](https://www.gnu.org/software/gsl/)

### 6. **LAPACK (Linear Algebra PACKage)**

- **Description**: LAPACK is a highly optimized library written in Fortran for linear algebra routines. It is commonly used for solving systems of linear equations, eigenvalue problems, and other matrix operations.
- **Features**:
  - Provides matrix inversion, decomposition, and eigenvalue calculations.
  - Often used as a backend for other libraries (like Armadillo and SciPy).
- **Installation**:
  ```bash
  sudo apt install liblapack-dev
  ```
- **Documentation**: [LAPACK Documentation](https://www.netlib.org/lapack/)

### 7. **BLAS (Basic Linear Algebra Subprograms)**

- **Description**: BLAS is a low-level library that provides basic routines for vector and matrix operations. It is the foundation for many other linear algebra libraries, such as LAPACK.
- **Features**:
  - Supports matrix-vector and matrix-matrix operations.
  - Optimized for performance and often used in conjunction with LAPACK.
- **Installation**:
  ```bash
  sudo apt install libblas-dev
  ```
- **Documentation**: [BLAS Documentation](https://www.netlib.org/blas/)

### 8. **OpenBLAS**

- **Description**: OpenBLAS is an optimized implementation of BLAS that provides better performance on various hardware architectures. It is often used as an alternative to the standard BLAS.
- **Features**:
  - Drop-in replacement for BLAS with improved performance.
  - Supports a range of matrix operations and can be linked to other libraries.
- **Installation**:
  ```bash
  sudo apt install libopenblas-dev
  ```
- **Documentation**: [OpenBLAS Documentation](https://www.openblas.net/)

### Example Code Using NumPy and SciPy in Python

Here’s an example of using **NumPy** and **SciPy** to perform matrix inversion in Python:

```python
import numpy as np
from scipy.linalg import inv

# Define a 3x3 matrix
A = np.array([[4, 7, 2],
              [3, 5, 1],
              [2, 6, 3]])

# Calculate the inverse using SciPy
A_inv = inv(A)

print("Matrix A:")
print(A)
print("\nInverse of A:")
print(A_inv)
```

### Example Code Using Eigen in C++

Here’s an example of using **Eigen** in C++ to invert a matrix:

```cpp
#include <iostream>
#include <Eigen/Dense>

int main() {
    // Define a 3x3 matrix
    Eigen::Matrix3d A;
    A << 4, 7, 2,
         3, 5, 1,
         2, 6, 3;

    // Calculate the inverse
    Eigen::Matrix3d A_inv = A.inverse();

    std::cout << "Matrix A:\n" << A << std::endl;
    std::cout << "\nInverse of A:\n" << A_inv << std::endl;

    return 0;
}
```

Compile with:
```bash
g++ -o matrix_inverse matrix_inverse.cpp -I /usr/include/eigen3
```

### Summary

Each of these libraries has its strengths:

- **NumPy/SciPy**: Great for scientific computing in Python. Very user-friendly.
- **Eigen and Armadillo**: Ideal for C++ applications with a focus on performance.
- **GSL and LAPACK**: Comprehensive scientific libraries, commonly used in high-performance computing.

Choose the library that best fits your preferred programming language and performance requirements.

