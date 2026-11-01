
import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()

# Initialize Search Tool
search_tool = None

if os.getenv("TAVILY_API_KEY"):
    search_tool = TavilySearch(max_results=5)

# Web Search Function
def search_web(query):

    if search_tool is None:
        return "Tavily API key is missing. Web search is unavailable."

    try:

        print("Searching the web:", query)
        result = search_tool.invoke({"query": query})
        return str(result)

    except Exception as error:
        print("Search Error:", str(error))
        return f"Web search failed: {str(error)}"

print("NexusAI: Search Tool Loaded Successfully!")
