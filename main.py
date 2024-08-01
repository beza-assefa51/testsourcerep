import os 
import argparse

def main():
    #change so its not hard coded
    home_directory = os.path.expanduser("~")
    source_repo_path = os.path.join(home_directory, 'testsourcerep')
    output_path = os.path.join(home_directory, 'testingoutput_directory')
    
    os.mkdir(output_path)
    clone_repo(source_repo_path, output_path)

    #change command to render -f file -g group
    parser = argparse.ArgumentParser(
       # prog="render"
        #thodescription="Renders template with properties files."
    )

    parser.add_argument(
        '-f',
        '--file',
        type=str,
        help='Properties files for your environment.',
        required=False
    )