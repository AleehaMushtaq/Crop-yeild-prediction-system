
import streamlit as st
import pandas as pd
import joblib
import json

# Page settings
st.set_page_config(
    page_title="CropYield | Smart Agriculture",
    page_icon="🌿",
    layout="wide"
)

# Load trained model and metadata
@st.cache_resource
def load_model():
    return joblib.load("crop_yield_model.joblib")

@st.cache_data
def load_metadata():
    with open("model_metadata.json", "r", encoding="utf-8") as file:
        return json.load(file)

model = load_model()
metadata = load_metadata()

# Professional green theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

    .stApp {
        background: #f5f8f3;
        color: #1b3025;
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"] {
        background: rgba(245,248,243,0.9);
    }

    [data-testid="stSidebar"] {
        background: #163b2b;
    }

    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    .hero {
        background: linear-gradient(120deg, #123b2b, #226344);
        padding: 38px 40px;
        border-radius: 22px;
        color: white;
        margin-bottom: 26px;
        box-shadow: 0 10px 30px rgba(22,59,43,0.12);
    }

    .hero-tag {
        color: #c7efcf;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .hero h1 {
        color: white;
        font-family: 'Manrope', sans-serif;
        font-size: clamp(30px, 4vw, 44px);
        line-height: 1.2;
        margin: 12px 0;
    }

    .hero p {
        color: #e0eee3;
        font-size: 16px;
        max-width: 650px;
        line-height: 1.7;
        margin-bottom: 0;
    }

    .section-title {
        font-family: 'Manrope', sans-serif;
        font-size: 23px;
        font-weight: 800;
        color: #183d2c;
        margin: 14px 0 4px 0;
    }

    .section-subtitle {
        color: #64756a;
        font-size: 14px;
        margin-bottom: 20px;
    }

    .info-card {
        background: white;
        border: 1px solid #e2e9df;
        border-radius: 16px;
        padding: 20px;
        min-height: 112px;
        box-shadow: 0 4px 16px rgba(28,58,38,0.035);
    }

    .info-label {
        color: #708074;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 9px;
    }

    .info-value {
        color: #1c5035;
        font-family: 'Manrope', sans-serif;
        font-size: 23px;
        font-weight: 800;
    }

    .panel {
        background: #ffffff;
        border: 1px solid #e1e9df;
        border-radius: 18px;
        padding: 24px;
        margin: 10px 0 18px 0;
    }

    .result-panel {
        background: linear-gradient(135deg, #e5f4e5, #f8fcf5);
        border: 1px solid #cce4cd;
        border-radius: 18px;
        padding: 28px;
        margin-top: 20px;
    }

    .result-label {
        color: #416b4c;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .result-number {
        color: #16472d;
        font-family: 'Manrope', sans-serif;
        font-size: clamp(32px, 4vw, 46px);
        font-weight: 800;
        margin: 8px 0;
    }

    div.stButton > button {
        background: #20633f;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 20px;
        font-weight: 700;
        min-height: 48px;
        transition: 0.2s;
    }

    div.stButton > button:hover {
        background: #16472d;
        color: white;
        border: none;
        box-shadow: 0 5px 15px rgba(22,71,45,0.16);
    }

    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {
        border-radius: 9px;
        border-color: #d8e3d6;
    }

    .footer {
        border-top: 1px solid #dce6da;
        color: #738176;
        font-size: 12px;
        padding-top: 18px;
        margin-top: 35px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 🌿 CropYield")
    st.caption("SMART AGRICULTURE PLATFORM")
    st.markdown("---")
    st.markdown("### About this tool")
    st.write(
        "Estimate crop yield using growing conditions "
        "and a trained machine-learning model."
    )
    st.markdown("---")
    st.markdown("**Prediction unit**")
    st.write("hg/ha and tonnes/ha")
    st.markdown("**Validation method**")
    st.write("10-fold cross-validation")
    st.markdown("---")
    st.caption("AIC354 · Machine Learning Fundamentals")

# Main hero banner
st.markdown("""
<div class="hero">
    <div class="hero-tag">🌱 Data-driven farming</div>
    <h1>Crop Yield<br>Prediction System</h1>
    <p>
        Turn crop and weather information into a yield estimate.
        Explore how rainfall, temperature, and agricultural inputs
        can support smarter planning.
    </p>
</div>
""", unsafe_allow_html=True)

# Overview cards
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="info-card">
        <div class="info-label">Dataset records</div>
        <div class="info-value">{metadata['rows_used']:,}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="info-card">
        <div class="info-label">Crop varieties</div>
        <div class="info-value">{len(metadata['crops']):,}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="info-card">
        <div class="info-label">Areas covered</div>
        <div class="info-value">{len(metadata['areas']):,}</div>
    </div>
    """, unsafe_allow_html=True)

# Input section
st.markdown('<div class="section-title">01 / Growing conditions</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Enter the details for your crop and growing area.</div>',
    unsafe_allow_html=True
)

with st.container(border=True):
    left, right = st.columns(2, gap="large")

    with left:
        st.markdown("#### 🌾 Crop details")

        area = st.selectbox(
            "Country / Area",
            options=metadata["areas"]
        )

        crop = st.selectbox(
            "Crop type",
            options=metadata["crops"]
        )

        year = st.number_input(
            "Growing year",
            min_value=int(metadata["year_min"]),
            max_value=int(metadata["year_max"]),
            value=int(metadata["year_max"]),
            step=1
        )

    with right:
        st.markdown("#### 🌦️ Environmental inputs")

        rainfall = st.number_input(
            "Average annual rainfall (mm)",
            min_value=0.0,
            value=1000.0,
            step=50.0,
            help="Average rainfall in millimetres per year."
        )

        pesticides = st.number_input(
            "Pesticides used (tonnes)",
            min_value=0.0,
            value=100.0,
            step=10.0,
            help="Enter the amount in tonnes, not kilograms."
        )

        temperature = st.number_input(
            "Average temperature (°C)",
            value=20.0,
            step=0.5
        )

    st.markdown("")
    predict_button = st.button(
        "🌱  Calculate Estimated Yield",
        use_container_width=True
    )

# Prediction result
if predict_button:
    input_data = pd.DataFrame([{
        "Area": area,
        "Item": crop,
        "Year": int(year),
        "average_rain_fall_mm_per_year": rainfall,
        "pesticides_tonnes": pesticides,
        "avg_temp": temperature
    }])

    try:
        with st.spinner("Analysing growing conditions..."):
            prediction = float(model.predict(input_data)[0])

        if not pd.notna(prediction):
            raise ValueError("The model returned an invalid prediction.")

        tonnes_per_hectare = prediction / 10000

        st.markdown(
            '<div class="section-title">02 / Prediction report</div>',
            unsafe_allow_html=True
        )

        st.markdown(f"""
        <div class="result-panel">
            <div class="result-label">Estimated crop yield</div>
            <div class="result-number">{prediction:,.2f} hg/ha</div>
            <div style="color:#416b4c;font-size:16px;">
                Equivalent to approximately
                <b>{tonnes_per_hectare:,.4f} tonnes per hectare</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("")
        r1, r2, r3 = st.columns(3)

        with r1:
            st.metric("Selected crop", crop)

        with r2:
            st.metric("Growing area", area)

        with r3:
            st.metric("Growing year", int(year))

        report = pd.DataFrame([{
            "Area": area,
            "Crop": crop,
            "Year": int(year),
            "Rainfall_mm": rainfall,
            "Pesticides_tonnes": pesticides,
            "Temperature_C": temperature,
            "Predicted_yield_hg_per_ha": prediction,
            "Predicted_yield_tonnes_per_ha": tonnes_per_hectare
        }])

        st.download_button(
            "⬇️ Download prediction report (CSV)",
            data=report.to_csv(index=False).encode("utf-8"),
            file_name="crop_yield_prediction.csv",
            mime="text/csv"
        )

        st.info(
            "This result is an estimate from historical data. "
            "Actual yield may vary with soil quality, crop variety, "
            "irrigation, pests, and other conditions."
        )

    except Exception as error:
        st.error(f"Could not generate the prediction: {error}")

# Model information
with st.expander("View machine-learning model information"):
    st.write("**Best algorithm:**", metadata["best_algorithm"])
    st.write("**Target variable:**", metadata["target_column"])
    st.write("**Evaluation:** 10-fold cross-validation")
    st.write("**Training records:**", f"{metadata['rows_used']:,}")
    st.write("**Mean cross-validation RMSE:**",
             f"{metadata['mean_rmse']:,.2f} hg/ha")
    st.write("**RMSE standard deviation:**",
             f"{metadata['std_rmse']:,.2f} hg/ha")

st.markdown("""
<div class="footer">
    CropYield Prediction System · AIC354 Machine Learning Fundamentals<br>
    Educational project · Predictions are estimates, not guaranteed harvest outcomes.
</div>
""", unsafe_allow_html=True)
