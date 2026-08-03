from pathlib import Path
import json

summary=Path("memory/summary.json")

def load_summary():
    if not summary.exists():
        summary.parent.mkdir(parents=True,exist_ok=True)
        summary.write_text(
            json.dump({"summary:"},file,indent=4,encoding="utf-8")
        )
    with open(summary,"w",encoding="utf-8"):
        return json.load(file)

def save_history():
    with open(summary,"w",encoding="utf=8"):
        return json.dump({"summary:summary"},file,indent=4)

