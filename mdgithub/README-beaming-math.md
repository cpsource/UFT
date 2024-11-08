[Home](https://t2m.io/VwvDcuw)
---

Here is the **Wolfram Language** code that visualizes the relativistic beaming effect with sliders for $v$ (velocity as a fraction of $c$) and $\theta$ (angle of observation). It displays both the intrinsic intensity $I_0$ and the observed intensity $I_{\text{obs}}$:

```wolfram
Manipulate[
 Module[{gamma, I0, Iobs},
  (* Lorentz factor *)
  gamma = 1/Sqrt[1 - (v/c)^2];
  
  (* Intrinsic intensity *)
  I0 = 1; (* Normalized to 1 for simplicity *)
  
  (* Observed intensity formula *)
  Iobs = I0 * (1 - (v/c) * Cos[theta]) / gamma^3;
  
  (* Display the results *)
  Column[{
    "Relativistic Beaming Effect",
    "Lorentz Factor (γ) = " <> ToString[N[gamma]],
    "Intrinsic Intensity (I₀) = " <> ToString[N[I0]],
    "Observed Intensity (I(obs)) = " <> ToString[N[Iobs]],
    Plot3D[
     I0 * (1 - (v/c) * Cos[phi]) / (1/Sqrt[1 - (v/c)^2])^3, 
     {phi, 0, Pi}, {v, 0.01, 0.99 c},
     PlotRange -> All,
     AxesLabel -> {"θ", "v/c", "I(obs)"},
     ColorFunction -> "TemperatureMap",
     MeshFunctions -> {#3 &},
     MeshStyle -> {{Thick, Blue}}
    ]
   }]
 ],
 {{v, 0.1, "Velocity v (as a fraction of c)"}, 0.01, 0.99 c, ControlType -> Slider},
 {{theta, Pi/4, "Angle θ (in radians)"}, 0, Pi, ControlType -> Slider},
 Initialization :> (
   c = 1; (* Speed of light placeholder *)
 )
]
```

### Explanation:
- **`gamma`** is the **Lorentz factor** calculated as $\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}$.
- **`I0`** is the intrinsic intensity, normalized to 1 for simplicity.
- **`Iobs`** is the observed intensity given by the formula:
  $$I_{\text{obs}} = I_0 \cdot \left(\frac{1 - \frac{v}{c} \cos \theta}{\gamma^3}\right)$$
- The **`Plot3D`** shows the variation of observed intensity $I_{\text{obs}}$ as a function of $\theta$ (angle) and $v/c$ (velocity as a fraction of the speed of light).

### Behavior:
- Use the **slider for $v$** to adjust the velocity of the object relative to the speed of light.
- Use the **slider for $\theta$** to change the observation angle in radians.
- The output displays:
  - The calculated **Lorentz factor $\gamma$**.
  - The **intrinsic intensity $I_0$** (set to 1 for comparison).
  - The **observed intensity $I_{\text{obs}}$** based on the current values of $v$ and $\theta$.

### Visual Insight:
- The plot shows how the **observed intensity** changes with velocity and angle due to **relativistic beaming**.
- As $v$ approaches $c$, the intensity becomes more concentrated in the forward direction (small $\theta$).

Feel free to customize or extend this code further based on your needs!


---

[README-lorentz-contraction.md](https://t2m.io/eALrAKC)
