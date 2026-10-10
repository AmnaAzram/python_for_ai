# note -  make save load find

import json
import logging
import re
from datetime import datetime
from pathlib import Path
from time import asctime


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s" )

NOTES_FILE = Path("notes.json")

def load_notes()->list:
    if not NOTES_FILE.exists():
        logging.warning("file not found")
        return []

    with open("notes.json","r",encoding="utf-8") as f:
        return json.load(f)

def save_notes(text:str)->None:
    notes = load_notes()
    note = {"time":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "text":text}
    notes.append(note )
    with open(NOTES_FILE,"w", newline="" , encoding="utf-8") as f:
        json.dump(notes, f, indent=4)
    logging.info(f"Note saved to {NOTES_FILE}")

def search_notes(keyword:str)->list:
    notes = load_notes()
    return [note for note in notes if  re.search(keyword,note["text"],re.IGNORECASE)]




if __name__ == "__main__":
    save_notes("This is my daily routeen noteboke")
    save_notes("This is my personal note book if yu open then please close it")








