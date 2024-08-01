import os
import subprocess
from jinja2 import Environment, FileSystemLoader
import argparse

def load_variables(properties_file):
    variables = {}
    with open(properties_file, 'r') as file:
        for line in file:
            if line.strip():
                key, value = line.strip().split(':', 1)
                variables[key.strip()] = value.strip()
    return variables

def render_template(template, variables, target_dir, output_folder, filename):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template)
    output = template.render(variables)

    path = os.path.join(target_dir, output_folder, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(output)

    print(f'Your pipeline code is saved in {path}')

def clone_repo(source_repo_path, target_dir):
    try:
        subprocess.run(['git', 'clone', source_repo_path, target_dir], check=True)
        print(f'Repo cloned from {source_repo_path} to {target_dir}')
    except subprocess.CalledProcessError as e:
        print(f'Error cloning repo: {e}')

def main():
    home_directory = os.path.expanduser("~")
    source_repo_path = os.path.join(home_directory, 'testsourcerep')
    output_path = os.path.join(home_directory, 'testingoutput_directory')

    os.makedirs(output_path, exist_ok=True)
    clone_repo(source_repo_path, output_path)

    parser = argparse.ArgumentParser(
        prog="render",
        description="Renders template with properties files."
    )

    parser.add_argument(
        '-f',
        '--file',
        type=str,
        help='Properties file for your environment.',
        required=True
    )

    parser.add_argument(
        '-g',
        '--group',
        help='Framework to run pipeline (ingestion, EMR, redshift).',
        required=True
    )

    args = parser.parse_args()

    output_folder = args.group
    variables = load_variables(args.file)
    filename = os.path.basename(args.file)  # Using the file's basename for output filename
    render_template('template.j2', variables, output_path, output_folder, filename)

if __name__ == '__main__':
    main()
