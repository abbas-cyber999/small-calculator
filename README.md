# small-calculator
small calculator to do math
# 📘 Calculator Program  

This is a simple **Python-based Calculator** that allows the user to perform four basic arithmetic operations:  
- Addition  
- Subtraction  
- Multiplication  
- Division  

The program uses the **match-case** statement (Python 3.10+) to handle different operations.  

---

## ⚙️ How It Works  

1. The program displays a menu with 4 options:  
   ```
   Select operation:
   1. Addition (+)
   2. Subtraction (-)
   3. Multiplication (*)
   4. Division (/)
   ```
2. The user selects an operation by entering a number (1/2/3/4).  
3. The user then inputs two numbers.  
4. Based on the selected operation, the calculator performs the calculation and displays the result.  
5. If division by zero is attempted, an error message is displayed.  

---

## ▶️ Running the Program  

Run the Python script in your terminal:  

```bash
python calculator.py
```

---

## 📝 Example Input & Output  

### Example 1: Addition
**Input:**  
```
Enter choice (1/2/3/4): 1
Enter first number: 10
Enter second number: 5
```

**Output:**  
```
Result: 15.0
```

---

### Example 2: Subtraction
**Input:**  
```
Enter choice (1/2/3/4): 2
Enter first number: 20
Enter second number: 8
```

**Output:**  
```
Result: 12.0
```

---

### Example 3: Multiplication
**Input:**  
```
Enter choice (1/2/3/4): 3
Enter first number: 4
Enter second number: 6
```

**Output:**  
```
Result: 24.0
```

---

### Example 4: Division
**Input:**  
```
Enter choice (1/2/3/4): 4
Enter first number: 15
Enter second number: 3
```

**Output:**  
```
Result: 5.0
```

---

### Example 5: Division by Zero
**Input:**  
```
Enter choice (1/2/3/4): 4
Enter first number: 10
Enter second number: 0
```

**Output:**  
```
Error: Cannot divide by zero!
```

---

### Example 6: Invalid Input
**Input:**  
```
Enter choice (1/2/3/4): 7
Enter first number: 5
Enter second number: 3
```

**Output:**  
```
Invalid input!
```

---

✅ That’s it! You now have a working calculator in Python.
