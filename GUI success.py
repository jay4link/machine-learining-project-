#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
from tkinter import ttk, messagebox
import joblib

# Load the saved model and scaler
gb_classifier = joblib.load("phishing_gb_model.pkl")
scaler = joblib.load("phishing_scaler.pkl")

# Function to make a prediction using the model
def make_prediction():
    try:
        input_features = [
            float(sfh_entry.get()),
            float(pop_up_window_entry.get()),
            float(ssl_final_state_entry.get()),
            float(request_url_entry.get()),
            float(url_of_anchor_entry.get()),
            float(web_traffic_entry.get()),
            float(url_length_entry.get()),
            float(age_of_domain_entry.get()),
            float(having_ip_address_entry.get()),
        ]

        input_features_scaled = scaler.transform([input_features])
        prediction = gb_classifier.predict(input_features_scaled)[0]

        if prediction == 1:
            result = "Phishing"
        else:
            result = "Not Phishing"

        messagebox.showinfo("Prediction", f"The website is predicted to be {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values")
        
        
        


# In[4]:


# Add feature names to X
X.columns = ['SFH', 'popUpWidnow', 'SSLfinal_State', 'Request_URL', 'URL_of_Anchor',
             'web_traffic', 'URL_Length', 'age_of_domain', 'having_IP_Address']

# Normalize the input features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# In[ ]:



# Create the main window
root = tk.Tk()
root.title("Phishing Detection")
root.geometry("400x400")

# Create labels and input fields
sfh_label = ttk.Label(root, text="SFH:")
sfh_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")
sfh_entry = ttk.Entry(root)
sfh_entry.grid(row=0, column=1, pady=5, padx=5)

pop_up_window_label = ttk.Label(root, text="Pop-up Window:")
pop_up_window_label.grid(row=1, column=0, pady=5, padx=5, sticky="w")
pop_up_window_entry = ttk.Entry(root)
pop_up_window_entry.grid(row=1, column=1, pady=5, padx=5)

ssl_final_state_label = ttk.Label(root, text="SSL Final State:")
ssl_final_state_label.grid(row=2, column=0, pady=5, padx=5, sticky="w")
ssl_final_state_entry = ttk.Entry(root)
ssl_final_state_entry.grid(row=2, column=1, pady=5, padx=5)

request_url_label = ttk.Label(root, text="Request URL:")
request_url_label.grid(row=3, column=0, pady=5, padx=5, sticky="w")
request_url_entry = ttk.Entry(root)
request_url_entry.grid(row=3, column=1, pady=5, padx=5)

url_of_anchor_label = ttk.Label(root, text="URL of Anchor:")
url_of_anchor_label.grid(row=4, column=0, pady=5, padx=5, sticky="w")
url_of_anchor_entry = ttk.Entry(root)
url_of_anchor_entry.grid(row=4, column=1, pady=5, padx=5)

web_traffic_label = ttk.Label(root, text="Web Traffic:")
web_traffic_label.grid(row=5, column=0, pady=5, padx=5, sticky="w")
web_traffic_entry = ttk.Entry(root)
web_traffic_entry.grid(row=5, column=1, pady=5, padx=5)

url_length_label = ttk.Label(root, text="URL Length:")
url_length_label.grid(row=6, column=0, pady=5, padx=5, sticky="w")
url_length_entry = ttk.Entry(root)
url_length_entry.grid(row=6, column=1, pady=5, padx=5)

age_of_domain_label = ttk.Label(root, text="Age of Domain:")
age_of_domain_label.grid(row=7, column=0, pady=5, padx=5, sticky="w")
age_of_domain_entry = ttk.Entry(root)
age_of_domain_entry.grid(row=7, column=1, pady=5, padx=5)

having_ip_address_label = ttk.Label(root, text="Having IP Address:")
having_ip_address_label.grid(row=8, column=0, pady=5, padx=5, sticky="w")
having_ip_address_entry = ttk.Entry(root)
having_ip_address_entry.grid(row=8, column=1, pady=5, padx=5)

# Create the Predict button and bind it to the make_prediction function
predict_button = ttk.Button(root, text="Predict", command=make_prediction)
predict_button.grid(row=9, column=0, columnspan=2, pady=20)

# Run the main event loop
root.mainloop()


# In[ ]:




