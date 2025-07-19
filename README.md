#  Fraud Detection GUI Application

A desktop-based fraud detection system built with **Python**, **Tkinter**, and a **Random Forest Classifier** from `scikit-learn`. This app simulates a secure login and uses machine learning to predict whether a transaction is fraudulent based on user input.

---

##  Overview

This project is designed as a simple simulation of a fraud protection system for financial transactions. It includes:

- A login screen with limited attempts
- A fraud detection window where users enter transaction details
- Real-time predictions using a machine learning model
- Blocking of transactions flagged as fraudulent

It demonstrates how **AI models** can integrate with GUI-based interfaces for intelligent decision-making.

---

## 🚀 Features

### 🔐 Secure Login
- Password-protected access
- Max 3 attempts before alert is triggered
- Option to block after repeated failures

### 🧠 Fraud Prediction Engine
- Based on transaction **amount**, **type**, and **location**
- Uses a `RandomForestClassifier` trained on sample data
- Instant feedback: LEGITIMATE or FRAUDULENT

### 💼 Transaction Management
- Users can "pass" (transfer) an amount to a recipient
- Fraudulent transactions are automatically blocked

---

## 🎯 Tech Stack

| Layer         | Tools Used            |
|---------------|------------------------|
| GUI           | Tkinter, ttk           |
| ML Model      | Scikit-learn (`RandomForestClassifier`) |
| Data Handling | NumPy                  |
| Language      | Python 3.x             |

---

## 🖼️ Screenshots

> Login Window  
> ![Login](https://via.placeholder.com/300x150?text=Login+Window)

> Fraud Detection Window  
> ![Fraud Detection](https://via.placeholder.com/400x300?text=Fraud+Detection+Window)

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fraud-detection-gui.git
   cd fraud-detection-gui
