import random
import configparser
INI_DICTIONARIES = configparser.ConfigParser()
INI_DICTIONARIES.read("dictionaries.ini", encoding="utf-8")
INI_DICTIONARIES = INI_DICTIONARIES._sections


# Загрузка словарей из файлов
DICTIONARIES = {}
for d in INI_DICTIONARIES: 
  with open(f"dicts\\{INI_DICTIONARIES[d]['file']}", "r", encoding="utf-8") as file: # логгер + обработка ошибок
    process_dict = file.readlines()
  process_dict = [w.strip("\n") for w in process_dict]
  DICTIONARIES[d] = process_dict


class PoleGame():
  word: str
  wordSet: set
  guessedLetters: set
  end: bool
  theme: str

  def __init__(self, dict_name: str):
    if dict_name not in DICTIONARIES:
      pass # логгер + обработка ошибок
    self.word = random.choice(DICTIONARIES[dict_name])
    self.wordSet = set(self.word)
    self.guessedLetters = set()
    self.end = False
    self.theme = INI_DICTIONARIES[dict_name]["visible_name"]

  def check_letter(self, letter: str) -> tuple[bool, bool]:
    is_in_word = False
    is_new = False
    if letter in self.word:
      is_in_word = True
      if letter in self.guessedLetters:
        is_new = True
      self.guessedLetters.add(letter)
      if len(self.wordSet) == len(self.guessedLetters):
        self.end = True
    return is_in_word, is_new

  
  def check_word(self, word: str) -> bool:
    if str.lower(word)==str.lower(self.word):
      self.end = True
      self.guessedLetters = [c for c in self.word]
      return True
    else:
      return False
    
  def print_word(self) -> str:
    return "".join(c if (c in self.guessedLetters or c==" ") else "■" for c in self.word)