import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# 1. Define a simple tool the agent can use (e.g., a math tool)
def simple_calculator(query: str) -> str:
    try:
        return str(eval(query))
    except:
        return "Sorry, I can't calculate that."

tools = [
    Tool(
        name="Calculator",
        func=simple_calculator,
        description="Useful for solving basic math queries. Input should be a math expression."
    )
]

# 2. Define the language model
llm = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)

# 3. Set up memory for the agent
memory = ConversationBufferMemory(memory_key="chat_history")

# 4. Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory
)

# 5. Chat with the agent
print("🤖 Your AI Agent is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Agent: Goodbye! 👋")
        break
    response = agent.run(user_input)
    print(f"Agent: {response}\n")