import os
from pathlib import Path
import logging

#creating logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') 

#creating Project 
project_name="cnnClassifier"

#creating list of Files
list_of_files=[
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",

    "confi/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
#creating directory
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory; {filedir} for the file {filename}")
#creating files
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file {filepath}")
    else:
        logging.info(f"{filename} already exists")
