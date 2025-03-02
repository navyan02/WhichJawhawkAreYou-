import streamlit as st
import time

def get_jayhawk_type(answers):
    if answers.count("A") > max(answers.count("B"), answers.count("C"), answers.count("D")):
        return "The Classic Jayhawk (1941)", "https://github.com/navyan02/WhichJawhawkAreYou-/blob/main/ClassicJayhawk.png?raw=true"
    elif answers.count("B") > max(answers.count("A"), answers.count("C"), answers.count("D")):
        return "The Energetic Jayhawk (1929)", "https://github.com/navyan02/WhichJawhawkAreYou-/blob/main/The%20Energetic%20Jayhawk%20(1929).jpg?raw=true"
    elif answers.count("C") > max(answers.count("A"), answers.count("B"), answers.count("D")):
        return "The Scholarly Jayhawk (1912)", "https://github.com/navyan02/WhichJawhawkAreYou-/blob/main/TheScholarly.gif?raw=true"
    elif answers.count("D") > max(answers.count("A"), answers.count("B"), answers.count("C")):
        return "The Spirited Jayhawk (2005)", "https://github.com/navyan02/WhichJawhawkAreYou-/blob/main/The%20Spirited%20Jayhawk%20(2005).png?raw=true"
    elif answers.count("A") == answers.count("B") and answers.count("A") > max(answers.count("C"), answers.count("D")):
        return "The Loyal Jayhawk (1923)", "https://github.com/navyan02/WhichJawhawkAreYou-/blob/main/The%20Loyal%20Jayhawk%20(1923).png?raw=true"
    elif answers.count("B") == answers.count("C") and answers.count("B") > max(answers.count("A"), answers.count("D")):
        return "The Adventurous Jayhawk (1916)", "https://github.com/navyan02/WhichJawhawkAreYou-/blob/main/The%20Adventurous%20Jayhawk%20(1916).jpg?raw=true"
    elif answers.count("D") == answers.count("A") and answers.count("D") > max(answers.count("B"), answers.count("C")):
        return "The Scholarly Jayhawk (1912)", "https://github.com/navyan02/WhichJawhawkAreYou-/blob/main/TheScholarly.gif?raw=true"
    else:
        return "The Bold Jayhawk (2020)", "https://github.com/navyan02/WhichJawhawkAreYou-/blob/main/The%20Bold%20Jayhawk%20(2020).png?raw=true"

st.markdown("""
    <style>
        /* Set gradient background */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(to bottom, #1E3A8A, #2563EB);
        }
        /* Adjust the text styling */
        .big-title {
            font-size: 100px;
            color: #0A1A2B; /* Dark blue almost black */
            text-align: center;
            font-weight: bold;
            font-family: "Comic Sans MS";
        }
        .sub-title {
            font-size: 50px;
            color: #E8000D;
            text-align: center;
            font-family: "Comic Sans MS";
        }
        /* Style the button */
        .stButton>button {
            background-color: #0051BA;
            color: white;
            font-size: 20px;
            border-radius: 10px;
            padding: 10px;
            font-family: "Comic Sans MS";
        }
        .stButton>button:hover {
            background-color: #E8000D;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="font-size: 50px; color: #0A1A2B; text-align: center; font-weight: bold; font-family: Comic Sans MS;">Which Jayhawk Are You?</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="font-size: 25px; color: #E8000D; text-align: center; font-family: Comic Sans MS;">Answer these fun KU themed questions to find out!</h2>', unsafe_allow_html=True)

# Questions
questions = [
    ("What’s your ideal game day activity?", "A) Cheering in the student section", "B) Tailgating with friends", "C) Watching from home with analysis", "D) Organizing a watch party"),
    ("What’s your go to study spot?", "A) Watson Library", "B) The Union", "C) Engineering Library", "D) A cozy coffee shop"),
    ("What’s your ideal weekend activity?", "A) Going to a sports event", "B) Hanging out with friends downtown", "C) Reading or working on a project", "D) Exploring campus and nature trails"),
    ("Pick a favorite KU landmark", "A) Allen Fieldhouse", "B) Potter Lake", "C) Memorial Library", "D) Campanile")
]

answers = []

for question, option_a, option_b, option_c, option_d in questions:
    choice = st.radio(question, [option_a, option_b, option_c, option_d])
    if choice == option_a:
        answers.append("A")
    elif choice == option_b:
        answers.append("B")
    elif choice == option_c:
        answers.append("C")
    else:
        answers.append("D")

if st.button("Find My Jayhawk!"):
    with st.spinner("Finding your Jayhawk..."):
        time.sleep(2)
    result_text, image_url = get_jayhawk_type(answers)
    st.success(f"You're {result_text}!")
    st.image(image_url, caption=result_text, use_container_width=True)
    st.balloons()
