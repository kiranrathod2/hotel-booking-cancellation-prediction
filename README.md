🏨 Hotel Booking Cancellation Prediction

This project predicts whether a hotel booking will be canceled or honored, using machine learning.
It is deployed as an interactive Streamlit web app that allows users to input booking details and instantly see the prediction.

🚀 Project Overview

This project analyzes hotel booking data to predict cancellations based on various customer and booking features like:

Lead time (days before arrival)

Stay duration (weekend & week nights)

Number of adults, children, and babies

Meal type, country, market segment, distribution channel

Deposit type, customer type, previous cancellations, and more

The model helps hotels anticipate cancellations and manage overbooking or marketing strategies more effectively.

🧠 Machine Learning Model

The backend model is trained using historical hotel booking data.
It uses:

Pre-trained classifier → classifier_hotel_booking.pkl

Feature scaler → scaler_hotel_booking.pkl

Label encoders → encoders.pkl

These components are loaded automatically in the Streamlit app.

💻 Tech Stack

Python 3.8+

Streamlit – UI framework for deployment

Pandas – Data manipulation

Scikit-learn – Model training & scaling

Pickle – Model and encoder serialization

🧩 Input Features in the App

Users can interactively set:

Hotel type, meal plan, country

Market segment, distribution channel

Reserved room type, deposit type, customer type

Lead time, number of adults/children/babies

Weekend & week nights stay duration

Previous cancellations & non-cancellations

Average Daily Rate (ADR)

Parking requirements, special requests, etc.

📊 Output

After clicking “Predict”, the app displays:

✅ “The booking is likely to be HONORED”

❌ “The booking is likely to be CANCELED”

🧾 How to Run Locally

Clone this repository:

git clone https://github.com/<your-username>/hotel-booking-prediction.git
cd hotel-booking-prediction


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run hotel_booking_deploy.py


Open your browser at http://localhost:8501

🗂️ Project Files
File	Description
hotel_booking_deploy.py	Streamlit app for model deployment
classifier_hotel_booking.pkl	Trained classification model
scaler_hotel_booking.pkl	Feature scaling object
encoders.pkl	Label encoders for categorical features
📈 Example Use Case

Hotels can use this tool to:

Predict potential cancellations in advance

Optimize revenue management

Adjust booking policies or promotional offers

🙌 Acknowledgements

Inspired by the Hotel Booking Demand Dataset (from Kaggle).
Built with ❤️ using Streamlit and Scikit-learn.
