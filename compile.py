import os
import re
import subprocess
import argparse

# Function to modify the content of the LaTeX file
def modify_tex_file(content):
    # Replace the \chapter command with the new format and remove any \label
    # Also converts chapter titles to uppercase using \MakeUppercase
    modified_content = re.sub(
        r'\\chapter{(.+?)}',  # Regex to match \chapter{...}
        r'\\begin{center}\n    {\\huge \\textbf{\\MakeUppercase{\1}}}\\\\[1.2cm]\n\\end{center}',  # Replacing with new format
        content
    )
    # Remove any \label commands
    modified_content = re.sub(r'\\label{.*?}', '', modified_content)

    # Insert the modified content into the LaTeX template
    new_content = r'''\documentclass[11pt,a4paper,oneside]{article} 

\input{settings.tex}

\ifcsname showrefs\endcsname
\else
    \NewDocumentCommand{\showrefs}{}{false}
\fi

\begin{document}

%s

\end{document}
''' % modified_content
    return new_content

# Function to compile a .tex file twice using pdflatex
def compile_tex_file(file_path):
    try:
        # First compilation
        subprocess.run(['pdflatex', file_path], check=True)
        # Second compilation to resolve references
        subprocess.run(['pdflatex', file_path], check=True)
        print(f"Compiled {file_path} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error compiling {file_path}: {e}")

# Function to process 'sep-*.tex' files, copying them into root but not compiling yet
def process_and_copy_sep_tex_files(root_project_path):
    copied_files = []  # List to store the copied files for later compilation

    for root, dirs, files in os.walk(root_project_path):
        for file in files:
            # Check if the file name starts with 'ch0' and ends with '.tex'
            if file.startswith('ch0') and file.endswith('.tex'):
                original_path = os.path.join(root, file)

                # Read the content of the original .tex file
                with open(original_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Modify the content of the .tex file
                modified_content = modify_tex_file(content)

                # Define the new file name with the 'sep-' prefix in the root directory
                new_file_name = 'sep-' + file
                new_file_path = os.path.join(root_project_path, new_file_name)

                # Write the modified content to the new file in the root directory
                with open(new_file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)

                # Add the new file path to the list of copied files for later compilation
                copied_files.append(new_file_path)

    # Return the list of copied files to be compiled later
    return copied_files

# Function to remove unnecessary files after compilation
def remove_auxiliary_files(root_project_path):
    extensions_to_remove = ['.aux', '.log', '.out']
    for root, dirs, files in os.walk(root_project_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions_to_remove):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Removed file: {file_path}")
                except OSError as e:
                    print(f"Error removing file {file_path}: {e}")

# Function to remove sep-*.tex files
def remove_sep_tex_files(root_project_path):
    for root, dirs, files in os.walk(root_project_path):
        for file in files:
            if file.startswith('sep-') and file.endswith('.tex'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Removed sep file: {file_path}")
                except OSError as e:
                    print(f"Error removing sep file {file_path}: {e}")

# Main function
def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Compile LaTeX files")
    parser.add_argument('--all', action='store_true', help="Compile 'sep-*.tex' files and 'ti-skripta-3-rocnik.tex'")
    parser.add_argument('--rem', action='store_true', help="Remove auxiliary files (*.aux, *.log, *.out) after compilation")
    parser.add_argument('--remsep', action='store_true', help="Remove sep-*.tex files after compilation")
    args = parser.parse_args()

    # Get the current working directory (root of the project)
    root_project_path = os.getcwd()

    # Compile 'ti-skripta-3-rocnik.tex' (instead of 'ti-tretak.tex')
    ti_skripta_path = os.path.join(root_project_path, 'ti-skripta-3-rocnik.tex')
    if os.path.exists(ti_skripta_path):
        compile_tex_file(ti_skripta_path)
    else:
        print("'ti-skripta-3-rocnik.tex' not found in the project root.")

    # If the '--all' argument is provided, process and copy 'sep-*.tex' files, then compile them all
    if args.all:
        copied_files = process_and_copy_sep_tex_files(root_project_path)  # Copy files
        # Now compile all copied files
        for file_path in copied_files:
            compile_tex_file(file_path)

    # If the '--rem' argument is provided, remove auxiliary files
    if args.rem:
        remove_auxiliary_files(root_project_path)
    
    # If the '--remsep' argument is provided, remove sep-*.tex files
    if args.remsep:
        remove_sep_tex_files(root_project_path)

# Run the main function when the script is executed
if __name__ == '__main__':
    main()
