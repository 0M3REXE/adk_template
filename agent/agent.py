from google.adk import Agent
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools.agent_tool import AgentTool
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.tools import google_search




APP_NAME = "startup_agent" 
USER_ID = "user_test_1"
SESSION_ID = "session_abc_123"
MODEL = "gemini-2.0-flash-exp"

root_agent = Agent(
    name = APP_NAME,
    model= MODEL,
    description="An agent that helps you with startup ideas and business plans.",
    instruction="""Give a warm greeting to the User and ask how you can help them today.
    Take the user input and provide it to the 'generate_startup_idea' tool.
    Then take the result from generate_startup_idea and provide it to the 'validate_startup_idea' tool.
    Then take the result from validate_startup_idea and provide it to the 'create_startup_plan' tool.
    Finally, present the startup plan from create_startup_plan to the user in a clear, structured format.
    
    Use the Google search tool when you need to research market trends, competitors, or gather additional information to enhance the startup idea or validation process.
    
    Be sure to maintain context between steps and provide thoughtful transitions between each phase of the process.
    """,
    tools=[google_search]
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
