from requests import post
from collections import deque
from classes.Message import Message
import os
from data import get_data_from_file, update_conversation
from objsize import get_deep_size
from dotenv import load_dotenv
load_dotenv()

PALM_KEY = os.environ.get('PALM_KEY')
BASE_URL = os.environ.get('BASE_URL')
url = f"{BASE_URL}{PALM_KEY}"

prompter = {
    "prompt": {
        "context": "You are Charlie, the smartest and oldest owl in the forest. Try not to mention who you are without being asked first, but answer accordingly",
        "messages": []
    }
}

def ask(str, chat_id):
    error_msg = 'An error occurred. Can you please try again?'
    try:
        conversation = get_data_from_file(chat_id)
        if not conversation:
             return error_msg
        messages = conversation['messages']
        messages.append(Message(str).__dict__)
        while get_deep_size(messages) > 1800 or len(messages) >= 20:
            messages.pop(0)

        prompter['prompt']['messages'] = messages
        response = post(url, json=prompter)
        data = response.json()
        print(data)

        #check if any answer candidates exist
        if len(data['candidates']) <= 0:
            if data['filters']:
                print(data['filters'])
            return error_msg
        answer = data['candidates'][0]
        messages.append(answer)
        
        update_conversation(messages=list(messages), chat_id=chat_id)
        return answer['content']
    
    #handle a case where no candidates are returned
    except KeyError as e:
            print(e)
            return error_msg
    except Exception as e:
            print(e)
            return error_msg