import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open("voting_model.pkl", "rb"))

def predict(area, quality, g_cars, rooms, m_area, 
            fireplaces, lot_area, exter_qual, h_qual, base_qual,
            k_qual, garage,  m_type):
    
    a = float(area)
    q = int(quality)
    g_cars = int(g_cars)
    rooms = int(rooms)
    m_area = float(m_area)
    fireplaces = int(fireplaces)
    lot_area = float(lot_area)
    exter_qual = str(exter_qual)
    h_qual = str(h_qual)
    base_qual = str(base_qual)
    k_qual = str(k_qual)
    garage = str(garage)
    m_type = str(m_type)
    
    data = [[a, q, g_cars, rooms, m_area, fireplaces, lot_area, exter_qual, h_qual, base_qual, k_qual, garage, m_type]]
    data = pd.DataFrame(data, columns = ['grand_area', 'OverallQual', 'GarageCars', 'total_rooms', 'MasVnrArea', 
                                         'Fireplaces', 'LotFrontage', 'ExterQual', 'HeatingQC', 'BsmtQual', 
                                         'KitchenQual', 'GarageFinish', 'MasVnrType'])
    
    prediction = int(np.exp(model.predict(data)))

    return prediction


def main():

    st.title("House Price Predictor ML Web App")
    st.subheader("@author: Mohammed Misbahullah Sheriff")

    head_html = """
    <div style="background-color:#7D3C98; padding:10px;">
    <h2 style="color:white; text-align:center;">HOUSE PRICE PREDICTOR</h2>
    </div>
    """
    st.markdown(head_html, unsafe_allow_html=True)

    a = st.text_input("House Area (square feet)", "3000")
    if float(a) > 15000:
        raise ValueError("House Area: Given input beyond limit")
    elif float(a) < 0:
        raise ValueError("House Area: Value must be non-negative")

    q = st.text_input("Overall House Quality (1 - 10)", "5")
    if int(q) > 10:
        raise ValueError("House Area: Given input beyond limit")
    elif int(q) < 0:
        raise ValueError("House Area: Value must be non-negative")

    g_cars = st.text_input("No. of Cars in Garage", "0")
    if int(g_cars) > 10:
        raise ValueError("No. of Cars in Garage: Given input beyond limit")
    elif int(g_cars) < 0:
        raise ValueError("No. of Cars in Garage: Value must be non-negative")

    rooms = st.text_input("Total no. of Rooms", "6")
    if int(rooms) > 25:
        raise ValueError("Total no. of Rooms: Given input beyond limit")
    elif int(rooms) < 0:
        raise ValueError("Total no. of Rooms: Value must be non-negative")

    m_area = st.text_input("Masonry Area (square feet)", "100")
    if float(m_area) > 2000:
        raise ValueError("Masonry Area: Given input beyond limit")
    elif float(m_area) < 0:
        raise ValueError("Masonry Area: Value must be non-negative")

    fireplaces = st.text_input("No. of Fireplaces in House", "0")
    if int(fireplaces) > 10:
        raise ValueError("No. of Fireplaces in House: Given input beyond limit")
    elif int(fireplaces) < 0:
        raise ValueError("No. of Fireplaces in House: Value must be non-negative")

    lot_area = st.text_input("Lot Area (square feet)", "70")
    if float(lot_area) > 350:
        raise ValueError("Lot Area: Given input beyond limit")
    elif float(lot_area) < 0:
        raise ValueError("Lot Area: Value must be non-negative")

    exter_qual = st.selectbox("House exterior material quality", ["Excellent", "Good", "Average", "Poor"])
    if exter_qual == "Excellent":
        exter_qual = "Ex"
    elif exter_qual == "Good":
        exter_qual = "Gd"
    elif exter_qual == "Average":
        exter_qual = "TA"
    else:
        exter_qual = "Fa"
    
    h_qual = st.selectbox("Heating Quality", ["Excellent", "Good", "Average", "Poor"])
    if h_qual == "Excellent":
        h_qual = "Ex"
    elif h_qual == "Good":
        h_qual = "Gd"
    elif h_qual == "Average":
        h_qual = "TA"
    else:
        h_qual = "Fa"

    base_qual = st.selectbox("Basement Quality", ["Excellent", "Good", "Average", "Poor", "No Basement"])
    if base_qual == "Excellent":
        base_qual = "Ex"
    elif base_qual == "Good":
        base_qual = "Gd"
    elif base_qual == "Average":
        base_qual = "TA"
    elif base_qual == "Poor":
        base_qual = "Fa"
    else:
        base_qual = "NA"

    k_qual = st.selectbox("Kitchen Quality", ["Excellent", "Good", "Average", "Poor"])
    if k_qual == "Excellent":
        k_qual = "Ex"
    elif k_qual == "Good":
        k_qual = "Gd"
    elif k_qual == "Average":
        k_qual = "TA"
    else:
        k_qual = "Fa"

    garage = st.selectbox("Interior Finish of Garage", ["Excellent", "Good", "Poor", "No Garage"])
    if garage == "Excellent":
        garage = "Fin"
    elif garage == "Good":
        garage = "RFn"
    elif garage == "Poor":
        garage = "Unf"
    else:
        garage = "NA"

    m_type = st.selectbox("Masonry Type", ["Brick Common", "Brick Face", "Stone", "None"])
    if m_type == "Brick Common":
        m_type = "BrkCmn"
    elif m_type == "Brick Face":
        m_type = "BrkFace"
    elif m_type == "Stone":
        m_type = "Stone"
    else:
        m_type = "None"

    if st.button("PREDICT"):
        output = predict(a, q, g_cars, rooms, m_area, fireplaces,
                         lot_area, exter_qual, h_qual, base_qual, 
                         k_qual, garage, m_type)

        st.text("Data Processed")
        st.warning(f"Estimated Price: {output: ,} $")

    if st.button("LOOK ME UP"):
        st.info(
            "LinkedIn: https://www.linkedin.com/in/mohammed-misbahullah-sheriff-b684091a1")
        st.success("GitHub: https://github.com/MisbahullahSheriff")


if __name__ == "__main__":
    main()


        