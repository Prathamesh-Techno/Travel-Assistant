import streamlit as st 
from google import genai
from dotenv import load_dotenv
import time
load_dotenv()
client = genai.Client()
st.set_page_config(
    page_title="Prathamesh's App",  # Changes the browser tab name
    page_icon="🚀",                 # Can be an emoji or a path to an image file
    layout="wide"                 # Optional: "centered" or "wide"
)

st.markdown(
    """
    <style>
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-8px) rotate(3deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
    @keyframes pulseGlow {
        0% { opacity: 0.6; }
        50% { opacity: 1; filter: drop-shadow(0 0 10px rgba(255,255,255,0.6)); }
        100% { opacity: 0.6; }
    }
    .travel-hero {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        padding: 2.5rem 2rem;
        border-radius: 18px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .travel-icon {
        display: inline-block;
        animation: float 4s ease-in-out infinite;
        font-size: 3.5rem;
        margin-bottom: 5px;
    }
    .travel-title {
        font-size: 3rem; 
        margin: 0; 
        font-weight: 800; 
        letter-spacing: 1px;
        font-family: 'Inter', sans-serif;
        background: linear-gradient(to right, #ffffff, #a8ff78);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .travel-badge {
        margin-top: 15px;
        display: inline-block;
        background: rgba(255, 255, 255, 0.12);
        padding: 6px 18px;
        border-radius: 20px;
        font-size: 0.9rem;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        animation: pulseGlow 3s infinite;
    }
    </style>

    <div class="travel-hero">
        <div class="travel-icon">✈️🌍</div>
        <h1 class="travel-title">AI Travel Assistant</h1>
        <p style="font-size: 1.2rem; margin-top: 12px; color: #d0d7de; font-weight: 300;">
            Your intelligent companion for seamless journeys, itineraries, and local secrets.
        </p>
        <div class="travel-badge">
            🚀 Ready for takeoff • Let's explore the world
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("Your personal travel planner")

location = st.text_input("Where do you want to go?")
days_nr = st.number_input("How many days of trip?", min_value=1,value = None)

budget = st.selectbox("Select budget type", ["Luxury", "Moderate", "Budgeted"],index = None)
travel_type = st.radio("Select trip type", ["Family","Solo", "Friends"],index = None)

prompt = f"""You are a Travel Planner, User is saying he/she wants to 
go to {location} and for {days_nr} days , he is on a budget of type {budget}
Travel Type is :  {travel_type}
Plan a trip and share answer in bullet format"""

if st.button("Plan Trip"):
    with st.spinner("Processing..."):
      interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt
        )

    st.success("Here are some Fab suiggestions for you!")
    st.write(interaction.output_text)
    
    
