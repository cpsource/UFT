You’re absolutely correct: **measuring the voltage of a battery measures its potential energy per unit charge, not the total energy stored in the battery**. Let's break this down and clarify how voltage relates to energy, and why measuring the energy in a battery requires more than just checking the voltage.

---

### 1. **Voltage vs. Energy**
- **Voltage** (\(V\)): Measures the electric potential difference between two points in a circuit, or the "push" the battery can exert on charges.
  - Units: Volts (\(1 \, \text{V} = 1 \, \text{Joule}/\text{Coulomb}\)).
  - It indicates how much energy each unit of charge will gain or lose when it moves through the circuit.
  
- **Energy** (\(E\)): The total work the battery can do, which depends on both the voltage and the amount of charge it can deliver.
  - Units: Joules (\(1 \, \text{J} = 1 \, \text{Coulomb} \times \text{Volt}\)).
  - Energy is given by:
    \[
    E = Q \cdot V
    \]
    where:
    - \(Q\): Total charge the battery can deliver (measured in Coulombs),
    - \(V\): Voltage of the battery.

Thus, voltage alone doesn’t tell us how much energy is in the battery. To determine the energy, we also need to know how much charge (\(Q\)) the battery can provide.

---

### 2. **Why Voltage Alone is Insufficient**
- A fully charged battery and a nearly depleted battery can have the same voltage under no load. This is because voltage represents potential energy, but it doesn't account for the remaining capacity (the total charge available for work).
- The battery’s energy depends on its **state of charge (SOC)**, which indicates how much of the stored charge is still available. SOC requires additional measurements, like:
  - The battery’s internal resistance.
  - How voltage drops under load.
  - The battery's capacity (ampere-hours, \(Ah\)).

---

### 3. **How to Measure the Energy in a Battery**
To estimate the total energy in a battery, you need:
1. **Voltage (\(V\))**: Measure the battery’s potential difference.
2. **Capacity (\(Q\))**: Determine how much charge the battery can deliver. This is usually expressed in ampere-hours (\(Ah\)):
   - 1 \(Ah = 3600 \, \text{Coulombs}\).
3. Combine them:
   - Energy (\(E\)) in joules: 
     \[
     E = Q \cdot V
     \]
   - Energy (\(E\)) in watt-hours:
     \[
     E_{\text{Wh}} = V \cdot \text{Capacity (Ah)}
     \]

#### Practical Example:
- A 12V battery with a capacity of 100Ah has an energy capacity of:
  \[
  E = 12 \, \text{V} \cdot 100 \, \text{Ah} = 1200 \, \text{Wh}.
  \]

---

### 4. **Voltage Under Load vs. Open Circuit**
- Measuring voltage under **no load** gives the open-circuit voltage, which provides a rough idea of the battery’s charge.
- Measuring voltage under **load** provides more information about the battery’s ability to deliver energy. A significant voltage drop under load can indicate that the battery’s capacity is low or that it’s nearing depletion.

---

### 5. **Energy vs. Power**
- **Energy**: Total work a battery can do (\(E = V \cdot Q\)).
- **Power**: The rate at which energy is delivered (\(P = V \cdot I\), where \(I\) is the current in amperes).

---

### 6. **How This Relates to Measurement**
- Measuring voltage alone gives insight into the battery’s "pressure" but not its "reservoir size."
- To measure total energy, you must combine voltage with the battery’s total deliverable charge or capacity, often determined by discharging the battery under controlled conditions.

---

### Summary
You are correct: measuring voltage only indicates **potential energy per charge unit**, not the total stored energy. To measure the total energy in a battery, we need both the voltage and the available charge (capacity). Voltage is an important diagnostic tool, but it is only part of the story when assessing a battery's total energy content.

