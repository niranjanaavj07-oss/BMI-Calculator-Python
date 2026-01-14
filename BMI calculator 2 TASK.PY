import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        # BMI Category
        if bmi < 18.5:
            status = "Underweight"
        elif bmi < 24.9:
            status = "Normal"
        elif bmi < 29.9:
            status = "Overweight"
        else:
            status = "Obese"

        result_label.config(text=f"BMI: {bmi}")
        status_label.config(text=f"Status: {status}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x300")
root.resizable(False, False)

# Heading
title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Weight input
weight_label = tk.Label(root, text="Enter Weight (kg)")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

# Height input
height_label = tk.Label(root, text="Enter Height (meters)")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

# Calculate button
calc_button = tk.Button(
    root,
    text="Calculate BMI",
    bg="green",
    fg="white",
    command=calculate_bmi
)
calc_button.pack(pady=15)

# Result labels
result_label = tk.Label(root, text="BMI: ")
result_label.pack()

status_label = tk.Label(root, text="Status: ")
status_label.pack()

# Run app
root.mainloop()
