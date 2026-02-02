import fileinput
import shutil
from pathlib import Path
import re

import subprocess
import sys
import os
from textswap.utils.config import ConfigReader
from bs4 import BeautifulSoup


def get_index_htmls(base_path: str = None, filename: str = "index.html"):
    search_path = Path(base_path) / "simple/"
    # rekursiv nach exaktem Dateinamen suchen
    for p in search_path.rglob(filename):
        if p.is_file():
            #print(f"Datei: {p}")
            write_index_htmls_to_file(p, base_path)


# Beispielaufruf:
# find_and_open("/pfad/zum/ordner", "config.toml")
def write_index_htmls_to_file(index_file, base_path: str, log_file: str = "./index.log") -> None:
    """Schreibt alle index.html Inhalte in eine Ausgabedatei."""
    if not index_file:
        print("Keine index.html gefunden")
        return
    content = index_file.read_text(encoding="utf-8")

    soup = BeautifulSoup(content, 'html.parser')
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    pattern = re.escape("../../")

    links = [re.sub(pattern, base_path, url) for url in links]


    clean_links = []
    file_miss = "/mnt/python/data/index_miss.log"
    for url in links:
        i = url.find("#")
        clean_links.append(url if i == -1 else url[:i])
    for url in clean_links:

       if not file_exists(url) and url.startswith("/"):
            with open("/mnt/python/data/links.log", "a") as f:
                f.write(f"{url}\n")
                print(url)

def file_exists(path_str: str) -> bool:
    """Prüft, ob Datei existiert. True für Datei/Verzeichnis."""
    return Path(path_str).exists()