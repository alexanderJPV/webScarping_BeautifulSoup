import requests

def telegram_bot_sendtext(bot_message):
    bot_token = '1400374312:AAFkM5XdW4wPRXAzPqSLTKKlM6ezj8j6XCI'
    bot_chatID = '82240544'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


test = telegram_bot_sendtext("Mensaje desde python script hay oferat!!! ")
#print(test)