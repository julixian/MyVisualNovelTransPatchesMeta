from pathlib import Path
import subprocess


kScriptRoot = Path(__file__).resolve().parent


if __name__ == "__main__":
    subprocess.run(["git", "add", "."], cwd=kScriptRoot)
    subprocess.run(["git", "commit", "-m", "update"], cwd=kScriptRoot)
    subprocess.run(["git", "push", "origin", "main"], cwd=kScriptRoot)
    input("按回车键退出...")
