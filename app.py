import streamlit as st
from groq import Groq

# Page config
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot using Groq + Streamlit")

# Sidebar for API Key
groq_api_key = st.sidebar.text_input("Enter Groq API Key", type="password")

if groq_api_key:
    client = Groq(api_key=groq_api_key)

    user_input = st.text_area("Ask something:")

    if st.button("Generate Response"):
        if user_input:
            with st.spinner("Thinking..."):
                response = client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=[
                        {"role": "user", "content": user_input}
                    ]
                )

                answer = response.choices[0].message.content
                st.success("Response:")
                st.write(answer)
        else:
            st.warning("Please enter a question.")
else:
    st.info("Enter your Groq API key in sidebar.")
