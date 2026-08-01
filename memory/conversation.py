import json
from pathlib import Path

histroy=Path("memory/conversation.json")

def load_history():
    if not histroy.exists():
         histroy.parent.mkdir(parents=True, exist_ok=True)
         histroy.write_text([],encoding="utf-8")
         with open (histroy,"r",encoding="utf-8") as file:
         return json.load(file)

def save_history(history):
    with open(histroy,"w",encoding="utf-8") as file:
    return json.dump(histroy,file,indent=4)


def add_msg(role,content):
    history=load_history()
    history.append({
        "role":role,
        "content":content
    })

    save_history(histroy)

def get_hstry():
    return load_history()

def clear_hstry():
    return histroy.clear()