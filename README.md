
First Create an init with uv
```
uv init my-adk-agent
```

Then move to the folder

```
cd my-adk-agent
```

Create a venv for the agent
```
uv venv
uv run
```

then add google adk to the project

```
uv add google-adk
```
add dependencies
```
 uv add langchain-community tavily-python litellm
```
then sync them with environment 
```
uv sync
```

project view
```
google-adk/
├── agent_module/
│   ├── __init__.py
│   └── agent.py
├── .venv/
└── .env
```

```
# agent_module/__init__.py
from . import agent
```


Command to run

```
adk web
```
