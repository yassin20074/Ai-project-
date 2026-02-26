#calling the libraries
from langchain.agents import AgentExecutor, create_openai_functions_agent 
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

# preparing the memory using chroma
embeddings = OpenAIEmbeddings()
# toi store all user commands
memory_db = Chroma(persist_directory="memory_db", embedding_function=embeddings)

# a simple function that simulates the movement of an arm 
def move_robot_arm(coordinates: str):
    return f"Simulated: Moving arm to {coordinates}"


class AutonomousRobot:
    def init(self, tools):
        # creating the smart model
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        # tools available to the agent
        self.tools = tools
        # conversation template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a secure robotic controller. Execute tasks safely."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        
    #linking the base of the chroma
        self.memory = memory_db

# creating agent
    def create_executor(self):
        # creating agent capable of understandung and executing commands
        agent = create_openai_functions_agent(self.llm, self.tools, self.prompt)
        # sending a secure result to the user
        return AgentExecutor(agent=agent, tools=self.tools, verbose=True)