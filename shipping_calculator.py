import streamlit as st

# Function to calculate air and sea freight prices
def calculate_freight_prices(actual_weight_kg, length_cm, width_cm, height_cm):
    # Air freight pricing details
    initial_cost_air = 19  # RMB for first 0.5kg
    additional_cost_air_per_05kg = 9.5  # RMB per additional 0.5kg

    # Sea freight pricing details
    cost_sea_per_kg = 8  # RMB per kg for sea freight

    # Calculate volumetric weight for air freight
    volumetric_weight_kg = (length_cm * width_cm * height_cm) / 6000

    # Determine which weight to use for air freight (volumetric or actual)
    air_freight_weight = max(volumetric_weight_kg, actual_weight_kg)

    # Calculate air freight cost
    first_05kg_air_cost = initial_cost_air
    remaining_weight_kg = air_freight_weight - 0.5
    additional_05kg_units = remaining_weight_kg / 0.5
    additional_05kg_air_cost = additional_05kg_units * additional_cost_air_per_05kg
    total_air_cost = first_05kg_air_cost + additional_05kg_air_cost

    # Calculate sea freight cost
    total_sea_cost = actual_weight_kg * cost_sea_per_kg

    return total_air_cost, total_sea_cost

# Streamlit UI
st.title("Freight Price Calculator")

# User inputs for weight and dimensions
weight = st.number_input("Enter the actual weight of the parcel (KG):", min_value=0.0, format="%.3f")
length = st.number_input("Enter the length of the parcel (cm):", min_value=0.0, format="%.1f")
width = st.number_input("Enter the width of the parcel (cm):", min_value=0.0, format="%.1f")
height = st.number_input("Enter the height of the parcel (cm):", min_value=0.0, format="%.1f")

# When the user clicks the button, calculate the prices
if st.button("Calculate Freight Prices"):
    air_cost, sea_cost = calculate_freight_prices(weight, length, width, height)
    st.write(f"### Total Air Freight Cost: {air_cost:.2f} RMB")
    st.write(f"### Total Sea Freight Cost: {sea_cost:.2f} RMB")
