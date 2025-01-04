The **Euler-Lagrange equation** is a fundamental equation in calculus of variations and plays a key role in physics, especially in the principle of least action in classical mechanics. It provides a way to find the function that minimizes (or extremizes) a functional.

---

### **Mathematical Formulation**
Suppose we have a functional \( J[y] \) defined as:

\[
J[y] = \int_{x_1}^{x_2} L(x, y, y') \, dx
\]

Here:
- \( L(x, y, y') \): The **Lagrangian**, a function of \( x \), \( y(x) \), and \( y'(x) = \frac{dy}{dx} \).
- \( y(x) \): The function to be determined that extremizes the functional \( J[y] \).
- \( y'(x) \): The derivative of \( y(x) \) with respect to \( x \).

The **Euler-Lagrange equation** is given by:

\[
\frac{\partial L}{\partial y} - \frac{d}{dx} \left( \frac{\partial L}{\partial y'} \right) = 0
\]

This equation provides a condition that \( y(x) \) must satisfy to make \( J[y] \) stationary (i.e., a minimum, maximum, or saddle point).

---

### **Derivation (Overview)**
The derivation comes from the principle that small variations in \( y(x) \) around the extremal function \( y(x) \) should not change the value of \( J[y] \) to first order.

1. Start with the perturbed function:
   \[
   y(x) \to y(x) + \epsilon \eta(x)
   \]
   where \( \eta(x) \) is a small arbitrary variation that vanishes at \( x_1 \) and \( x_2 \), and \( \epsilon \) is a small parameter.

2. Substitute into the functional:
   \[
   J[y] = \int_{x_1}^{x_2} L(x, y + \epsilon \eta, y' + \epsilon \eta') \, dx
   \]

3. Expand to first order in \( \epsilon \), and require the variation \( \delta J \) to be zero.

4. After integration by parts and using the boundary conditions (\( \eta(x_1) = \eta(x_2) = 0 \)), you arrive at the Euler-Lagrange equation.

---

### **Applications**

1. **Classical Mechanics**:
   In the Lagrangian formulation of mechanics, the functional represents the action:
   \[
   S = \int_{t_1}^{t_2} L(q, \dot{q}, t) \, dt
   \]
   where \( L = T - V \) is the Lagrangian (kinetic energy minus potential energy). The Euler-Lagrange equation gives the equations of motion:
   \[
   \frac{\partial L}{\partial q} - \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) = 0
   \]

2. **Geodesics in Differential Geometry**:
   The shortest path between two points on a curved surface can be found by solving the Euler-Lagrange equation with the functional representing the arc length.

3. **Optics (Fermat's Principle)**:
   Light takes the path that extremizes the travel time. This principle leads to Euler-Lagrange equations that describe the path of light in different media.

4. **Field Theory**:
   In physics, fields like the electromagnetic field are governed by actions that are extremized. The Euler-Lagrange equations generalize to fields, leading to equations like Maxwell's equations.

---

### **Example: Brachistochrone Problem**
Find the curve \( y(x) \) that minimizes the time of descent for a particle under gravity. The Lagrangian is:
\[
L = \sqrt{1 + y'^2} / \sqrt{y}
\]

The Euler-Lagrange equation for this \( L \) gives the equation of the cycloid, which is the solution.

---

Would you like an example worked out step by step or further explanation of a specific application?

