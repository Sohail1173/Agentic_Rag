from langchain_community.utilities import GoogleSerperAPIWrapper
from crewai.tools import BaseTool
from pydantic import Field
from crewai_tools import PDFSearchTool
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import os
import requests
from dotenv import load_dotenv
load_dotenv()
os.environ['SERPER_API_KEY'] = os.getenv("SERPER_API_KEY")
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")


response_llm=ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model_name="DeepSeek-R1-Distill-Llama-70B",
            temperature=0.6,
            max_tokens=2048,
        )

pdf_url='https://arxiv.org/pdf/2405.01577' 
response = requests.get(pdf_url)

with open('hatespeech.pdf', 'wb') as file:
    file.write(response.content)