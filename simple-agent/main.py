from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os 
import asyncio

load_dotenv()
# ... imports ...

load_dotenv()

# --- DEBUG BLOCK ---
api_key = os.getenv("FIRECRAWL_API_KEY")
print(f"DEBUG: Found API Key? {api_key is not None}")
if api_key:
    print(f"DEBUG: Key starts with: {api_key[:5]}...")
else:
    print("CRITICAL ERROR: .env file not loaded or key is missing.")
    exit() # Stop here so we don't get the confusing Pydantic error
# -------------------

# params to connect mcp tool server
server_params = StdioServerParameters(
    command="npx.cmd",
    env={
        "FIRECRAWL_API_KEY": api_key, # Use the variable we just checked
    },
    args=["firecrawl-mcp"]
)

# ... rest of main() ...


model = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

#params to connect mcp tool server
server_params= StdioServerParameters(
    command = "npx.cmd",
    env={
        "FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY"),
    },
    args=["firecrawl-mcp"]
)

async def main():
    async with stdio_client(server_params) as (read,write): #mcp client
        async with ClientSession(read,write) as session:
            await session.initialize()
            tools=await load_mcp_tools(session)
            agent=create_react_agent(model,tools) #create agent
            
            messages=[
                {
                    "role":"system",
                    "content": "You are a helpful assistant that can scrape websites, crawl pages, and extract data using Firecrawl tools. Think step by step and use the appropriate tools to help the user."
                }
            ]
            
            print("Available tools-", *[tool.name for tool in tools])
            print('-'*50)
            
            while True:
                user_input = input("\nYou: ")
                if user_input == "quit":
                    print("Goodbye")
                    break
                
                messages.append({"role": "user", "content":user_input[0:175000]})
                
                try:
                    agent_response = await agent.ainvoke({"messages":messages})
                    ai_message = agent_response["messages"][-1].content
                    print("\nAgent: ", ai_message )
                
                except Exception as e:
                        print("Error: ", e)
                        
if __name__ == "__main__" :
    asyncio.run(main())                        
                
            
            