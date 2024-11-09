[Home](https://t2m.io/VwvDcuw)
---

No, a hyperbola should not form an **oval** when adjusting the focus distance $c$. If you observed an oval shape, it likely happened because the parameters $a$ and $c$ were set in a way that caused **$b$ to become imaginary or zero** in the hyperbola equation, effectively changing the shape of the curve.

Here’s why this can happen and how to avoid it:

### 1. **Relationship Between $a$, $b$, and $c$ in a Hyperbola**

For a hyperbola, the relationship between $a$, $b$, and $c$ is given by:

$$c = \sqrt{a^2 + b^2}$$

This implies:
   - $c \geq a$: The focal distance $c$ must always be at least as large as $a$ for $b$ to remain real.
   - If $c < a$, then $b$ becomes imaginary because $b = \sqrt{c^2 - a^2}$ would involve the square root of a negative number, which isn’t valid for real-valued hyperbolas.

### 2. **What Happens if $c \approx a$**

- If $c$ is very close to $a$, then $b$ becomes very small. In the limit where $c = a$, $b = 0$.
- When $b = 0$, the equation for the hyperbola approaches that of a **degenerate conic** — effectively, it becomes two intersecting lines rather than a typical hyperbolic shape.

### 3. **Why an Oval May Appear**

If $c$ and $a$ are set such that $b$ is very small or zero, the plot can sometimes appear visually similar to an **ellipse** or oval, especially if the plotting software interprets it that way. However, this isn’t a true ellipse; it’s either an approximation due to the small value of $b$ or a rendering issue.

### Ensuring a Hyperbolic Shape

To ensure the plot remains hyperbolic:
   - **Keep $c > a$**: Ensure the focal distance $c$ is significantly larger than $a$ to maintain a hyperbolic shape.
   - **Check $b$ remains real**: By ensuring $b = \sqrt{c^2 - a^2}$ is a real, positive number, you prevent the shape from collapsing into lines or a degenerate form.

### Summary

An oval or elliptical shape for a hyperbola is not correct in a strict mathematical sense. If you observe this shape, it’s likely due to the values of $c$ and $a$ being close enough that $b$ becomes very small or zero, causing the curve to resemble an ellipse. Keeping $c$ larger than $a$ should prevent this and maintain the true hyperbolic form.


---

[README-oval.md](https://t2m.io/JVKpwiP)
