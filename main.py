import os
import sys
import uvicorn
import importlib.util
from fastapi import FastAPI

# Suppress tracing warnings during development
os.environ.setdefault("OTEL_SDK_DISABLED", "true")

from google.adk.cli.fast_api import get_fast_api_app

# Get the directory where main.py is located
APP_DIR = os.path.dirname(os.path.abspath(__file__))

# Add parent directory to sys.path if it's not there already
# This fixes the module import issue
parent_dir = os.path.abspath(os.path.join(APP_DIR, os.pardir))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Fix for 'ai-agent' module import
# Needed because the framework expects the code to be importable
# under the app's name.
# TODO(adk): Make this automatic.
import types

# Only register the module if it hasn't been registered already
if 'ai-agent' not in sys.modules:
    # Create a proper module for 'ai-agent'
    ai_agent_module = types.ModuleType('ai-agent')
    sys.modules['ai-agent'] = ai_agent_module

    # Import the actual agent code
    import agent

    # Make it available as 'ai-agent.agent'
    ai_agent_module.agent = agent
    # Expose the root agent directly if it exists
    if hasattr(agent, 'root_agent'):
        ai_agent_module.root_agent = agent.root_agent

    print(f"Registered 'ai-agent' and 'ai-agent.agent' in sys.modules")
else:
    # Module already registered, just import agent
    import agent

# Example session DB URL (e.g., SQLite)
SESSION_DB_URL = "sqlite:///./sessions.db"

# Example allowed origins for CORS
ALLOWED_ORIGINS = ["http://localhost", "http://localhost:8080", "*"]

# Call the function to get the FastAPI app instance
# The function requires 'agents_dir' and 'web' as mandatory arguments
app: FastAPI = get_fast_api_app(
    agents_dir=APP_DIR,  # Directory containing the agent code
    web=True,  # Enable web interface
    session_db_url=SESSION_DB_URL,
    allow_origins=ALLOWED_ORIGINS,
)

if __name__ == "__main__":
    # Use port 8080 by default, or override with PORT env var
    port = int(os.environ.get("PORT", 8080))
    print(f"Starting agent server on port {port}...")
    
    # Run the server using uvicorn
    # Use import string format to enable reload functionality
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True) 