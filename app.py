import streamlit as st
import collections
import pandas as pd
# --- Custom CSS for Gemini-like theme ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")
# --- Page Configuration ---
st.set_page_config(
    page_title="CareerMate",
    page_icon="🤖",
    layout="wide"
)

# --- Custom CSS for Gemini-like theme ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# --- Chatbot Responses and Knowledge Base ---
responses = {
    # Greetings and General
    ("hi", "hello", "hey", "hii"): "Hi! I'm your personal career guide, CareerMate. How can I help you?",
    ("career guidance", "career help", "career advice", "help me", "career path"): "I can help with career guidance. What stream are you in (Science, Commerce, Arts)?",
    ("thanks", "thank you", "thank u", "thankyou"): "You're welcome! Feel free to ask more questions.",
    
    # Streams and Courses
    ("science", "pcb", "pcm", "medical", "engineering"): "After 12th Science, popular courses include Engineering, MBBS, BSc, Pharmacy, and Computer Science. You can specialize in fields like AI, Data Science, or Biomedical Engineering.",
    ("commerce", "bcom", "accounts", "bba"): "After 12th Commerce, you can pursue B.Com, CA, BBA, Economics, or Hotel Management. Emerging fields include Digital Marketing and Financial Planning.",
    ("arts", "humanities", "arts student", "humanities student"): "After 12th Arts, popular options are BA, Journalism, Law, Fashion Designing, Psychology, and B.Ed. New-age careers include UX/UI Design and Content Creation.",
    
    # Exams and Admissions
    ("exam", "exams", "entrance", "neet", "jee", "clat"): "Key entrance exams are JEE for Engineering, NEET for Medical, CLAT for Law, and CUET for Central Universities. Some private colleges also have their own exams.",
    
    # Salary and Jobs
    ("job", "jobs", "career", "employment", "future"): "Job opportunities vary by stream. Engineering graduates can work in IT, software development, or core industries. Commerce grads can find roles in banking, finance, or corporate management. Arts students can excel in journalism, civil services, and design roles.",
    ("salary", "fresher salary", "starting salary"): "For a fresher, the average starting salary in India is between ₹3-6 lakhs per annum, but this can vary greatly based on your skills, college, and industry.",
    ("interview", "interview tips", "how to prepare for an interview"): "To prepare for an interview, research the company, be confident, and be ready to discuss your skills and projects. Practicing common questions and mock interviews can also help.",
    
    # Financial Guidance
    ("fees", "fee", "cost", "how much"): "Education costs vary. For Engineering: ₹1-5 lakhs/year. For Medicine: ₹5-15 lakhs/year. For Commerce/Arts: ₹30,000-1 lakh/year. These are approximate and depend on the college type (government/private).",
    ("scholarship", "scholarships", "financial aid", "funding"): "Scholarships are available from various sources, including the National Scholarship Portal, private organizations, and specific college funds. Researching early can help you secure financial aid.",
    
    # Other
    ("abroad", "foreign", "overseas", "study abroad"): "For studying abroad, you can consider countries like the US, UK, Canada, and Germany. Common exams required are SAT, IELTS, or TOEFL.",
    ("choose", "pick", "select", "which one"): "The best way to choose a career is by evaluating your interests, skills, and long-term goals. Don't follow trends; find what you are passionate about."
}

# --- Chat Memory and Logging ---
if "chat" not in st.session_state:
    st.session_state.chat = []
if "query_log" not in st.session_state:
    st.session_state.query_log = []

# --- Layout ---
st.title("🤖 CareerMate")

# Create a container for the chat interface with a modern look
chat_container = st.container()

with chat_container:
    st.subheader("Your Personal Career Guide")
    
    # Display chat history
    for role, msg in st.session_state.chat:
        if role == "You":
            st.markdown(f'<div class="chat-bubble user-bubble">{msg}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bubble bot-bubble">{msg}</div>', unsafe_allow_html=True)

    # Create a form to handle user input
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_input("Talk to CareerMate:", key="user_input_field")
        submit_button = st.form_submit_button(label='Send')

    # Process the user input when the button is clicked
    if submit_button and user_input:
        st.session_state.chat.append(("You", user_input))
        st.session_state.query_log.append(user_input.lower())
        
        reply = "I'm still learning, could you rephrase? Please ask a question about careers, courses, or streams. For example, 'What are the options in Science?'"
        user_input_lower = user_input.lower()
        
        # Check for matching keywords
        for keywords, response in responses.items():
            if any(keyword in user_input_lower for keyword in keywords):
                reply = response
                break
        
        st.session_state.chat.append(("Bot", reply))
        # Rerun the app to update the chat history
        st.rerun()

# --- Placeholder for Chatbot Insights (Dashboard Element) ---
st.markdown("---")
st.subheader("📊 CareerMate Insights")

# A simple chart based on user queries
if st.session_state.query_log:
    query_counts = collections.Counter(st.session_state.query_log)
    query_df = pd.DataFrame(query_counts.items(), columns=["Query", "Count"])
    
    st.markdown("##### **Top Queries This Session**")
    st.bar_chart(query_df.set_index("Query"))
else:
    st.info("Start a conversation to see insights!")