import google.generativeai as genai

def generate_plant_disease_info(disease_name):
    # Configure the API key for Google Generative AI
    genai.configure(api_key="<API-KEY>")
    model = genai.GenerativeModel('gemini-pro')

    # Create the prompt dynamically using the plant disease name provided
    prompt = f"""Provide detailed information about the plant disease '{disease_name}'. The response should cover the following:

    1. **Name of the Disease**: Clearly state the name of the disease.
    2. **Symptoms**: Describe the typical symptoms or signs of the disease.
    3. **Causes**: Explain the factors or conditions that lead to the disease (e.g., environmental factors, pathogens, pests).
    4. **Cure/Remedies**: Provide practical steps for curing or treating the disease, including chemical or organic treatments.
    5. **Supplements**: Suggest any beneficial supplements, fertilizers, or nutrients that can help support the plant's recovery or enhance its resilience.
    6. **Future Care**: Recommend ongoing care practices to prevent the disease from recurring, such as proper watering, soil health, pest control, or environmental adjustments.

    Example Input: 'What can I do for my tomato plant affected by blight disease?'
    """

    # Generate the content using the model
    generated_info = model.generate_content(prompt)
    
    # Return the generated text about the plant disease
    return generated_info.text
