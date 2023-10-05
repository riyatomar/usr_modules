import os

scripts=[
    "concepts.py",
    "indexing.py",
    "sem_cat.py",
    "morpho_sem.py",
    "dependency.py",
    "discourse.py",
    "spk_view.py",
    "scope.py",
    "sent_type.py"
]

def run_script(script_name):
    try:
        command=f"python3 {script_name}"
        os.system(command)
    except Exception as e:
        print(f"Error running script: {e}")

for script in scripts:
    run_script(script)
