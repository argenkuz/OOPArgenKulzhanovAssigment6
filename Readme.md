# BMIApp

## Overview
BMIApp is a simple Python application that calculates the Body Mass Index (BMI) based on user input for weight and height. The application uses PyQt6 for the graphical user interface.

## Classes and Methods

### `BMIApp`
- **Purpose:** Main application window class that inherits from `QMainWindow` and `Ui_MainWindow`.
- **Methods:**
  - `__init__(self)`: Initializes the main window and connects the button click to the `calculate_bmi` method.
  - `calculate_bmi(self)`: Calculates the BMI based on the input weight and height, and displays the result.
  - `update_label(self, bmi)`: Updates the label based on the BMI value.
  - `clear_fields(self)`: Clears all input fields and output labels.
  - `show_information(self)`: Displays information about how to use the application.
  - `save_file(self)`: Saves the BMI and conversion results to a file.
    
## How to Run the Code
### 1.Run the main script:
```sh
   python main.py
```
### 2.Enter the weight and height in the respective fields.
### 3.Click the "Click Me" button to calculate the BMI.
### 4.To convert metric to feet, enter the value in centimeters in the input field and click the button next to the input field.
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
<img width="796" alt="Снимок экрана 2025-03-04 в 15 46 42" src="https://github.com/user-attachments/assets/e53f475e-a663-4321-8648-1317c4d9c14c" />


### Example 2
<img width="798" alt="Снимок экрана 2025-03-04 в 15 49 07" src="https://github.com/user-attachments/assets/0b7d6c83-c158-41d3-8957-63de3eb8b74c" />


Features
- Calculate BMI based on weight and height.
- Convert height from metric to feet.
- Clear input fields and output labels.
- Display information about how to use the application.
- Save BMI and conversion results to a file.
