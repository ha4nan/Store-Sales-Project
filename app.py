# ==========================================================
# Store Sales Prediction System
# Machine Learning Project
# ==========================================================

import streamlit as st
import pandas as pd
import joblib
import time

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Store Sales Prediction",
    page_icon="🏪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------------------------------------
# Custom CSS
# ----------------------------------------------------------

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

h1{
    text-align:center;
    color:#4F8BF9;
}

.stButton>button{
    width:100%;
    height:50px;
    border-radius:10px;
    font-size:18px;
    background:#4F8BF9;
    color:white;
    border:none;
}

.stButton>button:hover{
    background:#6EA8FE;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# Load Trained Model
# ----------------------------------------------------------

model = joblib.load("best_model.pkl")
features = joblib.load("feature_columns.pkl")
# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------

with st.sidebar:

    st.title("🏪 Store Sales Predictor")

    st.markdown("---")

    st.subheader("🤖 Model")
    st.success("Random Forest Regressor")

    st.subheader("📂 Input")
    st.info("CSV File")

    st.markdown("---")

    st.subheader("Development Team")

    st.markdown("""
**Hager**  
Mohamed Ashraf  
Hanan  
Abdelrahman  
Mohamed Amr
""")

    st.markdown("---")
    st.caption("Machine Learning Project | 2026")
    

# ----------------------------------------------------------
# Application Title
# ----------------------------------------------------------

st.markdown("""
<div style="
background:#1B1F2A;
padding:25px;
border-radius:15px;
border:1px solid #31333F;
text-align:center;
margin-bottom:20px;
">
<h1 style="color:#4F8BF9;">🏪 Store Sales Prediction System</h1>
<p style="font-size:17px;color:#B0B3B8;">
Upload a CSV file to predict future store sales using our trained Machine Learning model.
</p>
</div>
""", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)
# ----------------------------------------------------------
# File Upload Section
# ----------------------------------------------------------

st.subheader("📂 Upload Test File")

uploaded_file = st.file_uploader(
    "Choose test.csv",
    type=["csv"]
)

# ----------------------------------------------------------
# Process Uploaded File
# ----------------------------------------------------------

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    st.success("✅ File uploaded successfully!")
    st.toast("File uploaded successfully 📂")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", data.shape[0])

    with col2:
        st.metric("Columns", data.shape[1])


    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📋 Data Preview")

    st.dataframe(
        data.head(),
        use_container_width=True
    )

  
    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # Prediction Button
    # ------------------------------------------------------
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button(
        "🚀 Predict Sales",
        use_container_width=True
    ):

        with st.spinner("🤖 AI Model is predicting sales..."):

            progress = st.progress(0)

            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)

            progress.empty()

        # --------------------------------------------------
        # Load Supporting Files
        # --------------------------------------------------

        stores = pd.read_csv("stores.csv")

        oil = pd.read_csv("oil.csv")

        oil["date"] = pd.to_datetime(oil["date"])

        oil["dcoilwtico"] = (
            oil["dcoilwtico"]
            .ffill()
            .bfill()
        )

        # --------------------------------------------------
        # Merge Datasets
        # --------------------------------------------------

        data["date"] = pd.to_datetime(data["date"])

        data = data.merge(
            stores,
            on="store_nbr",
            how="left"
        )

        data = data.merge(
            oil,
            on="date",
            how="left"
        )

        data["dcoilwtico"] = (
            data["dcoilwtico"]
            .ffill()
            .bfill()
        ) 
        # --------------------------------------------------
        # Create Date Features
        # --------------------------------------------------

        data["year"] = data["date"].dt.year
        data["month"] = data["date"].dt.month
        data["day"] = data["date"].dt.day
        data["dayofweek"] = data["date"].dt.dayofweek
        data["weekend"] = data["dayofweek"].isin([5, 6]).astype(int)

        # --------------------------------------------------
        # Apply One-Hot Encoding
        # --------------------------------------------------

        data = pd.get_dummies(
            data,
            columns=["family", "city", "state", "type"],
            drop_first=True
        )

        # --------------------------------------------------
        # Save Test IDs
        # --------------------------------------------------

        test_ids = data["id"].copy()

        # --------------------------------------------------
        # Add Missing Feature Columns
        # --------------------------------------------------

        for col in features:
            if col not in data.columns:
                data[col] = 0

        # Keep only the columns used during training
        data = data[features]

        # --------------------------------------------------
        # Generate Predictions
        # --------------------------------------------------

        prediction = model.predict(data)

        result = pd.DataFrame({
            "id": test_ids,
            "sales": prediction
        })

        # --------------------------------------------------
        # Display Results
        # --------------------------------------------------

        st.success("✅ Prediction completed successfully!")

        st.balloons()
        st.toast("Prediction completed successfully 🎉")

        st.subheader("📊 Prediction Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Average Sales",
                f"{result['sales'].mean():.2f}"
            )

        with col2:
            st.metric(
                "Maximum Sales",
                f"{result['sales'].max():.2f}"
            )

        with col3:
            st.metric(
                "Minimum Sales",
                f"{result['sales'].min():.2f}"
            )

        st.markdown("<br>", unsafe_allow_html=True)

        st.subheader("📋 Prediction Results")

        st.dataframe(
            result.head(10),
            use_container_width=True
        )

        st.subheader("📈 Sales Prediction Trend")

        st.line_chart(
    result.set_index("id")["sales"].head(100)
           )

        csv = result.to_csv(index=False).encode("utf-8")
        st.info("Download the generated submission file and upload it to Kaggle.")
        st.download_button(
            label="📥 Download submission.csv",
            data=csv,
            file_name="submission.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.success("Submission file is ready for Kaggle! 🚀")   
        st.markdown("---")

st.caption(
    "Store Sales Prediction System | Machine Learning Project | 2026"
)
     