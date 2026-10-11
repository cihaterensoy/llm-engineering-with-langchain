from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1)
"""
messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]"""
system_prompt = "Translate the following into {language}"
prompt_tamplate=ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),("user","{text}")
    ]
)
parser=StrOutputParser()
#response=model.invoke(messages)
#response'yi böyle yazmak yerine
#chainleri birbirine bağlamak icin kullanılan tekniği kullanabiliriz
#chain=model | parser


#chain=prompt_tamplate | model | parser
#if __name__=="__main__":
    #print(parser.invoke(response)) #bu şekilde direkt content'in içeriğini alabiliriz response.content ilede yapabilirdik bunu ancak ilerleyen adımlarda kullanacağız
    #print(chain.invoke({"language":"italian","text":"Hi"})) 