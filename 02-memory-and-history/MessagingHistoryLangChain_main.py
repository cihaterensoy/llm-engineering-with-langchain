from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.chat_history import  BaseChatMessageHistory,InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

store={}

def get_session_history(session_id : str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()#memory'i döndürüyor sessiona göre
    return store[session_id]
#session id yoksa onun session id'sini stroe'a kaydedip dönüdürüyoruz

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Answer all questions to the best of your ability."),
        MessagesPlaceholder(variable_name="messages")
    ]
)

chain=prompt | model
config={"configurable":{"session_id":"abcde123"}} #session id'mizi burada takip ettiriyoruz

with_message_history=RunnableWithMessageHistory(chain,get_session_history)
#hangi chain'i çalıştıracağız ve onun sessionu alacağı fonksiyonu soruyor


if __name__=="__main__":
    """
    while True:
        user_input=input("Enter message:")
        response=with_message_history.invoke( #chane.invoke demiyoruz
            [
                HumanMessage(content=user_input),
            ],
            config=config
        )
        print(response.content)
    """
    while True:
        user_input = input("Enter message:")
        for r in with_message_history.stream(  # chane.invoke demiyoruz
            [
                HumanMessage(content=user_input),
            ],
            config=config
        ):
            print(r.content,end=" ")