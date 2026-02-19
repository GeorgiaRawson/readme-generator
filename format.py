def markdown_content(anwsers):
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

def save_readme (content, filename="README.md"):
          with open ("README.md", "w") as readme:
            readme.write(content)
            