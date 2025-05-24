from pyrogram import Client
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL

async def send_log_message(client: Client, user_id: int, original_input_message: Message, sent_content_message: Message):
    actual_log_channel_id = 0
    if LOG_CHANNEL:
        try:
            actual_log_channel_id = int(LOG_CHANNEL)
        except ValueError:
            print(f"[LOG_ERROR] LOG_CHANNEL ('{LOG_CHANNEL}') is not a valid integer. Logging will be disabled.")
            actual_log_channel_id = 0
    
    if actual_log_channel_id == 0:
        return

    try:
        user_mention = f"[{user_id}](tg://user?id={user_id})"
        input_text = "N/A"
        if original_input_message and original_input_message.text:
            input_text = original_input_message.text.splitlines()[0]
        elif original_input_message and original_input_message.caption:
            input_text = original_input_message.caption.splitlines()[0]

        log_caption = (
            f"👤 **User:** {user_mention}\n"
            f"💬 **Input:** `{input_text}`\n\n"
            f"✅ **Content sent to user.**"
        )

        if hasattr(sent_content_message, 'forward'):
            try:
                forwarded_message = await sent_content_message.forward(chat_id=actual_log_channel_id)
                if forwarded_message:
                    await client.send_message(
                        chat_id=actual_log_channel_id,
                        text=log_caption,
                        disable_web_page_preview=True
                    )
                else:
                    final_log_text = log_caption + f"\n(Note: Content forwarding seemed to fail silently for message ID {sent_content_message.id} from chat {sent_content_message.chat.id if sent_content_message.chat else 'N/A'})"
                    await client.send_message(chat_id=actual_log_channel_id, text=final_log_text, disable_web_page_preview=True)
            except Exception as forward_err:
                print(f"[LOG_ERROR] Could not forward content to log channel {actual_log_channel_id}. Error: {forward_err}")
                final_log_text = log_caption + f"\n(Note: Content (ID: {sent_content_message.id}) could not be forwarded. Error: {forward_err})"
                await client.send_message(chat_id=actual_log_channel_id, text=final_log_text, disable_web_page_preview=True)
        else:
            final_log_text = log_caption + f"\n(Note: `sent_content_message` was not a forwardable message object.)"
            await client.send_message(chat_id=actual_log_channel_id, text=final_log_text, disable_web_page_preview=True)
    except Exception as e:
        print(f"[LOG_ERROR] General error in send_log_message for channel {actual_log_channel_id}. Error: {e}")

class Bot(Client):

    def __init__(self):
        super().__init__(
            "techvj login",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="TechVJ"),
            workers=50,
            sleep_threshold=10
        )
    
    async def start(self):
        await super().start()
        print('Bot Started Powered By @VJ_Botz')

    async def stop(self, *args):
        await super().stop()
        print('Bot Stopped Bye')

if __name__ == "__main__":
    Bot().run()
