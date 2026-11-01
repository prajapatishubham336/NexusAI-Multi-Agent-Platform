
import os
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Groq LLM Configuration
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing in .env file")

llm = ChatGroq(
    model=os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
    temperature=0.3,
    max_retries=2
)


# Common AI Function
def ask_ai(prompt):
    response = llm.invoke(prompt)
    return response.content


# 1. Manager Agent
def manager_agent(task):

    prompt = f"""
You are NexusAI Manager Agent.

Analyze this task:
{task}

Choose exactly one category:
CODE - Programming and website development
RESEARCH - Research and information gathering
GENERAL - Other tasks

Reply with only one category:
CODE, RESEARCH, or GENERAL.
"""

    result = str(ask_ai(prompt)).upper()
    match = re.search(r"\b(CODE|RESEARCH|GENERAL)\b", result)
    if match:
        return match.group(1)
    return "GENERAL"


# 2. Research Agent
def research_agent(task, research_data):

    prompt = f"""
You are NexusAI Research Agent.

User Task:
{task}

Web Search Results:
{research_data}

Instructions:
1. Analyze the available information.
2. Give useful and relevant findings.
3. Explain important concepts.
4. Do not invent facts.
5. Mention if information is unavailable.
"""

    return ask_ai(prompt)


# 3. Coding Agent
def coding_agent(task):

    prompt = f"""
You are NexusAI Coding Agent.

User Task:
{task}

Generate a complete solution.

Requirements:
1. Beginner-friendly code.
2. Explain the folder structure.
3. Include required dependencies.
4. Use clean and organized code.
5. Include comments where useful.
6. Do not claim that code was executed.
"""

    return ask_ai(prompt)


# 4. Testing Agent
def testing_agent(task, code):

    prompt = f"""
You are NexusAI Testing Agent.

Original Task:
{task}

Generated Code:
{code}

Review the code carefully.

Check:
1. Syntax issues.
2. Logical errors.
3. Missing dependencies.
4. Possible bugs.
5. Improvements.

Do not claim actual execution.
Give corrected suggestions where needed.
"""

    return ask_ai(prompt)


# 5. Report Agent
def report_agent(task, results):

    prompt = f"""
You are NexusAI Report Agent.

Original Task:
{task}

Results from all agents:
{results}

Create a professional final report.

Include:
1. Task Summary
2. Manager Agent Decision
3. Research Findings
4. Generated Code or Solution
5. Testing and Review
6. Recommendations
7. Limitations

Do not claim work was completed if it was not performed.
"""

    return ask_ai(prompt)

print("NexusAI: All  Agents Loaded Successfully!")
