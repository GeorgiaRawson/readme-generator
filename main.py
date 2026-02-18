from InquirerPy import prompt

questions = [
    {"type": "input", "name": "title", "message": "Enter your project title:"},
    {"type": "input", "name": "description", "message": "Describe your project:"},
    {"type": "input", "name": "installation", "message": "Enter Installation instructions:"},
    {"type": "input", "name": "useage", "message": "Enter useage information:"},
    {"type": "input", "name": "author", "message": "Authors name:"},
    {"type": "input", "name": "contact", "message": "Contact information:"},
    {"type": "list", "name": "licence", "message": "Select a licence:", "choices": ["Apache License 2,0", "MIT License", "GNU GPL v3", "GNU LGPL v3", "Mozilla Public License 2.0", "Creative Commons" , "Unlicense",], "default": None,}
]
answers = prompt(questions)

content = f"""
           # {answers['title']}
           
           ## Description

           {answers['description']}
            
           ## Installation 

           {answers['installation']} 
   
           ## Useage 
           
           {answers['useage']}
           
           ## Author 
           
           {answers['author']} <{answers ['contact']}>
           
           ## Licence
           
           {answers['licence']}"""

          
with open ("README.md", "w") as readme:
    readme.write(content)

print("README.md has been generated sucessfully!")