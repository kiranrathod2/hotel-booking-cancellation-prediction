import streamlit as st
import pickle as pk
import pandas as pd

classifier = pk.load(open("classifier_hotel_booking.pkl", "rb"))
scaler = pk.load(open("scaler_hotel_booking.pkl", "rb"))
encoders = pk.load(open("encoders.pkl", "rb"))

st.header("🏨 Hotel Booking Cancellation Prediction")

hotel = st.radio("Select Hotel", encoders["hotel"].classes_)
meal = st.selectbox("Meal", encoders["meal"].classes_)
country = st.selectbox("Country", encoders["country"].classes_)
market = st.selectbox("Market Segment", encoders["market_segment"].classes_)
channel = st.selectbox("Distribution Channel", encoders["distribution_channel"].classes_)
reserved_room = st.selectbox("Reserved Room Type", encoders["reserved_room_type"].classes_)
deposit_type = st.selectbox("Deposit Type", encoders["deposit_type"].classes_)
customer_type = st.selectbox("Customer Type", encoders["customer_type"].classes_)

lead_time = st.slider("Lead Time (days)", 0, 1000, 100)
adults = st.number_input("Adults", 1, 10, 2)
children = st.number_input("Children", 0, 10, 0)
babies = st.number_input("Babies", 0, 5, 0)
weekend_nights = st.slider("Weekend Nights Stay", 0, 10, 1)
week_nights = st.slider("Week Nights Stay", 0, 20, 3)
booking_changes = st.number_input("Booking Changes", 0, 10, 0)
waiting_days = st.number_input("Days in Waiting List", 0, 100, 0)
adr = st.number_input("ADR (Average Daily Rate)", 0.0, 500.0, 100.0, 5.0)
parking = st.number_input("Required Parking Spaces", 0, 5, 0)
special_requests = st.number_input("Total Special Requests", 0, 5, 0)
is_repeated = st.radio("Repeated Guest?", [0, 1])
prev_cancellations = st.number_input("Previous Cancellations", 0, 10, 0)
prev_not_canceled = st.number_input("Previous Bookings Not Canceled", 0, 20, 0)

hotel = encoders["hotel"].transform([hotel])[0]
meal = encoders["meal"].transform([meal])[0]
country = encoders["country"].transform([country])[0]
market = encoders["market_segment"].transform([market])[0]
channel = encoders["distribution_channel"].transform([channel])[0]
reserved_room = encoders["reserved_room_type"].transform([reserved_room])[0]
deposit_type = encoders["deposit_type"].transform([deposit_type])[0]
customer_type = encoders["customer_type"].transform([customer_type])[0]

if st.button("Predict"):

    hotel_data = pd.DataFrame([[hotel, lead_time, weekend_nights, week_nights, adults, children, babies,
                                    meal, country, market, channel,
                                    is_repeated, prev_cancellations, prev_not_canceled,
                                    reserved_room, booking_changes, deposit_type,
                                    waiting_days, customer_type, adr, parking, special_requests,]], 
                                    columns=['hotel', 'lead_time', 'stays_in_weekend_nights', 'stays_in_week_nights', 
                                             'adults', 'children', 'babies',
                                            'meal', 'country', 'market_segment', 'distribution_channel',
                                            'is_repeated_guest', 'previous_cancellations', 
                                            'previous_bookings_not_canceled',
                                            'reserved_room_type', 'booking_changes', 'deposit_type',
                                            'days_in_waiting_list', 'customer_type', 'adr', 
                                            'required_car_parking_spaces', 'total_of_special_requests'])

    scaled_data = scaler.transform(hotel_data)


    prediction = classifier.predict(scaled_data)

    if prediction[0] == 1:
        st.error("❌ The hotel booking is likely to be CANCELED.")
    else:
        st.success("✅ The hotel booking is likely to be HONORED.")


