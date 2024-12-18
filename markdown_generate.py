import os

def generate_markdown(folder_path, output_file="directory_structure.md"):
    """
    Generate a Markdown file that documents the structure of a given directory.

    Parameters:
        folder_path (str): The root folder path to document.
        output_file (str): The Markdown file to write the structure into.
    """
    with open(output_file, "w") as md_file:
        md_file.write(f"# Directory Structure for `{folder_path}`\n\n")
        md_file.write("```\n")
        
        # Walk the directory and write structure
        for root, dirs, files in os.walk(folder_path):
            level = root.replace(folder_path, '').count(os.sep)
            indent = ' ' * 4 * level
            md_file.write(f"{indent}{os.path.basename(root)}/\n")
            sub_indent = ' ' * 4 * (level + 1)
            for f in files:
                md_file.write(f"{sub_indent}{f}\n")
        
        md_file.write("```\n")

    print(f"Markdown file `{output_file}` has been created.")

if __name__ == "__main__":
    # Set the folder to document
    folder_to_document = r"C:/Users/TR/Desktop/GIT/arcgis-SDK-js/backend/data/raw/gistemp.zarr"
    output_markdown_file = "directory_structure.md"
    
    # Generate the Markdown
    generate_markdown(folder_to_document, output_markdown_file)
