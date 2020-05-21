from bot import telegram_chatbot
import sqlite3

bot = telegram_chatbot("config.cfg")

def get_name(req):
    query = "SELECT res FROM message WHERE req=?;"

    connection = sqlite3.connect("chatbotdb.sqlite")
    cursor = connection.cursor()
    cursor.execute(query, [req])
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    
    if len(results) != 0:
        return results[0][0]    
    return "fuck this"

def make_reply(msg):
    reply = None
    if msg is not None:
        reply = get_name(msg)
    return reply

# def switch_demo(argument):
#     switcher = {
#         "bahman": "mikhare",
#         "zohre": "vas zohreh ham mikhare vali roosh nmishe"
#     }
#     return switcher.get(argument, "vas hame mikhare vali roshon nmishe!")

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
