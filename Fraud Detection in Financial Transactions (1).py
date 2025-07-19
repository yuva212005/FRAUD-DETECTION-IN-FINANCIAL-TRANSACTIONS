import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Define correct password
CORRECT_PASSWORD = "2"

# Track wrong attempts
attempts = 0
MAX_ATTEMPTS = 3

# Sample training data for fraud detection (features: amount, transaction_type, location_code)
# For simplicity, transaction_type and location_code are encoded as integers
X_train = np.array([
    [100, 0, 1],
    [2000, 1, 2],
    [50, 0, 1],
    [5000, 1, 3],
    [20, 0, 1],
    [3000, 1, 2],
    [10, 0, 1],
    [7000, 1, 3]
])
y_train = np.array([0, 1, 0, 1, 0, 1, 0, 1])  # 0 = legitimate, 1 = fraud

# Train a simple RandomForest model
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

def predict_fraud(amount, transaction_type, location_code):
    features = np.array([[amount, transaction_type, location_code]])
    prediction = model.predict(features)
    return prediction[0]

# Function to check password
def check_password():
    global attempts
    entered_password = password_entry.get()
    
    if entered_password == CORRECT_PASSWORD:
        messagebox.showinfo("Access Granted", "Welcome! Transaction access granted.")
        attempts = 0  # Reset after success
        root.withdraw()  # Hide login window
        open_fraud_detection_window()
    else:
        attempts += 1
        messagebox.showwarning("Access Denied", f"Wrong password! Attempt {attempts} of {MAX_ATTEMPTS}.")
        
        if attempts >= MAX_ATTEMPTS:
            messagebox.showerror("ALERT 🚨", "Multiple failed attempts detected!\nThis attempt has been flagged as suspicious.")
            # Optionally: Log the event, send email alert, block access, etc.

def open_fraud_detection_window():
    fraud_window = tk.Toplevel()
    fraud_window.title("Fraud Detection")
    fraud_window.geometry("400x350")
    fraud_window.configure(bg="#f0f4f8")

    style = ttk.Style(fraud_window)
    style.configure("TLabel", background="#f0f4f8", font=("Helvetica", 11))
    style.configure("TEntry", font=("Helvetica", 11))
    style.configure("TButton", font=("Helvetica", 11), foreground="#ffffff", background="#007acc")
    style.map("TButton",
              foreground=[('active', '#ffffff')],
              background=[('active', '#005f99')])

    # Frame for padding
    frame = ttk.Frame(fraud_window, padding=20, style="TFrame")
    frame.pack(fill=tk.BOTH, expand=True)

    ttk.Label(frame, text="Enter Transaction Amount:").pack(pady=5, anchor="w")
    amount_entry = ttk.Entry(frame, width=30)
    amount_entry.pack(pady=5)

    ttk.Label(frame, text="Transaction Type (0=debit, 1=credit):").pack(pady=5, anchor="w")
    type_entry = ttk.Entry(frame, width=30)
    type_entry.pack(pady=5)

    ttk.Label(frame, text="Location Code (1, 2, or 3):").pack(pady=5, anchor="w")
    location_entry = ttk.Entry(frame, width=30)
    location_entry.pack(pady=5)

    def on_predict():
        try:
            amount = float(amount_entry.get())
            transaction_type = int(type_entry.get())
            location_code = int(location_entry.get())
            if transaction_type not in [0, 1] or location_code not in [1, 2, 3]:
                messagebox.showerror("Input Error", "Transaction type must be 0 or 1, location code must be 1, 2, or 3.")
                return
            result = predict_fraud(amount, transaction_type, location_code)
            if result == 1:
                messagebox.showwarning("Fraud Detection Result", "Warning: This transaction is likely FRAUDULENT!")
            else:
                messagebox.showinfo("Fraud Detection Result", "This transaction appears LEGITIMATE.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")

    # New entry for recipient account
    ttk.Label(frame, text="Recipient Account:").pack(pady=5, anchor="w")
    recipient_entry = ttk.Entry(frame, width=30)
    recipient_entry.pack(pady=5)

    def on_pass_amount():
        try:
            amount = float(amount_entry.get())
            transaction_type = int(type_entry.get())
            location_code = int(location_entry.get())
            recipient = recipient_entry.get().strip()
            if not recipient:
                messagebox.showerror("Input Error", "Please enter a recipient account.")
                return
            if transaction_type not in [0, 1] or location_code not in [1, 2, 3]:
                messagebox.showerror("Input Error", "Transaction type must be 0 or 1, location code must be 1, 2, or 3.")
                return
            result = predict_fraud(amount, transaction_type, location_code)
            if result == 1:
                messagebox.showwarning("Transfer Blocked", "This transaction is flagged as FRAUDULENT! Transfer blocked.")
            else:
                messagebox.showinfo("Transfer Successful", f"Transaction amount ${amount:.2f} passed to account '{recipient}' successfully.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")

    predict_btn = ttk.Button(frame, text="Check Fraud", command=on_predict)
    predict_btn.pack(pady=10)

    pass_btn = ttk.Button(frame, text="Pass Amount", command=on_pass_amount)
    pass_btn.pack(pady=10)

# Create GUI for login
root = tk.Tk()
root.title("Fraud Protection - Secure Login")
root.geometry("320x200")
root.configure(bg="#e1e5ea")

style = ttk.Style(root)
style.configure("TLabel", background="#e1e5ea", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12), foreground="#ffffff", background="#007acc")
style.map("TButton",
          foreground=[('active', '#ffffff')],
          background=[('active', '#005f99')])

login_frame = ttk.Frame(root, padding=30, style="TFrame")
login_frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(login_frame, text="Enter your password:").pack(pady=10)
password_entry = ttk.Entry(login_frame, show="*", width=30)
password_entry.pack(pady=10)

submit_btn = ttk.Button(login_frame, text="Submit", command=check_password)
submit_btn.pack(pady=15)

root.mainloop()
