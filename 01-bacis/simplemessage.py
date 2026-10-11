from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1)

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

#if __name__=="__main__":
    #response=model.invoke(messages)#mesaj atıp cevap almaya yarar
    #print(response)
    #content='Ciao!' response_metadata={'prompt_feedback': {'block_reason': 0, 'safety_ratings': []}, 'finish_reason': 'STOP', 'safety_ratings': []} id='run-7a996e61-1ec3-4961-973f-8211f2bf49e3-0' usage_metadata={'input_tokens': 10, 'output_tokens': 2, 'total_tokens': 44}
    #bilerek kapatıldı gereksiz istek atmayayım diye
    # print(response.content) şeklinde direkt cevabı alabiliriz
