import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()

# 'gemini-2.5-flash-lite' is the 2026 stable free-tier model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite", 
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

try:
    print("--- Connecting to Gemini 2.5 Flash-Lite ---")
    response = llm.invoke([HumanMessage(content="Hello! Verify you are Gemini 2.5 Flash-Lite.")])
    print(f"Response: {response.content}")
    print("--- SUCCESS ---")
except Exception as e:
    print(f" Connection failed: {e}")
    print("Check if you need to run: pip install -U langchain-google-genai")