from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

# Define prompt
prompt_template = """Write a concise summary of the following:
"{text}"
CONCISE SUMMARY:"""
prompt = PromptTemplate.from_template(prompt_template)


# business logic for summarization
class Summarize():
    def __init__(self):
        # define LLM model
        self.llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")
        # Initializing an LLM chain with a prompt
        self.llm_chain = LLMChain(llm=self.llm, prompt=prompt)

    def summarize(self, text):
        result = self.llm_chain.run(text)
        return result
