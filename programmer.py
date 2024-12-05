from swarm import Agent, Swarm

from models import model_list
from prompts import *

client = Swarm()

QWEN7 = 2
LLAMA7 = 0
GPT = 10


def order_code():
    return agent_b


def test_code():
    return agent_c


def execute_code(code=None, test_code=None):
    return agent_d


agent_a = Agent(
    name="ProjectManager",
    model=model_list[QWEN7],
    instructions="You are project manager.",
    functions=[order_code, test_code, execute_code],
)

agent_b = Agent(
    name="Programmer",
    model=model_list[QWEN7],
    instructions=PROGRAM_PYTHON_PROMPT,
)

agent_c = Agent(
    name="Tester",
    model=model_list[QWEN7],
    instructions=TESTER_PROMPT,
)

agent_d = Agent(
    name="Executor",
    model=model_list[QWEN7],
    instructions=SYSTEM_EXECUTOR_PROMPT,
)

response = client.run(
    agent=agent_a, messages=[{"role": "user", "content": PROJECT_MANAGER_PROMPT}]
)

print(response.messages[-1]["content"])
