import os
from os.path import join, dirname
from dotenv import load_dotenv

#Solve settings / keys

def solve_env_field( env_field: str ) -> any:
    dotenv_path = join(dirname(__file__), '../.env')
    load_dotenv(dotenv_path)
 
    return os.getenv( env_field )
