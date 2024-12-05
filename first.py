from swarm import Agent, Swarm

from models import model_list

client = Swarm()


def transfer_to_agent_b():
    return agent_b


agent_a = Agent(
    name="Agent A",
    model=model_list[0],
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b],
)

agent_b = Agent(
    name="Agent B",
    model=model_list[0],
    instructions="Only speak in Haikus.",
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to talk to agent B."}],
)

print(response.messages[-1]["content"])
