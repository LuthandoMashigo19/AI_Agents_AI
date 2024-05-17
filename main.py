import streamlit as st
import google.generativeai as gen_ai
import PyPDF2
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from crewai.process import Process
from crewai import Crew
from tasks import Tasks
from agents import Agents

tasks = Tasks()
agents = Agents()

load_dotenv()

GOOGLE_API_KEY = ("AIzaSyAzvYjga2f7OBF-_F3lOa8FekGtZb3Wo9U")
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')
team = ""
chatbot = model.start_chat()
extractedtext = ""
functionality = ""

with st.sidebar:
            st.subheader("AI Selection")
            functionality = st.selectbox(
                'Do you want to use the underlying AI Agents',
                ["Yes", "No, I will continue using the regular AI Chatbot"],
                key="functionality")

            if functionality == "Yes":
                        st.subheader("Crews")
                        selected_team = st.selectbox(
                            'Choose a team',
                            ['Research Team', 'Software Development Team'],
                            key='selected team')
                        if selected_team == "Research Team":
                                    team = "Research Team"
                        elif selected_team == "Software Development Team":
                                    team = "Software Development Team"


def extract_text_from_pdf(file):
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page_num in range(len(reader.pages)):
                        page = reader.pages[page_num]
                        text += page.extract_text()
            return text


st.title("Multi Functional AI")

uploaded_file = st.file_uploader("Upload your doucment")

if uploaded_file:
            extractedtext = extract_text_from_pdf(uploaded_file)

if "message" not in st.session_state:
            st.session_state["message"] = [{
                "role":
                "assistant",
                "content":
                "Hello! How can I help you today?"
            }]

for msg in st.session_state.message:
            st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

            st.session_state.message.append({
                "role": "user",
                "content": prompt
            })
            st.chat_message("user").write(prompt)

            if functionality == "Yes":
                        #AI Crew Stuff
                        task = prompt

                        #Dev Team
                        senior_researcher_planner = agents.development_researcher(
                        )
                        senior_engineer_agent = agents.senior_engineer_agent()
                        qa_engineer_agent = agents.qa_engineer_agent()
                        chief_qa_engineer_agent = agents.chief_qa_engineer_agent(
                        )

                        #Research Team
                        expert_researcher = agents.expert_researcher()
                        expert_info_summer = agents.expert_information_summarizer(
                        )

                        # Create Tasks
                        #Dev team
                        research_plan = tasks.research_plan_task(
                            senior_researcher_planner, task)
                        code = tasks.code_task(senior_engineer_agent, task)
                        review = tasks.review_task(qa_engineer_agent, task)
                        approve = tasks.evaluate_task(chief_qa_engineer_agent,
                                                      task)

                        #Research Team
                        research = tasks.research_task(expert_researcher, task)
                        paper_retrival_summarizer = tasks.summarization_and_paper_feeding(
                            expert_info_summer, task)

                        # Create Crew responsible for Management
                        #Crew Selection
                        agent_list = []
                        task_list = []
                        if team == "Research Team":
                                    agent_list = [
                                        expert_researcher, expert_info_summer
                                    ]
                                    task_list = [
                                        research, paper_retrival_summarizer
                                    ]
                        elif team == "Software Development Team":
                                    agent_list = [
                                        senior_researcher_planner,
                                        senior_engineer_agent,
                                        qa_engineer_agent,
                                        chief_qa_engineer_agent
                                    ]
                                    task_list = [
                                        research_plan, code, review, approve
                                    ]
                        crew = Crew(agents=agent_list,
                                    tasks=task_list,
                                    process=Process.hierarchical,
                                    memory=True,
                                    cache=True,
                                    manager_llm=ChatGoogleGenerativeAI(
                                        model="gemini-pro",
                                        temperature=0.4,
                                        client_options=None,
                                        transport=None,
                                        additional_headers=None,
                                        client=None),
                                    verbose=True)

                         
                        task = crew.kickoff()
                        st.chat_message("assistant").write(task)
            
            elif functionality == "No, I will continue using the regular AI Chatbot":
                        #Regular chatbot stuff
                        if extractedtext:
                                    newprompt = prompt + " : " + extractedtext
                                    genAIRes = chatbot.send_message(newprompt)
                        else:
                                    genAIRes = chatbot.send_message(prompt)

                        response = genAIRes.text

                        st.session_state.message.append({
                            "role": "assistant",
                            "content": response
                        })
                        st.chat_message("assistant").write(response)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
