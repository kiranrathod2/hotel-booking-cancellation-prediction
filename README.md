# 🏨 **Hotel Booking Cancellation Prediction**

This project predicts whether a hotel booking will be **canceled or honored**, using machine learning.  
It is deployed as an **interactive Streamlit web app** that allows users to input booking details and instantly see the prediction.

---

## 🚀 **Project Overview**

This project analyzes hotel booking data to predict cancellations based on various customer and booking features.

---

## 🧠 **Machine Learning Model**

The backend model is trained using historical hotel booking data.

---

## 💻 **Tech Stack**

- **Python 3.8+**
- **Streamlit**
- **Pandas**
- **Scikit-learn**
- **Pickle**

---

## 🧾 **How to Run Locally**

1. Clone this repository:
   
   git clone https://github.com/<your-username>/hotel-booking-prediction.git
   cd hotel-booking-prediction
   
2. Create & activate a virtual environment

 -  macOS / Linux:

      python3 -m venv venv
   
      source venv/bin/activate

 - Windows (PowerShell):

      python -m venv venv
      .\venv\Scripts\Activate.ps1


 - Windows (cmd):

      python -m venv venv
      .\venv\Scripts\activate


5. Upgrade pip (optional)

   pip install --upgrade pip


6. Install dependencies (single step)

   pip install -r requirements.txt


   If you don’t have a requirements.txt, create one with the sample below.

7. Run the Streamlit app

   streamlit run hotel_booking_deploy.py


8. Open the app in your browser

   http://localhost:8501

**📦 Sample requirements.txt**
streamlit
pandas
scikit-learn
numpy


**🧩 Usage (what to input)**

The app UI asks for:

Hotel type, Meal, Country

Market Segment, Distribution Channel

Reserved Room Type, Deposit Type, Customer Type

Lead time, stay nights (weekend & week), adults, children, babies

Previous cancellations, previous bookings not canceled

ADR (average daily rate), required parking spaces, special requests, etc.

**Click Predict to see:**

✅ The booking is likely to be HONORED

❌ The booking is likely to be CANCELED

**📬 Contact**

GitHub: kiranrathod2

Email: kiranrathod2602@gmail.com

LinkedIn: www.linkedin.com/in/kiran-rathod-605919367


