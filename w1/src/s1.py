# Main functions here for streamlit
from rich.traceback import install
import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

install(show_locals=True)


def he1():
    "Test code here"
    st.write("Hello from s1 \n and panty")
    st.write(
        {
            "key": "value",
            "key2": "value2",
            "key3": "value3",
            "key4": "value4",
            "key5": "value5",
        }
    )


def wo1():
    img = "https://porngipfy.com/wp-content/uploads/2018/11/facesitting_001.gif"
    st.image(img)
    "Main  Tutorial Function here"
    st.divider()
    st.title("Data Panty")
    st.divider()

    # Sidebar notaion
    # Using object notation
    add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
    )

    # Using "with" notation
    with st.sidebar:
        add_radio = st.radio(
            "Choose a shipping method", ("Standard (5-15 days)", "Express (2-5 days)")
        )
        st.info("This is a purely informational message", icon="ℹ️")

    upl_fl = st.file_uploader("FuckFuck Loader", type="csv")

    st.subheader("Data Panties")

    st.divider()

    if upl_fl is not None:
        df = pd.read_csv(upl_fl)
        st.write(df.head())
        st.dataframe(df, width=1000)

        st.divider()

        st.subheader("Data Summary")
        st.dataframe(df.describe())

        # Data filtration
        st.divider()
        st.subheader("Data Filter")
        col1 = df.columns.to_list()
        selcol1 = st.selectbox("Select Columns", col1)
        unique1 = df[selcol1].unique().tolist()
        sel_val1 = st.selectbox("Select Value", unique1)

        fil_df = df[df[selcol1] == sel_val1]
        st.write(fil_df)

        # Data Plotting
        st.divider()
        st.subheader("Data Plotting")
        x_column = st.selectbox("Select X Column", col1)
        y_column = st.selectbox("Select Y Column", col1)

        if st.button("Genplot"):
            st.line_chart(fil_df.set_index(x_column)[y_column])

    else:
        st.header("bastard no file")
        img2 = "https://gifdb.com/images/high/gladiator-thumbs-down-angry-joaquin-phoenix-wgc9hlaatcgkwbst.webp"
        st.image(img2)
