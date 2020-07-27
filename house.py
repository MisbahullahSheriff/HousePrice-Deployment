import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open("voting_model.pkl", "rb"))

def predict(area, quality, g_cars, rooms, m_area, 
            fireplaces, lot_area, exter_qual, h_qual, base_qual,
            k_qual, garage,  m_type):
    
    a = int(area)
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

    a = st.text_input("House Area (square feet) (eg: 3000)", "Type Here")
    q = st.text_input("Overall Quality (eg: 1 - 10)", "Type Here")
    g_cars = st.text_input("Garage Size rating (eg: 1 - 5)", "Type Here")
    rooms = st.text_input("Total no. of Rooms", "Type Here")
    m_area = st.text_input("Masonry Area (square feet) (eg: 100)", "Type Here")
    fireplaces = st.text_input("No. of Fireplaces (eg: 0 - 3)", "Type Here")
    lot_area = st.text_input("Lot Area (square feet) (eg: 70)", "Type Here")

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

        st.success(f"Estimated Price: {output: ,} $")


if __name__ == "__main__":
    main()


        