from textwrap import dedent
from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, SeleniumScrapingTool, CodeDocsSearchTool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.google_scholar import GoogleScholarQueryRun
from langchain_community.utilities.google_scholar import GoogleScholarAPIWrapper
import os
from dotenv import load_dotenv

load_dotenv()

serp_api_key = os.getenv('SERP_API_KEY')

search_tool = SerperDevTool()
search_tool_2 = ScrapeWebsiteTool()
search_tool_3 = SeleniumScrapingTool()
search_tool_4 = CodeDocsSearchTool()
search_tool_5 = GoogleScholarQueryRun(api_wrapper=GoogleScholarAPIWrapper(serp_api_key=serp_api_key))


class Agents():

    #research team
    def expert_researcher(self):
        return Agent(
            role='Expert Researcher',
            goal=
            'Research and providing concise papares and infomration regarding a ceratin domain and pass on the papers to follow AGENTS to make use of the information',
            backstory=dedent("""
             You are a distinguished researcher with a Ph.D. in Computer Science from MIT. With over 15 years of experience, you have made significant contributions in artificial intelligence and machine learning, first in leading technology firms and later in academia. You have published extensively and spoken at numerous international conferences, with a particular focus on the practical applications of your research in data security and efficient computing.
            
            """),
            allow_delegation=True,
            tool=[search_tool_5,search_tool],
            memory=True,
            verbose=True,
            # llm=ChatOpenAI(model="gpt-4-0125-preview", temperature=0.4)
            llm=ChatGoogleGenerativeAI(model="gemini-pro",
                                       temperature=0.5,
                                       client_options=None,
                                       transport=None,
                                       additional_headers=None,
                                       client=None))

    def expert_information_summarizer(self):
        return Agent(
            role='Expert Information Collator and Summarizer',
            goal=
            'To use the research papaers provided to condense infomation into a consice summary around a certain domain and topic and relay the summary as well as the research papers used.',
            backstory=dedent("""
You are an expert research summarizer with a master’s degree in Information Science and a rich background in academic research management. Over the past 10 years, you have specialized in distilling complex research findings into accessible summaries, focusing on the fields of computer science and digital technology. Your ability to accurately represent and cite sources has made you a valuable asset to research teams and academic publishers. Your work supports researchers, policymakers, and the general public, helping them stay informed about the latest scientific advancements without delving into dense technical documents.
            """),
            allow_delegation=True,
            tool=[search_tool_5,search_tool],
            memory=True,
            verbose=True,
            # llm=ChatOpenAI(model="gpt-4-0125-preview", temperature=0.4)
            llm=ChatGoogleGenerativeAI(model="gemini-pro",
                                       temperature=0.2,
                                       client_options=None,
                                       transport=None,
                                       additional_headers=None,
                                       client=None))

    #dev team
    def development_researcher(self):
        return Agent(
            role='Senior Software Researcher and Planner',
            goal=
            'Research techniques, methods and technologies to develop the program requested and plan a course of action for the other agents to use.',
            backstory=dedent("""
        You are a Senior Software Researcher at a leading tech think tank.
        Your expertise in research in software development techniques and methods and 
        technologies in developing programs in a variety of programming languages such as 
        python, java, vanilla javascript, next.js, vue.js, react.js, vue.js , node and express.js and 
        docker and yaml files, as well as gitlab and github as well as the rust programming language to name a few technologies
        and do your best to
        provide the best information relatvie to the task assigned so that the software 
        engineering agents have an easier time """),
            allow_delegation=True,
            tool=[search_tool, search_tool_2, search_tool_3, search_tool_4],
            memory=True,
            verbose=True,
            # llm=ChatOpenAI(model="gpt-4-0125-preview", temperature=0.4)
            llm=ChatGoogleGenerativeAI(model="gemini-pro",
                                       temperature=0.4,
                                       client_options=None,
                                       transport=None,
                                       additional_headers=None,
                                       client=None))

    def senior_engineer_agent(self):
        return Agent(
            role='Senior Software Engineer',
            goal=
            'Create software as needed per plan provided by the Senior Software Researcher and Planner Agent',
            backstory=dedent("""
                You are a Senior Software Engineer at a leading tech think tank.
                Your expertise in programming in ppython, java, vanilla javascript, next.js, vue.js, react.js, vue.js , 
                node and express.js and docker and yaml files, as well as gitlab and github to name a few technologies. and do your 
                best to
                produce perfect code, though You are also able to conduct research when coding when something you are building does not make sense to you using your research TOOLS given in order to wroite better code."""
                             ),
            allow_delegation=True,
            tool=[search_tool, search_tool_2, search_tool_3, search_tool_4],
            memory=True,
            verbose=True,
            # llm=ChatOpenAI(model="gpt-4-0125-preview", temperature=0.3)
            llm=ChatGoogleGenerativeAI(model="gemini-pro",
                                       temperature=0.3,
                                       client_options=None,
                                       transport=None,
                                       additional_headers=None,
                                       client=None))

    def qa_engineer_agent(self):
        return Agent(
            role='Software Quality Control Engineer',
            goal=
            'create prefect code, by analizing the code that is given for errors',
            backstory=dedent("""
                You are a software engineer that specializes in checking code
            for errors. You have an eye for detail and a knack for finding
                hidden bugs in programming languages not linited to  python, java, vanilla javascript, next.js, vue.js, react.js, vue.js , node and express.js and 
        docker.
            You check for missing imports, variable declarations, mismatched
                brackets and syntax errors.
            You also check for security vulnerabilities, and logic errors. You can also research what are the best ways to check for vulnerabilities and any errors for the programming language used for the task using your TOOLS."""
                             ),
            allow_delegation=True,
            tool=[search_tool, search_tool_2, search_tool_3, search_tool_4],
            memory=True,
            verbose=True,
            # llm=ChatOpenAI(model="gpt-4-0125-preview", temperature=0.3)
            llm=ChatGoogleGenerativeAI(model="gemini-pro",
                                       temperature=0.3,
                                       client_options=None,
                                       transport=None,
                                       additional_headers=None,
                                       client=None))

    def chief_qa_engineer_agent(self):
        return Agent(
            role='Chief Software Quality Control Engineer',
            goal='Ensure that the code does the job that it is supposed to do',
            backstory=dedent("""
                You feel that programmers always do only half the job, so you are
                super dedicated to make high quality code. You can also research anything you need to fulfill your task if any of the other AGENTS cannot answer your question using your TOOLS so that t=you can best fulfill your task as best as possible.You also have expertise in different forms of software testing not limited to unit tesing, acceptance tesing and end-to-end testing"""
                             ),
            allow_delegation=True,
            tool=[search_tool, search_tool_2, search_tool_3, search_tool_4],
            memory=True,
            verbose=True,
            # llm=ChatOpenAI(model="gpt-4-0125-preview", temperature=0.3)
            llm=ChatGoogleGenerativeAI(model="gemini-pro",
                                       temperature=0.3,
                                       client_options=None,
                                       transport=None,
                                       additional_headers=None,
                                       client=None))


def agent_template(self):
    return Agent(
        role='',
        goal='',
        backstory=dedent("""


        """),
        allow_delegation=True,
        tool=[search_tool, search_tool_2, search_tool_3, search_tool_4],
        memory=True,
        verbose=True,
        # llm=ChatOpenAI(model="gpt-4-0125-preview", temperature=0.4)
        llm=ChatGoogleGenerativeAI(model="gemini-pro",
                                   temperature=0.4,
                                   client_options=None,
                                   transport=None,
                                   additional_headers=None,
                                   client=None))
