from google.adk import Agent
from google.adk import Runner
from google.adk.tools import agent_tool
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.adk.code_executors import BuiltInCodeExecutor



APP_NAME = "Python_Teacher" 
USER_ID = "user_test_1"
SESSION_ID = "session_abc_123"
MODEL = "gemini-2.0-flash"

search_agent = Agent(
    model='gemini-2.0-flash',
    name='SearchAgent',
    instruction="""
    You're a specialist in Google Search for finding Python-related information, tutorials, and documentation.
    When asked to search for information, provide relevant and up-to-date results.
    Focus on educational content that would help someone learn Python programming.
    """,
    tools=[google_search]
)
coding_agent = Agent(
    model='gemini-2.0-flash',
    name='CodeAgent',
    instruction="""
    You're a specialist in Python code execution and teaching.
    When given a mathematical expression or Python code problem, write and execute Python code to demonstrate the solution.
    Always explain your code clearly and show the output.
    For teaching purposes, break down complex problems into steps and explain each part.
    When executing code, make sure to show both the code and its execution results.
    """,
    code_executor=BuiltInCodeExecutor()
)



root_agent = Agent(
    name = APP_NAME,
    model= MODEL,
    description="An agent that helps you Learn Python Code.",
    instruction="""Give a warm greeting to the User and ask how you can help them today.
    Take user input and classify if it is a question about Python code, a request for help with a specific coding problem, or a general inquiry about Python programming.
    
    If the input is a question about Python code:
    - Provide a detailed explanation and example code
    - Use the CodeAgent to execute and demonstrate the code when helpful
    
    If the input is a request for help with a specific coding problem:
    - Ask clarifying questions to understand the problem better
    - Use the CodeAgent to write, execute, and test solutions
    - Show the code execution results to validate the solution
    
    If the input is a general inquiry about Python programming:
    - Provide a brief overview of Python and its applications
    - Use practical code examples executed by the CodeAgent when appropriate
    
    For mathematical problems or calculations:
    - Always delegate to the CodeAgent to write and execute Python code
    - The CodeAgent will show both the code and the execution results
    
    For web searches or finding information:
    - Use the SearchAgent to find relevant information
    
    Always encourage the user to ask follow-up questions if they need more clarification or assistance.
    Be sure to maintain context between steps and provide thoughtful transitions between each phase of the process.
    When using agents, explain what you're doing to help the user understand the process.
    """,
     tools=[agent_tool.AgentTool(agent=search_agent), agent_tool.AgentTool(agent=coding_agent)]
)

session_service = InMemorySessionService()
session = session_service.create_session(
    user_id=USER_ID,
    session_id=SESSION_ID,
    app_name=APP_NAME
)

runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service
)
