import os
import subprocess
from jinja2 import Environment, FileSystemLoader
import argparse

#loading variables
def load_variables(properties_file):
    variables = {}
    with open(properties_file, 'r') as file:
        for line in file:
            if line.strip():
                key,value = line.strip().split(':', 1)
                variables[key.strip()] = value.strip()
    return variables

#render template with variables
def render_template(template, variables,target_dir, output_folder, filename):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template)
    output = template.render(variables)

    #output repo to store

    path = os.path.join(target_dir,output_folder, filename)
    with open(path, 'w') as f:
        f.write(output)

    print(f'Your pipeline code is saved in {path}')

#cloining repo
def clone_repo(source_repo_path, target_dir):
    try:
        subprocess.run(['git', 'clone', source_repo_path, target_dir], check=True)
        print(f'Repo cloned from {source_repo_path} to {target_dir}')
    except subprocess.CalledProcessError as e:
        print(f'Error clonning repo: {e}')


