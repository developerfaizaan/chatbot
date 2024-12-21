import streamlit as st
import google.generativeai as genai

# Configure the API key for Google Generative AI (Replace with your API key)
genai.configure(api_key="AIzaSyB8RylTDVAykRTpzEwZ44Vxp8XAsh0QYXY")  # Replace <API-KEY> with your actual API key
model = genai.GenerativeModel('gemini-pro')

def generate_plant_disease_info(disease_name):
    # Constructing the prompt based on the disease name
    prompt = f"""Provide detailed information about the plant disease '{disease_name}'. The response should cover the following:

    1. **Name of the Disease**: Clearly state the name of the disease.
    2. **Symptoms**: Describe the typical symptoms or signs of the disease.
    3. **Causes**: Explain the factors or conditions that lead to the disease (e.g., environmental factors, pathogens, pests).
    4. **Cure/Remedies**: Provide practical steps for curing or treating the disease, including chemical or organic treatments.
    5. **Supplements**: Suggest any beneficial supplements, fertilizers, or nutrients that can help support the plant's recovery or enhance its resilience.
    6. **Future Care**: Recommend ongoing care practices to prevent the disease from recurring, such as proper watering, soil health, pest control, or environmental adjustments.
    """

    # Generate the content using the model
    generated_info = model.generate_content(prompt)
    
    return generated_info.text

# Streamlit UI
def plant_disease_chatbot():
    # Set page title and background
    st.set_page_config(page_title="Plant Disease Chatbot", page_icon="🌱", layout="wide")
    
    # Header with title and description
    st.title("Plant Disease Chatbot 🌿🦠")
    st.markdown("Ask me about any plant disease, and I'll provide details on symptoms, causes, remedies, supplements, and future care for your plants!")

    # Chat history container
    chat_history = []

    # User input field
    user_input = st.text_input("Ask me about a plant disease:", "")

    if user_input:
        # Display user's question in chat-like format
        chat_history.append(f"**You:** {user_input}")
        
        # Process the input and generate response
        try:
            # Generate plant disease information
            response = generate_plant_disease_info(user_input)

            # Display chatbot's response
            chat_history.append(f"**Bot:** {response}")

            # Display the full conversation history
            for chat in chat_history:
                st.markdown(f"{chat}\n")
        except Exception as e:
            st.error(f"Error: {e}")
    
    # Button for resetting chat history (optional)
    if st.button("Reset Conversation"):
        chat_history.clear()

# Run the chatbot UI
if __name__ == "__main__":
    plant_disease_chatbot()
