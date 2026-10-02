
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

# All Inputs
location = st.text_input("Enter your current location")
destination = st.text_input("Enter your destination")
days_nr = st.number_input("How many days of trip?", min_value = 1, value = None)
budget_type = st.selectbox("Select budget type", ["Luxury", "Moderate", "Budgeted"],index = None)
budget = st.number_input("Enter your exact budget", min_value = 50, value = None)
travel_type = st.radio("Select trip type", ["Family","Couple","Friends","Solo"],index = None)
if travel_type == "Family" :
  travelers = st.number_input("Enter number of family members", min_value = 2, value = None)
elif travel_type == "Couple" :
  travelers = 2
elif travel_type == "Friends" :
  travelers = st.number_input("Enter number of friends going on trip", min_value = 2 , value = None)
else :
  travelers = 1
travel_services = st.multiselect("Select your travel preferences", ["Car","Bike","Cab","Auto","Bus","Train",
    "Metro","Online Travel Platform's Services","Bicycle","Walking","Flight","Boat","Private Jet","Private Helicopter","Private Boat"])
purpose = st.selectbox("Select your purpose of travel", ["Trip","Enjoy","Fun","Party","Trekking","Exploring",
    "Shoping","Photoshoot","Chilling","Work Related","Study Related","Just Visiting Place","Just Travelling From One Place To Another","Other"], index = None)
if purpose == "Other" :
  purpose = st.text_input("Enter your purpose of travel")

prompt = f"""I wants to go to {destination} & my current location is {location} and for {days_nr} days ,
I am on a budget of type {budget_type} and the budget is {budget} , Travelling with {travel_type}, Number of travelers is : {travelers},
I would prefer travelling by {travel_services} these services, my purpose of this travel is {purpose}"""

if st.button("Plan Trip"):
    with st.spinner("Processing..."):
      interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt,
            system_instruction="""You are a Experienced Travel and Trip Planner.As per the given requirements (take them as it is don't assume them),
            plan a travel and trip.Keep your response in Four phases :

            First, guide user step by step for reaching to his/her desired destiny as per prefered travelling services by him/her with real
            locations and available travel services in that area and from many ways of traveling & reaching to destiny,
            suggest user the nearest,fastest,safest and minmum costly way (tell estimate cost at each step).

            Second, plan a detailed trip for the destination as per given number of day and required purpose
            (In this one sujjest/plan a trip for locations to visit and so on at destination,
            give ideas what to do on destination for given number of day
            and tell estimated cost at every point you feel ex.for some food item).

            Third, guide user step by step to returning to his/her location from destiny as per prefered travelling services by him/her with real
            locations and available travel services in that area and from many ways of traveling & reaching to destiny,
            suggest user the nearest,fastest,safest and minmum costly way (tell estimate cost at each step).

            Fourth, Give Total summary of everything(Eg.,shoping,food,stay,rides,etc) with budget estimation encluding travel and trip.
            It should contain both Total estimeted budget and estimeted budget for per person (Only if travelers are more than 1),
            in also bullet format and add some little workds by you and make it feel person more happy and engaging (keep it short and covering all)

            Don't give title to or divide answer in these phases just remember your response should contain these
            four things.Keep phases in a constant flow without knowing to user that answer is divided in four phases.

            Share answer in bullet format and keep subheadings font size little
            big and include numbers as much as posible (Eg.,5days ,Rs.2000,1km (don't use these
            numbers and style it's just examples . Use perticular info related to given requirements))
            keep response more engaging by using little relavent emojies the user should not be bored
            by too many words so keep your answer short but with covering all points smartly.

            Constraints :
            Don't give response using bad and harsh words,avoide adulte wording.
            Use cassual and simple language.
            Don't use technical words(language) related to coding and all.
            If you have to use requirements in response then don't use it in "",instead keep the words bold.
            Don't use travelers word directly in response, instead use the relevant word for travelers as per given requirements.

            Take care of these conditions/things :
            If location and destination is same don't generate answer, politly respod in littel more and correct words in your way with use of emojies also (don't make user's fool/laugh).
            If any required information is missing (contain None) in requirements don't generate answer, politly respond in little more and correct words in your way with use of emojies also (don't make user's fool/laugh).
            If you fill some satrange in given requirements then don't generate answer, politly tell what strange thing you feel and correct it
            politly in little more and correct words in your way with use of emojies also (don't make user's fool/laugh).
            If budget type is budgeted then focus on saving money and fitting the trip in given budget while planing the trip and
            for that suggest the affordable/minimum costly and nearest travelling way instead of fastest, suggest the minimum costly stay and all.
            if budget is fine then don't compromise things and traveling time.
            If budget type is moderate then focus on spending less money and fitting the trip in given budget while planing the trip and
            for that suggest the affordable/minimum costly and nearest travelling way as per budget instead of fastest, suggest the minimum costly stay and all as per budget;
            if budget is fine then don't compromise things and traveling time.

            Try to fit Total estimated cost with in budget(given in requirements) even if after all in any situation/way budget is insufficient then don't generate answer, politly respond like could you please uplift your budget a little more,
            it's insufficient for ever posible way, you need minimum {minimum budget can sufficient for such trip} budget for this trip,
            In little more and correct words in your way with use of emojies also (don't use the given same line, respond it in your way).
            """
      )

    st.success("Here is your required plan!")
    st.write(interaction.output_text)

