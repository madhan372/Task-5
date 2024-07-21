import tkinter as tk
from tkinter import ttk, messagebox
from forex_python.converter import CurrencyRates

# Function to perform currency conversion
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = "USD"
        to_currency = combo_currency.get()

        c = CurrencyRates()
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate

        label_result.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for amount.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to handle quit action
def quit_app():
    root.destroy()

# Create main application window
root = tk.Tk()
root.title("USD Currency Converter")

# Create widgets
label_amount = tk.Label(root, text="Enter amount in USD:")
entry_amount = tk.Entry(root, width=15)
label_currency = tk.Label(root, text="Select currency:")
combo_currency = ttk.Combobox(root, values=["EUR", "GBP", "JPY", "CAD", "AUD"])
button_convert = tk.Button(root, text="Convert", command=convert_currency)
label_result = tk.Label(root, text="Conversion result will appear here", wraplength=250, justify="center")

# Layout widgets using grid
label_amount.grid(row=0, column=0, padx=10, pady=10)
entry_amount.grid(row=0, column=1, padx=10, pady=10)
label_currency.grid(row=1, column=0, padx=10, pady=10)
combo_currency.grid(row=1, column=1, padx=10, pady=10)
button_convert.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Configure Combobox
combo_currency.current(0)  # Set default selection

# Bind Enter key to convert_currency function
root.bind('<Return>', lambda event=None: convert_currency())

# Run the main application loop
root.mainloop()
