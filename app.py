import streamlit as st
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from environment
tavily_api_key = os.getenv("TAVILY_API_KEY")

# Streamlit app title and intro
st.title("🔎 LangChain - Chat with Search")
st.markdown("""
Use this chatbot to search via **Arxiv**, **Wikipedia**, or **Tavily Web Search**.
> 🛡️ **Note**: You must enter your **Groq API key** in the sidebar to chat.
""")

# Sidebar for entering Groq API Key
st.sidebar.title("Settings")
groq_api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

# Display past chat messages
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# Check for API key before enabling chat
if groq_api_key:
    if prompt := st.chat_input("Ask me anything..."):
        st.session_state["messages"].append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        try:
            # Initialize LLM
            llm = ChatGroq(
                groq_api_key=groq_api_key,
                model_name="Llama3-8b-8192",
                streaming=True
            )

            # Setup tools
            arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
            arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

            wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
            wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

            tavily = TavilySearchResults(tavily_api_key=tavily_api_key)

            tools = [tavily, arxiv, wiki]

            # Create the agent
            agent = initialize_agent(
                tools,
                llm,
                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                handle_parsing_errors=True
            )

            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
                response = agent.run(prompt, callbacks=[st_cb])
                st.session_state["messages"].append({"role": "assistant", "content": response})
                st.write(response)

        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
else:
    st.info("🔐 Please enter your Groq API key in the sidebar to start chatting.")
