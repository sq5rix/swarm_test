from swarm import Agent, Swarm

from models import model_list
from prompts import *

client = Swarm()

QWEN7 = 2
LLAMA7 = 0
GPT = 10


def order_code():
    return agent_b


agent_a = Agent(
    name="ProjectManager",
    model=model_list[QWEN7],
    instructions="You are project manager.",
    functions=[order_code],
)

agent_b = Agent(
    name="Programmer",
    model=model_list[QWEN7a],
    instructions=PROGRAM_PYTHON_PROMPT,
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": PROJECT_MANAGER_PROMPT}],
)

print(response.messages[-1]["content"])
