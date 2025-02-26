# BMIApp

## Overview
BMIApp is a simple Python application that calculates the Body Mass Index (BMI) based on user input for weight and height. The application uses PyQt6 for the graphical user interface.

## Classes and Methods

### `BMIApp`
- **Purpose:** Main application window class that inherits from `QMainWindow` and `Ui_MainWindow`.
- **Methods:**
  - `__init__(self)`: Initializes the main window and connects the button click to the `calculate_bmi` method.
  - `calculate_bmi(self)`: Calculates the BMI based on the input weight and height, and displays the result.
    
## How to Run the Code
### 1.Run the main script:
```sh
   python main.py
```
### 2.Enter the weight and height in the respective fields.
### 3.Click the "Don't push Me" button to calculate the BMI.

## Sample Input/Output

### Example 1
- **Input:**
  - Weight: 70 kg
  - Height: 175 cm
- **Output:**
  - BMI: 22.9

### Example 2
- **Input:**
  - Weight: 85 kg
  - Height: 169 cm
- **Output:**
  - BMI: 29.8

## Screenshots

### Example 1
<img width="666" alt="Снимок экрана 2025-02-26 в 20 11 47" src="https://github.com/user-attachments/assets/0eff0ca1-4fd5-4353-ad50-7d83405b4806" />


### Example 2

<img width="654" alt="Снимок экрана 2025-02-26 в 20 12 09" src="https://github.com/user-attachments/assets/2401e5ad-394c-4c8a-8002-fd01bcf3cf09" />
