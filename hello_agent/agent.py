from google.adk.agents import Agent
from google.adk.cli.built_in_agents.adk_agent_builder_assistant import root_agent


def greet_user():
    return "안녕하세요"

root_agent = Agent (
    name="hello_agent",
    model="gemini-3-flash-preview",
    description="유저와 인사하는 에이전트입니다.",
    instruction="사용자에게 반갑고 친절하게 인사해 주세요",
    tools=[greet_user]
)