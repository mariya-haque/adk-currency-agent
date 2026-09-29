from google.adk.agents import Agent
from tools import get_exchange_rate

root_agent = Agent(
    name="currency_exchange_agent",
    model="gemini-3.1-flash",
    instruction="""
You are a currency exchange assistant.

Whenever the user asks for currency conversion or exchange rates,
use the get_exchange_rate tool.
Explain the result in a friendly manner.
""",
    tools=[get_exchange_rate],
)