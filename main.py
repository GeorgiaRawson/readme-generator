from InquirerPy import prompt
import questions

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