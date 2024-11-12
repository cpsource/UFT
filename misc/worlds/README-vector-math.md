
# Rotation and Translation of a Point in 3D Space Using Matrix Algebra

In this guide, we show how to rotate and translate a point in 3D space using matrix algebra. This approach is commonly used in computer graphics and 3D transformations.

## 1. Represent the Point as a Vector
Let’s say we have a point \( P \) in 3D space with coordinates \( (x, y, z) \).

We represent this point as a **column vector**:
\[
P = \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}
\]

Here, the extra 1 is included to allow for **translation** using **homogeneous coordinates**.

## 2. Rotation in 3D Space
Rotations in 3D can be done around the **x-axis**, **y-axis**, or **z-axis**. We can create rotation matrices for each of these axes.

### a) Rotation Around the X-Axis by Angle \( \theta \)
\[
R_x(\theta) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & \cos \theta & -\sin \theta & 0 \\ 0 & \sin \theta & \cos \theta & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}
\]

### b) Rotation Around the Y-Axis by Angle \( \phi \)
\[
R_y(\phi) = \begin{bmatrix} \cos \phi & 0 & \sin \phi & 0 \\ 0 & 1 & 0 & 0 \\ -\sin \phi & 0 & \cos \phi & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}
\]

### c) Rotation Around the Z-Axis by Angle \( \psi \)
\[
R_z(\psi) = \begin{bmatrix} \cos \psi & -\sin \psi & 0 & 0 \\ \sin \psi & \cos \psi & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}
\]

To perform a rotation around multiple axes, we can multiply these matrices together. For example, to rotate around the x-axis by \( \theta \), y-axis by \( \phi \), and z-axis by \( \psi \), the combined rotation matrix \( R \) is:
\[
R = R_z(\psi) \times R_y(\phi) \times R_x(\theta)
\]

## 3. Translation in 3D Space
A translation matrix \( T \) to move a point by \( (t_x, t_y, t_z) \) is:
\[
T = \begin{bmatrix} 1 & 0 & 0 & t_x \\ 0 & 1 & 0 & t_y \\ 0 & 0 & 1 & t_z \\ 0 & 0 & 0 & 1 \end{bmatrix}
\]

## 4. Combined Rotation and Translation
To apply both rotation and translation to a point \( P \), we can combine the rotation and translation matrices. First, we rotate the point, then apply the translation. This is done by multiplying the matrices:
\[
M = T \times R
\]

Then, we apply \( M \) to the point \( P \):
\[
P' = M \times P
\]

where \( P' \) is the transformed point after rotation and translation.

## Example
Suppose we want to:
- Rotate a point \( P = (x, y, z) \) by \( \theta = 30^\circ \) around the x-axis, \( \phi = 45^\circ \) around the y-axis, and \( \psi = 60^\circ \) around the z-axis.
- Translate the point by \( (t_x, t_y, t_z) = (10, 5, 3) \).

1. **Calculate Rotation Matrices**:
   - \( R_x(30^\circ) \)
   - \( R_y(45^\circ) \)
   - \( R_z(60^\circ) \)

2. **Combine Rotations**:
   \[
   R = R_z(60^\circ) \times R_y(45^\circ) \times R_x(30^\circ)
   \]

3. **Create Translation Matrix**:
   \[
   T = \begin{bmatrix} 1 & 0 & 0 & 10 \\ 0 & 1 & 0 & 5 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 1 \end{bmatrix}
   \]

4. **Combine Rotation and Translation**:
   \[
   M = T \times R
   \]

5. **Apply Transformation**:
   \[
   P' = M \times \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}
   \]

This will give the new coordinates of the point \( P' \) after rotation and translation.
