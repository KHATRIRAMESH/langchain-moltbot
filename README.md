# langchain-moltbot

A Telegram bot powered by LangGraph and OpenAI that can search the web, perform calculations, and read/write files.

## Features

- 🤖 **AI-Powered Conversations** - Uses GPT-4o-mini via LangGraph's ReAct agent
- 🔍 **Web Search** - Search the internet using DuckDuckGo
- 🧮 **Calculator** - Perform mathematical calculations
- 📁 **File Operations** - Read and write files in the workspace
- 💾 **Memory Persistence** - Maintains conversation context per chat

## Project Structure

```
langchain-moltbot/
├── README.md
├── requirements.txt
└── workspace/
    ├── agent.py          # LangGraph agent with tools
    └── telegram_bot.py   # Telegram bot interface
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
pip install -U ddgs  # Required for DuckDuckGo search
```

### 2. Configure Environment Variables

Add the following to your `.env` file:

```env
OPENAI_API_KEY="your-openai-api-key"
TELEGRAM_BOT_TOKEN="your-telegram-bot-token"
```

Get your Telegram bot token from [@BotFather](https://t.me/BotFather).

### 3. Run the Bot

```bash
python workspace/telegram_bot.py
```

## Usage

1. Start a chat with your bot on Telegram
2. Send `/start` to get a welcome message
3. Ask questions, request calculations, or search the web

### Example Commands

- "What's the weather like in Tokyo?"
- "Calculate 25 \* 4 + 100"
- "Search for the latest news about AI"
- "Write a file called notes.txt with some content"

## Tools Available

| Tool         | Description                             |
| ------------ | --------------------------------------- |
| `search`     | Search the web using DuckDuckGo         |
| `calculator` | Evaluate mathematical expressions       |
| `read_file`  | Read files from the workspace folder    |
| `write_file` | Write content to files in the workspace |

## Technologies

- [LangChain](https://langchain.com/) - LLM framework
- [LangGraph](https://langchain-ai.github.io/langgraph/) - Agent orchestration
- [OpenAI GPT-4o-mini](https://openai.com/) - Language model
- [python-telegram-bot](https://python-telegram-bot.org/) - Telegram API wrapper
- [DuckDuckGo Search](https://duckduckgo.com/) - Web search

## License

MIT
