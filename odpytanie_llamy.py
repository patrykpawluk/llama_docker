import requests

def llama_api_call(max_tokens, prompt_content, task_content, chat_history):
    chat_list = []
    chat_list.append({"role": "system", "content": prompt_content})
    for item in chat_history:
        chat_list.append({"role": item[0], "content": item[1]})
    chat_list.append({"role": "user", "content": task_content})
    payload = {
        "max_tokens": max_tokens, 
        "messages": chat_list,
    }    
    res = requests.post('http://127.0.0.1:5001/chat', json=payload)
    answear = res.json()['choices'][0]['message']['content'].strip()
    return answear

def odpytanie_llamy():

    project_template = {
        #1	Project Overview:
        'Introduction': "Brief description of the project's purpose, goals, and objectives.",
        'Scope': "Write clearly defined boundaries of the project, including what is included and excluded from the scope.",
        'Objectives': "Write specific, measurable, achievable, relevant, and time-bound (SMART) goals that the project aims to achieve.",
        #2	Requirements Documentation:
        'Functional Requirements': "What are detailed description of the desired functionality and features of the system.",
        'Non-functional Requirements': "Write specifications related to performance, security, scalability, usability, etc.",
        'Use Cases/User Stories': "Write a scenarios that describe how users will interact with the system to accomplish tasks.",
        'Acceptance Criteria': "What criteria that must be met for each requirement to be considered complete.",
        #3	Architecture and Design:
        'System Architecture': "Write high-level overview of the system's components, their interactions, and dependencies.",
        'Database Schema': "What structure and relationships of the database tables/entities are needed.",
        'Design Patterns': "What patterns and principles should be used in the design of the system to ensure scalability, maintainability, and reusability.",
        'UI/UX Design': "What wireframes, mockups, and design guidelines for the user interface are needed.",
        #4	Development Guidelines:
        'Coding Standards': "Write guidelines for writing clean, consistent, and maintainable code.",
        'Version Control': "Write procedure for using version control systems like Git, including branching and merging strategies.",
        'Testing Strategy': "Describe and approach for testing the system, including unit tests, integration tests, and end-to-end tests.",
        'Deployment Plan': "Write steps and procedures for deploying the system to production or staging environments.",
        #5	Project Management:
        'Project Schedule': "Write timeline with milestones, deliverables, and dependencies.",
        'Resource Allocation': "Write allocation of human and material resources to different tasks and activities.",
        'Risk Management': "Write identification, assessment, and mitigation strategies for potential risks and issues.",
        'Communication Plan': "Write procedures for communication among team members and stakeholders, including meeting schedules and reporting channels.",
        #6	Support and Maintenance:
        'System Documentation': "Write user manuals, technical guides, and FAQs for operating and maintaining the system.",
        'Troubleshooting': "Write procedures for identifying and resolving common issues and errors.",
        'Change Management': "Write process for handling changes and updates to the system after deployment.",
        #7	Legal and Compliance:
        'Intellectual Property Rights': "Write ownership and licensing agreements for code, assets, and third-party libraries.",
        'Regulatory Compliance': "Write compliance with relevant laws, regulations, and industry standards, such as GDPR, HIPAA, or PCI-DSS.",
        #8	Appendices:
        'Glossary': "Write definitions of technical terms and acronyms used throughout the documentation.",
        'References': "Write citations and sources of information referenced in the documentation.",
        #9	SWAT analyzis:
        'Strenghts': "Describe what a project excels at and what separates it from the competition.",
        'Weaknesses': "Describe what stop a project from performing at its optimum level.",
        'Opportunieties': "Favorable external factors that could give a project a competitive advantage.",
        'Threats': "Write which factors have the potential to harm a project",
    }

    pre_prompt = """Imagine you are a person that is connecting IT developers with customers. Customer gives you feedback what he wants to build, what kind of site, explain what features he wants in their project. Customers have none of technical knowledge. Your job is to translate customer needs into project documentation and prepare this documentation. Documentation is for engineers. It should be precise and rigorous. Focus on what technology and solution will be the best for project. The client needs are:"""
    prompt_from_client = """ "I have a store with ski equipment, and I want to start selling thru internet. I would like to have my own webstore with products and stuff. When someone want to buy something there should be, a possibility to pay by nice payments apps like google pay. People should be able to make and account in my webstore and I want to send them emails with sale information. I’m sealing offline in my own store so this application should have own warehouse system to count how many items are left for sale total in offline and online as well." """
    end_prompt = """Answear in short statement."""

    max_iter = 3
    iter = 1
    project_overwiew = {}
    chat_history = []
    for bolt in project_template:
        if iter > max_iter:
            break
        prompt = pre_prompt+' '+ prompt_from_client+' '+end_prompt
        content = project_template[bolt]+' '+' End statement the ' + bolt + ' is: '
        project_overwiew[bolt] = llama_api_call(128, prompt, content, chat_history)
        chat_history.append(["user", content])
        chat_history.append(["assistant", project_overwiew[bolt]])
        iter += 1


if __name__ == '__main__':
    odpytanie_llamy()
