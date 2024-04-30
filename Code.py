import streamlit as st
import openai
import os
from dotenv import load_dotenv
load_dotenv()
# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Password for accessing the chatbot
PASSWORD = "1234@1234"

def analyze_syntax(code, language):
    # This function analyzes the syntax of the code
    # Add syntax analysis logic for different languages
    if language.lower() == "python":
        # Placeholder syntax analysis for Python
        # Check if the code contains at least one print statement
        if "print(" in code:
            return True
        else:
            return False
    elif language.lower() == "java":
        # Placeholder syntax analysis for Java
        # Check if the code contains at least one System.out.println statement
        if "System.out.println(" in code:
            return True
        else:
            return False
    elif language.lower() == "c":
        # Placeholder syntax analysis for C
        # Check if the code contains at least one printf statement
        if "printf(" in code:
            return True
        else:
            return False

def explain_code(code, language):
    # Generate explanation using OpenAI API
    prompt = f"Explain the following {language} code:\n\n{code}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # GPT-3.5 turbo model
        messages=[
            {"role": "system", "content": prompt}
        ],
        max_tokens=100,
        stop=None,
    )
    explanation = response.choices[0].message["content"].strip()
    return explanation

def main():
    st.title("Code Language Chatbot")

    # Password input
    password = st.text_input("Enter password:", type="password")

    if password == PASSWORD:
        st.success("Password correct. You can use the chatbot now.")

        # Initialize session state
        if 'previous_interactions' not in st.session_state:
            st.session_state.previous_interactions = []

        # Language selection dropdown
        language = st.selectbox("Select code language:", ["Python", "Java", "C"])

        user_input = st.text_area(f"Enter {language} code:", key="input_field")

        if st.button("Explain"):
            if user_input.strip():
                if analyze_syntax(user_input, language):
                    explanation = explain_code(user_input, language)
                    st.session_state.previous_interactions.append((user_input, explanation))
                else:
                    st.error("Invalid syntax for the selected language.")

        if st.session_state.previous_interactions:
            for user_code, explanation in st.session_state.previous_interactions:
                st.write(f"{language.capitalize()} code:")
                st.code(user_code)
                st.write("Explanation:")
                st.write(explanation)
                st.write("****************************************************************")
    elif password != "":
        st.error("Incorrect password. Please try again.")

if __name__ == "__main__":
    main()
