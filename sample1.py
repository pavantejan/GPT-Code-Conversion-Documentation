import codecs
import gradio as gr
import openai

openai.api_key = ""

print("Do you want code documentation expert press 1 or code convertion expert press 2")
n = int(input())
if( n == 1):
    messages = [{"role": "system", "content": "You are a Code Documentation expert that specializes in understanding Java code and adding the comments in Java code"}]    
else:
    messages = [{"role": "system", "content": "You are a Code Convertion expert that specializes in understanding Java and convert it into Python"}]


def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )

    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})

    return ChatGPT_reply

def get_java_code_from_file(file_path):

  with codecs.open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

  return code


def get_java_code_from_file_and_send_to_chatGPT(file_path):
    code = get_java_code_from_file(file_path)
    return CustomChatGPT(code)


interface = gr.Interface(
  fn=get_java_code_from_file_and_send_to_chatGPT,
  inputs = "text",
  outputs = "text",
  title = "Coding Expert"
)

interface.launch(share=True)
