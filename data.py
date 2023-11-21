import json
from classes.Conversation import Conversation

def guard(chat_id):
    with open("data.json") as file:
        data = json.load(file)
        if chat_id in data['allowed']:
            return True
    return False

def get_data_from_file(chat_id):
    try:
        with open("data.json") as file:
            data = json.load(file)
            for conversation in data['conversations']:
                if conversation['id'] == chat_id:
                     return conversation
            
            return Conversation(chat_id).__dict__
            
    except Exception as e:
         print(e)
    finally:
        file.close()
    
def update_conversation(messages, chat_id):
    try:
        with open("data.json", "+r") as file:
            data = json.load(file)
            conversation_exists = False
            for conversation in data['conversations']:
                if conversation['id'] == chat_id:
                     conversation['messages'] = messages
                     conversation_exists = True
            if not conversation_exists:
                new_conversation = Conversation(chat_id).__dict__
                new_conversation['messages'] = messages
                data['conversations'].append(new_conversation)

            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
    except Exception as e:
        print(e)
        print(f"Failed to update conversation for {chat_id}")
    finally:
        file.close()

def open_conversation(chat_id: int):
    try:
        with open("data.json", "+r") as file:
            data = json.load(file)
            if id in data['allowed']:
                return True
            else:
                data['allowed'].append(int(chat_id))
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
            return True
    except Exception as e:
        print(e)
        return False
    
def close_conversation(chat_id: int):
    try:
        with open("data.json", "+r") as file:
            data = json.load(file)
            chat_id = int(chat_id)
            if chat_id not in data['allowed']:
                return False
            else:
                data['allowed'].remove(chat_id)
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
            return True
    except Exception as e:
        print(e)
        return False