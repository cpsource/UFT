[Home](https://t2m.io/VwvDcuw)
---

To define a point along a **parabolic arc** given the **focal length** $f$, you can use the **standard form of a parabola** with the focus at $(0, f)$ and the directrix at $y = -f$.

For a parabola with its vertex at the origin and opening upwards, the equation in terms of $x$ and $y$ is:

$$y = \frac{x^2}{4f}$$

Here’s how you can define a point $(x, y)$ along this parabolic arc, given $f$ and a chosen $x$-coordinate.

### Steps to Define a Point on the Parabola

1. **Choose a Value for $x$**:
   - Select a value for $x$ to find the corresponding $y$-coordinate on the parabolic arc.

2. **Calculate $y$ Using the Parabola’s Equation**:
   - Substitute the $x$-value into the equation $y = \frac{x^2}{4f}$.

Thus, for a given $f$ and a chosen $x$-coordinate, the point $(x, y)$ on the parabola is:

$$(x, \, \frac{x^2}{4f})$$

### Wolfram Language Code to Define a Point

In the Wolfram Language, you can create a function to calculate the $y$-coordinate for a given $x$-coordinate and focal length $f$:

```wolfram
(* Define the y-coordinate on the parabola as a function of x and focal length f *)
y[x_, f_] := x^2 / (4 * f)

(* Example: Calculate a point on the parabola for x = 2 and focal length f = 1 *)
point = {2, y[2, 1]}
```

### Explanation

- `y[x_, f_] := x^2 / (4 * f)` defines the $y$-coordinate in terms of $x$ and $f$.
- `point = {2, y[2, 1]}` gives the coordinates of the point for $x = 2$ and $f = 1$. You can replace these values with any other values of $x$ and $f$ to get different points along the parabola.

### Plotting the Parabolic Arc

To plot the parabolic arc in Wolfram Language for a range of $x$-values, you could use:

```wolfram
Plot[y[x, 1], {x, -5, 5}, PlotRange -> All, AxesLabel -> {"x", "y"}, PlotLabel -> "Parabolic Arc"]
```

This would plot the parabolic arc for $f = 1$ over the range $x = -5$ to $x = 5$.

By adjusting $x$ and $f$, you can define any point along the parabolic arc.


---

[README-parabola-and-circle.md](https://t2m.io/rMgjma7)
