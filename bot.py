import os
import logging
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, InlineQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "Welcome to **English Quick Tutor**! 📚✨\n\n"
        "Your daily companion for mastering simple English grammar, vocabulary, and common idioms.\n\n"
        "**Available Commands:**\n"
        "/word - Get the Word of the Day\n"
        "/tip - Get a quick grammar rule\n\n"
        "💡 *Tip:* You can also use me in **Inline Mode** in any chat by typing: "
        "`@YourBotUsername [any word/phrase]`"
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")

async def word_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📖 **Word of the Day: Resilient**\n\n"
        "*Meaning:* Able to withstand or recover quickly from difficult conditions.\n"
        "*Example:* Despite facing multiple setbacks, her resilient attitude kept her moving forward."
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def tip_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "💡 **Grammar Tip: Affect vs. Effect**\n\n"
        "• **Affect** is usually a *verb* (action). *Ex: The rain will affect the game.*\n"
        "• **Effect** is usually a *noun* (result). *Ex: The medicine had an immediate effect.*"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return

    results = [
        InlineQueryResultArticle(
            id=query,
            title=f"English Quick Rule for: '{query}'",
            input_message_content=InputTextMessageContent(
                f"📚 **English Learning Hub**\n\n"
                f"Searched term: *{query}*\n"
                f"💡 *Quick Tip:* Always review context when learning new vocabulary to ensure proper usage in conversation."
            , parse_mode="Markdown")
        )
    ]
    await update.inline_query.answer(results, cache_time=1)

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN environment variable is missing!")
    
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("word", word_command))
    app.add_handler(CommandHandler("tip", tip_command))
    app.add_handler(InlineQueryHandler(inline_query))
    
    print("Bot is polling successfully...")
    app.run_polling()

if __name__ == '__main__':
    main()
