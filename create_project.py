import os
import subprocess
import sys

def create_project_structure(project_name):
    # 1. Create project folder
    # os.makedirs(project_name, exist_ok=True)
    # os.chdir(project_name)
    # print(f"📁 Created project folder: {project_name}")

    # 2. Create virtual environment
    print("⚙️ Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", "venv"])
    print("✅ Virtual environment created")

    # 3. Create main.py
    with open("main.py", "w", encoding="utf-8") as f:
        f.write("""\
def main():
    print("Hello, world!")

if __name__ == "__main__":
    main()
""")
    print("📝 Created main.py")

    # 4. Create requirements.txt
    with open("requirements.txt", "w", encoding="utf-8") as f:
        f.write("# Add your project dependencies here\n")
    print("📄 Created requirements.txt")

    # 5. Create README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(f"# {project_name}\n\nNew Python project.")
    print("📘 Created README.md")

    # 6. Create src/ folder with __init__.py
    os.makedirs("src", exist_ok=True)
    with open(os.path.join("src", "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Init file for src module")
    print("📁 Created src/ folder with __init__.py")

    # 7. Create .gitignore
    with open(".gitignore", "w", encoding="utf-8") as f:
        f.write("""\
# Ignore virtual environment folder
venv/

# Python cache files
__pycache__/
*.py[cod]

# Log files
*.log

# IDE folders
.vscode/
.idea/
""")
    print("🚫 Created .gitignore to ignore venv and other common files")

    print("\n🚀 Project setup complete!")
    
    
    print("\n📌 To activate the virtual environment:")
    print(r"   venv\Scripts\activate")



if __name__ == "__main__":
    project_name = input("Enter your project name: ")
    create_project_structure(project_name)
