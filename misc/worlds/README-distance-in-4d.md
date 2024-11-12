To calculate the distance between two points in 4-dimensional space, you use the **4D Euclidean distance formula**, which extends the familiar 3D distance formula by adding an extra coordinate. If you have two points, \( A = (w_1, x_1, y_1, z_1) \) and \( B = (w_2, x_2, y_2, z_2) \), the distance \( d \) between them is given by:

\[
d = \sqrt{(w_2 - w_1)^2 + (x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}
\]

### Step-by-Step Calculation

1. **Subtract corresponding coordinates** of the points:
   - \( \Delta w = w_2 - w_1 \)
   - \( \Delta x = x_2 - x_1 \)
   - \( \Delta y = y_2 - y_1 \)
   - \( \Delta z = z_2 - z_1 \)

2. **Square each difference**:
   - \( (\Delta w)^2 \)
   - \( (\Delta x)^2 \)
   - \( (\Delta y)^2 \)
   - \( (\Delta z)^2 \)

3. **Add up all the squared differences**:
   \[
   (\Delta w)^2 + (\Delta x)^2 + (\Delta y)^2 + (\Delta z)^2
   \]

4. **Take the square root** of the sum to get the distance:
   \[
   d = \sqrt{(\Delta w)^2 + (\Delta x)^2 + (\Delta y)^2 + (\Delta z)^2}
   \]

### Example Calculation

Suppose you have two points:
- \( A = (1, 2, 3, 4) \)
- \( B = (5, 6, 7, 8) \)

The distance \( d \) between \( A \) and \( B \) would be:

1. Find differences: 
   - \( \Delta w = 5 - 1 = 4 \)
   - \( \Delta x = 6 - 2 = 4 \)
   - \( \Delta y = 7 - 3 = 4 \)
   - \( \Delta z = 8 - 4 = 4 \)

2. Square each difference:
   - \( 4^2 = 16 \)

3. Sum the squares:
   \[
   16 + 16 + 16 + 16 = 64
   \]

4. Take the square root:
   \[
   d = \sqrt{64} = 8
   \]

So, the distance between \( A \) and \( B \) is \( 8 \). This formula generalizes to higher dimensions by adding more squared differences as needed.
