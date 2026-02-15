from InquirerPy import prompts

questions = [
    {"type": "input", "name": "title", "message": "Enter your project title:"},
    {"type": "input", "name": "description", "message": "Describe your project:"},
    {"type": "input", "name": "installation", "message": "Enter Installation instructions:"},
    {"type": "input", "name": "useage", "message": "Enter useage information:"},
    {"type": "input", "name": "author", "message": "Authors name:"},
    {"type": "input", "name": "contact", "message": "Contact information:"},
   
]
answers = prompt(questions)