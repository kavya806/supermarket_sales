import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Supermarket Sales Analysis",
    layout="wide"
)

st.title("Supermarket Sales Data Analysis")
st.write("Interactive analysis of Supermarket Sales dataset")

# Load dataset
df = pd.read_csv("supermarket_sales.csv")

# Sidebar
st.sidebar.title("Analysis")

option = st.sidebar.selectbox(
    "Choose an option",
    [
        "Dataset Overview",
        "Sales Summary",
        "Product Line",
        "Branch",
        "Gender",
        "Payment",
        "Quantity vs Total",
        "Time Analysis"
    ]
)

# Dataset Overview
if option == "Dataset Overview":

    st.header("Dataset Overview")

    st.write("First 5 rows of the dataset:")
    st.dataframe(df.head())

    st.write("Dataset Shape:")
    st.write(df.shape)

    st.write("Column Names:")
    st.write(df.columns.tolist())

    st.write("Missing Values:")
    st.write(df.isnull().sum())


# Sales Summary
elif option == "Sales Summary":

    st.header("Sales Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Sales", round(df["Total"].sum(), 2))

    with col2:
        st.metric("Total Quantity", df["Quantity"].sum())

    with col3:
        st.metric("Gross Income", round(df["gross income"].sum(), 2))

    st.subheader("Sales by Product Line")

    sales = df.groupby("Product line")["Total"].sum()

    st.bar_chart(sales)


# Product Line
elif option == "Product Line":

    st.header("Product Line Analysis")

    product_count = df["Product line"].value_counts()

    st.bar_chart(product_count)

    st.write("Number of sales for each product line:")
    st.dataframe(product_count)


# Branch
elif option == "Branch":

    st.header("Branch Analysis")

    branch_sales = df.groupby("Branch")["Total"].sum()

    st.bar_chart(branch_sales)

    st.write("Total sales by branch:")
    st.dataframe(branch_sales)


# Gender
elif option == "Gender":

    st.header("Gender Analysis")

    gender_count = df["Gender"].value_counts()

    st.bar_chart(gender_count)

    st.write("Customers by gender:")
    st.dataframe(gender_count)


# Payment
elif option == "Payment":

    st.header("Payment Method Analysis")

    payment_count = df["Payment"].value_counts()

    st.bar_chart(payment_count)

    st.write("Number of transactions by payment method:")
    st.dataframe(payment_count)


# Quantity vs Total
elif option == "Quantity vs Total":

    st.header("Total vs Quantity")

    fig, ax = plt.subplots()

    ax.scatter(df["Total"], df["Quantity"])

    ax.set_xlabel("Total")
    ax.set_ylabel("Quantity")
    ax.set_title("Scatter Plot of Total vs Quantity")

    st.pyplot(fig)


# Time Analysis
elif option == "Time Analysis":

    st.header("Time Feature Analysis")

    time_count = df["Time"].value_counts().sort_index()

    st.line_chart(time_count)

    st.write(
        "This graph shows the number of transactions at different times."
    )