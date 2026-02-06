import os
import asyncio
from dotenv import load_dotenv

# Load .env from the project root
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

from agent import agent
from langchain_core.messages import HumanMessage

load_dotenv()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi! I'm a LangGraph + OpenAI agent.\n"
        "I can search the web, do math, read/write files in workspace/.\n"
        "Just talk to me!"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    chat_id = str(update.effective_chat.id)
    user_text = update.message.text

    config = {"configurable": {"thread_id": chat_id}}  # persistence per chat

    # Run agent (async version)
    result = await agent.ainvoke(
        {"messages": [HumanMessage(content=user_text)]}, config=config
    )

    response = result["messages"][-1].content
    await update.message.reply_text(response)


if __name__ == "__main__":
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        print("❌ TELEGRAM_BOT_TOKEN missing in .env")
        exit(1)

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🚀 Bot is running... (Ctrl+C to stop)")
    app.run_polling()
