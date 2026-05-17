import numpy as np
import pandas as pd
import queue
from typing import List, Dict
from Bio import SeqIO
from pathlib import Path


# функция чтения ДНК-файла
def read_dnk_file(file_path: str) -> str:
  with open(file_path, 'r') as f:
    # Загрузить всё в словарь
    records = SeqIO.to_dict(SeqIO.parse(f, "fasta"))
    return records


# функция чтения и загрузки ДНК-файлов
def make_dnk_bank(dir_path: str) -> List:
  folder = Path(dir_path)
  dnks = []

  if not folder.is_dir():
    print(f"Папка {folder} не найдена")
  else:
    fna_files = list(folder.glob('*.fna'))
    print(f"Найдено {len(fna_files)} .fna файлов")

    for f in fna_files:
      record = read_dnk_file(f)
      dnks.append(record)

  return dnks

# НОП
def nop(str1: str, str2: str) -> int:
  pass
#
def make_table(dnks: dict) -> List[List[int]]:
  pass



if __name__=='__main__':
    pass
