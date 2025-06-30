Search_Engine_LLM
=================

This is a Streamlit-based AI-powered chatbot that integrates with LangChain and uses Groq's Llama3-8b-8192 model to search and respond using live data from the web. It fetches results from Tavily Search, Wikipedia, and Arxiv.

📚 Features
----------
- 🔍 Real-time search using Tavily (web), Wikipedia, and Arxiv.
- 💬 Conversational interface with LangChain Agent.
- 🧠 Powered by Groq's blazing fast LLM via API key.
- 🖥️ Simple UI using Streamlit.
- 🛠️ Uses `StreamlitCallbackHandler` to show thought steps of the agent.

🧪 Tech Stack
------------
- Python
- Streamlit
- LangChain
- Groq API
- Tavily Search API
- Wikipedia & Arxiv API Wrappers
- dotenv for environment management

🚀 Getting Started
------------------

1. **Clone the repository:**
git clone https://github.com/PrinceChauhanhub/Search_Engine_LLM.git
cd Search_Engine_LLM

2. **Install dependencies:**
pip install -r requirements.txt

3. **Set your environment variables:**

Create a `.env` file in the root folder with the following:
TAVILY_API_KEY=your_tavily_api_key_here

4. **Run the Streamlit app:**
streamlit run app.py

5. **Enter your Groq API key in the sidebar of the app.**

📝 How It Works
---------------
- The app uses LangChain's `initialize_agent` with a zero-shot reasoning agent.
- It queries sources like Tavily, Wikipedia, and Arxiv depending on your question.
- The Groq-hosted Llama3 model processes your query and integrates results into a natural reply.
- The chatbot interface is displayed using Streamlit.

🔐 API Keys Required
--------------------
- **Groq API Key** – Entered in the Streamlit sidebar.
- **Tavily API Key** – Stored in `.env` as `TAVILY_API_KEY`.

🛠️ Example Tools Used
----------------------
- `TavilySearchResults`
- `ArxivQueryRun`
- `WikipediaQueryRun`

📎 Useful Links
---------------
- Groq: https://console.groq.com
- Tavily: https://www.tavily.com
- LangChain Docs: https://docs.langchain.com

🙋‍♂️ Author
-----------
👨‍💻 Prince Chauhan  
🔗 GitHub: https://github.com/PrinceChauhanhub
