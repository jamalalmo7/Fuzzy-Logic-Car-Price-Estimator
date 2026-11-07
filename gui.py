import tkinter as tk
from tkinter import messagebox
from fuzzy_engine import calculate_car_price

class CarPriceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fuzzy Car Price Estimator")
        self.root.geometry("400x350")
        self.root.configure(bg="#2c3e50")
        self.root.resizable(False, False)

        title = tk.Label(root, text="Car Price Calculator", font=("Arial", 18, "bold"),
                        bg="#2c3e50", fg="white")
        title.pack(pady=20)

        frame = tk.Frame(root, bg="#34495e", bd=2, relief="groove")
        frame.pack(padx=30, pady=10, fill="x")

        tk.Label(frame, text="Manufacturing Year:", font=("Arial", 12),
                 bg="#34495e", fg="white").grid(row=0, column=0, padx=10, pady=8, sticky="w")
        self.year_entry = tk.Entry(frame, font=("Arial", 12), width=15, bg="#ecf0f1")
        self.year_entry.grid(row=0, column=1, padx=10, pady=8)
        self.year_entry.insert(0, "2020")

        tk.Label(frame, text="Mileage (km):", font=("Arial", 12),
                 bg="#34495e", fg="white").grid(row=1, column=0, padx=10, pady=8, sticky="w")
        self.mileage_entry = tk.Entry(frame, font=("Arial", 12), width=15, bg="#ecf0f1")
        self.mileage_entry.grid(row=1, column=1, padx=10, pady=8)
        self.mileage_entry.insert(0, "50000")

        calc_btn = tk.Button(root, text="Calculate Price", font=("Arial", 14, "bold"),
                             bg="#27ae60", fg="white", activebackground="#2ecc71",
                             cursor="hand2", command=self.calculate)
        calc_btn.pack(pady=15)

        self.result_label = tk.Label(root, text="", font=("Arial", 16, "bold"),
                                     bg="#2c3e50", fg="#f1c40f")
        self.result_label.pack(pady=10)

    def calculate(self):
        try:
            year_val = float(self.year_entry.get())
            mileage_val = float(self.mileage_entry.get())

            if not (2000 <= year_val <= 2026):
                messagebox.showerror("Error", "Year must be between 2000 and 2026")
                return

            if not (0 <= mileage_val <= 300000):
                messagebox.showerror("Error", "Mileage must be between 0 and 300,000 km")
                return

            price = calculate_car_price(year_val, mileage_val)
            self.result_label.config(text=f"Estimated Price: ${price:,.2f}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CarPriceApp(root)
    root.mainloop()
