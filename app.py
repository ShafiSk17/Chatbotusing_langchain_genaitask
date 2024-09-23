
from langchain_google_genai import GoogleGenerativeAI

# Replace with your Gemini API key
GEMINI_API_KEY = "your api key"

# Initialize the ChatGoogleGenerativeAI object
llm = GoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=GEMINI_API_KEY
)

# Define a function to handle user queries
def handle_query(query):
    try:
        response_data = llm.invoke(query)
        if isinstance(response_data, dict):
            response = response_data["content"]
        else:
            response = response_data
        return response
    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred. Please try again later."

# Implement basic conversation flow
def chatbot_flow():
    print("Chatbot: Hello! How can I assist you today? (Type 'exit' to end the conversation)")
    while True:
        user_query = input("User: ")
        if user_query.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = handle_query(user_query)
        print("Chatbot:", response)

# Run the chatbot
chatbot_flow()

