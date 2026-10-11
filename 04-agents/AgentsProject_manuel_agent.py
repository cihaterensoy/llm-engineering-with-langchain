from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
#from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain import hub
from langchain.agents import create_react_agent,AgentExecutor
from langchain_core.prompts import PromptTemplate
load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
memory=SqliteSaver.from_conn_string(":memory:")
search = TavilySearchResults(max_results=2)#maksimum kaç sonuç istiyoruz diye parametre alıyor

#prompt = hub.pull("hwchase17/react-chat")


tools=[search]
prompt = PromptTemplate.from_template("""
You are a helpful assistant.

You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
Thought: I now know the final answer
Final Answer: the final answer to the user

Question: {input}
Thought: {agent_scratchpad}
""")
agent=create_react_agent(model,tools,prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, checkpoint=memory)
config = {"configurable": {"thread_id": "abc123"}}

if __name__ == '__main__':
    chat_history = []

    while True:
        user_input = input(">")
        chat_history.append(f"Human: {user_input}")

        response = []
        for chunk in agent_executor.stream(
                {
                    "input": user_input,
                    "chat_history": "\n".join(chat_history),
                },
                config
        ):
            if 'text' in chunk:
                print(chunk['text'], end='')
                response.append(chunk['text'])

        chat_history.append(f"AI: {''.join(response)}")
        print("\n----")