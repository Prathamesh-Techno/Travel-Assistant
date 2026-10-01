
import streamlit as st 
from google import genai
from dotenv import load_dotenv
import time
load_dotenv()
client = genai.Client()
st.set_page_config(
    page_title="Prathamesh's App",
    page_icon="🚀",
    layout="wide"
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

location = st.text_input("Enter your current location")
destination = st.text_input("Enter your destination")
days_nr = st.number_input("How many days of trip?", min_value = 1, value = None)
budget_type = st.selectbox("Select budget type", ["Luxury", "Moderate", "Budgeted"],index = None)
budget = st.slider("Select your exact budget",100,1000000,100,100)
travel_type = st.radio("Select trip type", ["Family","Couple","Friends","Solo"],index = None)
if travel_type == "Family" :
  member_nr = st.number_input("Enter number of family members", min_value = 2, value = None)
prompt = f"""I wants to go to {destination} & my current location is {location} and for {days_nr} days ,
I am on a budget of type {budget_type} and the budget is {budget} , Travel Type is : {travel_type}"""

if st.button("Plan Trip"):
    with st.spinner("Processing..."):
      interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt,
            system_instruction="""You are a Experienced Travel and Trip Planner.As per given conditions,

            plan a travel and trip.Keep your response in three phases :
            First, guide user step by step to reaching on his/her desired destiny with real
            locations and available travel services in that area and from many ways of traveling & reaching to destiny,
            suggest user the nearest,fastest,safest and minmum costly way (tell estimate cost at each step).

            Second, plan a detailed trip for the destination as per given number of day (
            In this one sujjest/plan a trip for locations to visit and so on at destination,
            give ideas what to do on destination for given number of day
            and tell estimated cost at every point you feel ex.for some food item).

            Third, Total summary with budget estimation encluding travel and trip.It should contain both 
            Total estimeted budget and estimeted budget for per person.
            
            Don't give title to or divide answer in these phases just remember your response should contain these 
            three things.Keep phases in a constant flow without knowing to user that answer is divided in three phases.

            Share answer in bullet format and keep subheadings font little 
            big and include numbers as much as posible (Eg.,5days ,Rs.2000,1km (don't use these 
            numbers and style it's just examples . Use perticular info related to given conditions)) 
            keep response more engaging by using little relavent emojies the user should not be board 
            by too many words so keep your answer short but with covering all points smartly.

            Constraints :
            Don't give response using bad and harsh words,avoide adulte wording.
            Use cassual and simple language."""
      )

    st.success("Here are some Fab suiggestions for you!")
    st.write(interaction.output_text)
    
    
