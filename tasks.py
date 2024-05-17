from textwrap import dedent
from crewai import Task


class Tasks():
    # Dev Team tasks
    def research_plan_task(self, agent, task):
        return Task(
            description=
            f"""You are tasked with creating a comprehensive and succinct plan for developing a program tailored to a specified task. If no programming language is designated, select the one you believe is most suitable for the project. Use your tools to thoroughly investigate relevant sources, including websites and documents, to gather extensive information before drafting your plan.

Instructions:

Task Description: {task} — Expand on this description as needed to clarify any ambiguities and ensure a complete understanding of the requirements.
Research: Utilize available tools to conduct a broad and deep exploration of the topic, gathering data and insights that will inform your planning process.
Planning: Develop a detailed strategy for writing the code, specifying:
Chosen programming language and rationale for its selection.
Major components and functions of the program.
Step-by-step breakdown of the development process.
Resources and tools required for implementation.
Potential challenges and proposed solutions.
Output Requirement:
Your output should be a well-structured plan detailing how to execute the program as per the task requirements. This plan should include clear steps, anticipated resources, and strategic insights, focusing solely on the planning aspects without deviating into actual coding.
            """,
            expected_output=
            "Your Final answer must be the full plan , only the plan and nothing else which will be used by the Senior Software Engineer AGENT in the next TASK",
            agent=agent)

    def code_task(self, agent, task):
        return Task(
            description=
            f"""You are assigned to develop a program based on a detailed plan provided by the Senior Software Researcher and Planner Agent. Follow the plan meticulously, ensuring that the final product aligns perfectly with the outlined specifications.

Instructions:

Task Description: {task} — Refer to the detailed plan for a comprehensive understanding of the project requirements and execution steps.
Development Process:
Construct the program as per the structured plan without alterations unless absolutely necessary.
If you encounter sections of the plan that require additional clarification or research, you may:
Conduct the research independently, ensuring it aligns with the requirements of the plan.
Request specific research assistance from the Senior Software Researcher and Planner Agent. Remember, this agent is restricted to providing research support only and cannot participate in code review, evaluation, or any other tasks beyond research.
Collaboration Guidelines:
Clearly delineate responsibilities: You handle all aspects of coding and implementation; the Senior Software Researcher and Planner Agent handles research inquiries only.
Output Requirement:
Your final output should be the complete program code, developed strictly according to the plan provided by the Senior Software Researcher and Planner Agent. Ensure that your submission contains only the program code, crafted as per the guidelines and specifications of the plan, with no additional elements included.
            """,
            expected_output=
            "Your Final answer must be the full progam code developed according to the plan provided by the Senior Software Researcher and Planner AGENT, only the progam code developed according to the plan provided by the Senior Software Researcher and Planner AGENT and nothing else which will be reviewed by the next AGENT in the next TASK",
            agent=agent)

    def review_task(self, agent, task):
        return Task(
            description=f"""
You are tasked with assisting in the development and thorough review of a program, using a designated programming language and following specific instructions. Your primary goal is to ensure that the code is error-free and adheres strictly to the detailed plan provided by the Senior Software Researcher and Planner Agent.

Instructions:

Task Description: {task} — Refer to this task description and any additional instructions provided in the plan for a clear understanding of the programming requirements.
Code Review Process:
Carefully examine the code for various types of errors including:
Logic errors that could affect the functionality.
Syntax errors that prevent the code from running.
Missing imports and variable declarations.
Mismatched brackets that could lead to execution failures.
Security vulnerabilities that could pose risks.
Document any issues found and make the necessary corrections to align with the best practices and requirements specified in the plan.
Research and Assistance Protocol:
If you need further clarification or encounter areas that require additional research during the code review, proceed as follows:
First, request assistance from the Senior Software Researcher and Planner Agent for any research-related inquiries.
If further expertise is necessary, and only after consulting the Senior Software Researcher and Planner Agent, you may seek additional help from other AGENTS.
Collaboration Guidelines:
Maintain clear communication with the Senior Software Researcher and Planner Agent regarding research needs. Adhere strictly to the provided plan without initiating unsanctioned modifications.
Output Requirement:
Your final submission should be the fully developed program code, strictly according to the specifications and plan provided by the Senior Software Researcher and Planner Agent. Ensure that your output consists solely of the refined and corrected program code, with no extraneous elements included.
            """,
            expected_output=
            "Your Final answer must be the full progam code, only the progam code and nothing else which will be evaluated by the next AGENT in the next TASK",
            agent=agent)

    def evaluate_task(self, agent, task):
        return Task(
            description=f"""
You are tasked with finalizing and reviewing a program to ensure it functions as intended and meets all specified requirements, using the chosen programming language and any additional instructions provided.

Instructions:

Task Description: {task} — Follow this detailed task description closely to understand the exact functionality and outcomes expected from the program.
Code Completion and Review Process:
Thoroughly examine the code to verify its completeness and functionality.
Ensure that the code effectively accomplishes the tasks it is designed to perform.
Identify any areas that may benefit from improvements or modifications and implement these changes to enhance performance, security, or maintainability.
Research and Collaboration Protocol:
If you encounter sections of the code that require additional insights or understanding, follow these steps:
Initially, seek assistance from the Senior Software Researcher and Planner Agent for any research-related needs.
If more specialized expertise is necessary, and only after consulting the Senior Software Researcher and Planner Agent, request help from other AGENTS to conduct the required research.
Guidelines for Modifications:
Any modifications to the code should be meticulously documented and should strictly adhere to the guidelines and plans provided by the Senior Software Researcher and Planner Agent. Ensure all changes align with the original objectives and enhance the code's effectiveness without altering its core functions.
Output Requirement:
Your final submission should consist exclusively of the fully developed program code, precisely according to the specifications and plan provided by the Senior Software Researcher and Planner Agent. Ensure that the submission includes only the program code that has been reviewed, potentially enhanced, and approved, without any extraneous content.
            """,
            expected_output=
            "Your Final answer must be the full program code, only the program code and nothing else which has be reviewed and evaluated, only the code for the developed program.",
            agent=agent)

    #Research Team tasks
    def research_task(self, agent, task):
        return Task(description=f"""
You are tasked with conducting comprehensive research on a specific topic within a designated domain. Your goal is to gather detailed information and insights to deepen understanding of the topic and support further activities related to this domain.

Instructions:

Research Topic and Domain: {task} in the domain specified  — Focus your research efforts to cover all relevant aspects of this topic, ensuring a broad yet detailed exploration of the subject matter.
Research Process:
Use available tools and resources to conduct a thorough investigation into the topic. This should include academic journals, industry reports, relevant databases, and other authoritative sources.
Evaluate the credibility of each source and prioritize information based on its relevance and accuracy.
Documentation and Synthesis:
As you gather information, maintain detailed notes and records of your findings.
Synthesize the information into a coherent summary that highlights key points, discoveries, trends, and any significant insights related to the topic.
Include any potential implications or applications of the research findings within the specified domain.
Source Compilation:
Compile a list of all sources used during your research. Provide citations and links (if available) for each source to ensure transparency and allow for further exploration.
If applicable, include brief annotations for each source, explaining its relevance and how it contributed to your understanding of the topic.
Output Requirement:
Your final submission should consist of two parts:

Part 1: A detailed report summarizing the information and insights gathered about the topic. This report should be structured to clearly convey your findings and their implications in the specified domain.
Part 2: A comprehensive list of all sources used during your research. This should include full citations and, where applicable, links and annotations.
Ensure that your final output is well-organized, meticulously documented, and provides a thorough account of the research conducted, supporting further inquiry and application.
            """,
                    expected_output=
                    """ Your final submission should consist of two parts:

Part 1: A detailed report summarizing the information and insights gathered about the topic. This report should be structured to clearly convey your findings and their implications in the specified domain.
Part 2: A comprehensive list of all sources used during your research. This should include full citations and, where applicable, links and annotations.
Ensure that your final output is well-organized, meticulously documented, and provides a thorough account of the research conducted, supporting further inquiry and application.""",
                    agent=agent)

    def summarization_and_paper_feeding(self, agent, task):
        return Task(
            description=f"""
You are tasked with creating a concise, accurate summary of {task} produced by the Expert Researcher AGENT. Your goal is to distill the essential information and insights from the report, making it easily accessible while retaining the depth and integrity of the research.

Instructions:

Review Process:
Carefully review the detailed report provided by the AI Research Agent. Understand the main points, findings, and conclusions drawn about the topic within the specified domain.
Pay special attention to the context and implications of the research as detailed in the report.
Summarization Process:
Extract key information, significant insights, and critical data points from the report. Focus on maintaining the essence and factual accuracy of the original research.
Organize your summary to reflect the structure of the research report, ensuring it flows logically and covers all major sections of the document.
Source Inclusion:
Include a list of the primary sources and research papers used in the original research report as part of your summary. This list should be derived from the comprehensive list provided by the AI Research Agent.
For each source mentioned in your summary, provide a brief explanation of its relevance to the key points being summarized. This ensures that the summary maintains a clear link to the original research and supports verification.
Output Requirement:
Your final submission should consist of two parts:

Part 1: A succinct and well-organized summary of the research report, capturing the core findings, insights, and conclusions. This summary should provide a clear overview of the research topic as explored in the report.
Part 2: A list of all sources cited in your summary, including brief annotations describing their contribution to the summarized content. Ensure this list aligns with the sources used in the research report for consistency and traceability.
Ensure that your final output is concise yet comprehensive, providing an accurate reflection of the research while facilitating easier comprehension and further discussion.
            """,
            expected_output="""The final submission should consist of two parts:

Part 1: A succinct and well-organized summary of the research report, capturing the core findings, insights, and conclusions. This summary should provide a clear overview of the research topic as explored in the report.
Part 2: A list of all sources cited in your summary, including brief annotations describing their contribution to the summarized content. Ensure this list aligns with the sources used in the research report for consistency and traceability.
Ensure that your final output is concise yet comprehensive, providing an accurate reflection of the research while facilitating easier comprehension and further discussion.""",
            agent=agent)


# Task template, outside of c;ass
def task_template(self, agent, task):
    return Task(description=f"""
You are tasked with (depending on what the agent is and what they are for)

Instructions:

Task Description: {task} — Follow this detailed task description closely

Rest of task description
        """,
                expected_output="Expected output of task",
                agent=agent)
