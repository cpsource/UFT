Yes, you are absolutely correct! A **static charge at \( P_1 \)** that is **moving relative to \( P_2 \)** would indeed induce a **magnetic field** at \( P_2 \), even though the charge is "static" in its own frame. This is a direct result of the **relativistic relationship** between electric and magnetic fields.

---

### **1. Magnetic Field Due to a Moving Charge**
When a charge moves relative to an observer, it generates a magnetic field \( \vec{B} \), which can be calculated using the **Biot-Savart Law for a moving point charge**:

\[
\vec{B} = \frac{\mu_0}{4 \pi} \frac{q \vec{v} \times \vec{r}}{r^3}
\]

Where:
- \( q \): The magnitude of the charge at \( P_1 \).
- \( \vec{v} \): The velocity of \( P_1 \) relative to \( P_2 \).
- \( \vec{r} \): The vector from \( P_1 \) to \( P_2 \).
- \( r = |\vec{r}| \): The distance between \( P_1 \) and \( P_2 \).
- \( \mu_0 \): The permeability of free space.

---

### **2. Direction of the Magnetic Field**
The direction of \( \vec{B} \) is determined by the **right-hand rule**:
- Point your fingers in the direction of \( \vec{v} \) (velocity of the charge).
- Curl them toward \( \vec{r} \) (position vector from the charge to the observer).
- Your thumb points in the direction of \( \vec{B} \).

Thus, the magnetic field forms circular loops around the velocity vector of the charge.

---

### **3. Observations at \( P_2 \)**
At \( P_2 \), the magnetic field \( \vec{B} \):
- Is perpendicular to both the velocity \( \vec{v} \) of the charge and the vector \( \vec{r} \).
- Varies in magnitude as \( 1/r^2 \), because:
  - \( \vec{v} \) is constant for a uniformly moving charge.
  - The \( \sin \theta \) dependence from \( \vec{v} \times \vec{r} \) is embedded in the circular geometry.

---

### **4. Induced Voltage in the Wire**
If you have a wire at \( P_2 \), the moving charge at \( P_1 \) will induce a voltage in the wire via the **changing magnetic flux**. The induced voltage \( V \) depends on:
1. **The orientation of the wire** relative to \( \vec{B} \).
2. **The length of the wire** and its exposure to the field.

For a stationary wire at \( P_2 \):
- **No voltage is induced** if the magnetic field is constant (no change in flux through the loop).
- **Voltage is induced** if the charge at \( P_1 \) accelerates, causing a time-varying \( \vec{B} \).

---

### **5. How Does the Magnetic Field Arise?**
In special relativity, electric and magnetic fields are components of the **same entity**, the **electromagnetic field tensor**:
\[
F_{\mu \nu} = 
\begin{bmatrix}
0 & E_x & E_y & E_z \\
-E_x & 0 & -B_z & B_y \\
-E_y & B_z & 0 & -B_x \\
-E_z & -B_y & B_x & 0
\end{bmatrix}
\]

In one frame:
- A **stationary charge** generates only an electric field (\( \vec{E} \)).
- In another frame, where the charge is **moving**, part of this electric field transforms into a magnetic field (\( \vec{B} \)).

This transformation is given by:
\[
\vec{B} = \frac{\vec{v} \times \vec{E}}{c^2}
\]

---

### **6. Key Points**
1. A **static charge** that moves relative to \( P_2 \) generates a magnetic field \( \vec{B} \).
2. The magnetic field arises from the relative motion of the charge, even though it is "static" in its own frame.
3. The direction of \( \vec{B} \) depends on the velocity \( \vec{v} \) and the position vector \( \vec{r} \).
4. At \( P_2 \), you can detect this \( \vec{B} \) indirectly by measuring the force on moving charges (e.g., in a wire) or the induced voltage due to changing flux.

---

### **Summary**
Yes, \( P_2 \) would observe a magnetic field due to the motion of \( P_1 \)’s static charge. The direction and magnitude of this field depend on the relative motion and spatial geometry. This is a fundamental result of the interplay between electric and magnetic fields in special relativity.

