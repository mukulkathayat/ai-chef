from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from decouple import config

def askjarvischef(recipe_message):
    SECRET_KEY = config('OPENAI_API_KEY')
    chat = ChatOpenAI(openai_api_key=SECRET_KEY, model_name="gpt-3.5-turbo")
    systemMessagePrompt= SystemMessagePromptTemplate.from_template("""Your name is Jarvis, you are a masterchef who can tell
                                                                   recipes to cook. You are very helpful and friendly.
                                                                   You are not allowed to answer anything that is not
                                                                   related to cooking. If someone asks you a question
                                                                   that is not related to cooking, you should just
                                                                   answer "I don't know". You should always be""")
    
    humanMessagePrompt = HumanMessagePromptTemplate.from_template(f"{recipe_message}")
    
    chatPrompt = ChatPromptTemplate.from_messages([systemMessagePrompt, humanMessagePrompt])
    
    formatted_prompt = chatPrompt.format_prompt(recipe_message=recipe_message)
    response = chat.invoke(formatted_prompt)
    
    return response.content