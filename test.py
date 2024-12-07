from swarm import Agent
from swarm.rabbitmq.swarm import SwarmRabbitMQ

# RabbitMQ configuration
rabbitmq_config = {
    "host": "localhost",
    "port": 5672,
    "username": "guest",
    "password": "guest",
}

# Initialize SwarmRabbitMQ
client = SwarmRabbitMQ(rabbitmq_config=rabbitmq_config)


def transfer_to_agent_b():
    return agent_b


# Define agents
agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b],
)

agent_b = Agent(
    name="Agent B",
    instructions="Only speak in Haikus.",
)

# Register agents
client.register_agent(agent_a)
client.register_agent(agent_b)

# Run the system
response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to talk to agent B."}],
)

print(response.messages[-1]["content"])
