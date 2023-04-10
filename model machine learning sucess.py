#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler


# In[15]:


data = pd.read_csv('Website_Phishing[1].csv')


# In[16]:


print(data.columns)


# In[ ]:





# In[ ]:





# In[19]:


# Display the first few rows of the dataset
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Visualize the distribution of target variable (phishing or not)
sns.countplot(x='Result', data=data)
plt.show()


# In[20]:


X = data.drop('Result', axis=1)
y = data['Result']


# In[23]:


# Normalize the input features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# In[24]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# In[25]:


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# In[26]:




# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Step 4: Create and train the gradient boosting model
gb_classifier = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gb_classifier.fit(X_train, y_train)

# Step 5: Evaluate the model
y_pred = gb_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{confusion_mat}")
print(f"Classification Report:\n{report}")

# Step 6: Save the model and scaler for future use
import joblib

joblib.dump(gb_classifier, "phishing_gb_model.pkl")
joblib.dump(scaler, "phishing_scaler.pkl")

print("Model and scaler saved successfully.")


# In[ ]:




