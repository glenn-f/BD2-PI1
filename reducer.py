#!/usr/bin/env python
"""reducer.py"""
import sys


class Reducer:
    def __init__(self, doc):
        self.current_word = None
        self.current_count = 0
        word = None
        for line in doc:
            line = line.strip()  # remove espaços em branco no início e fim da linha
            line = line.lower()  # transformar em caixa baixa

            word, count = line.split('\t', 1)  # dividir dados
            try:
                count = int(count)  # parse na entrada vinda do mapper
            except ValueError:
                continue  # se count não é um número, ignora a linha
            if self.current_word == word:
                self.current_count += count # atualizar contador
            else:
                if self.current_word:
                    self.emit()  # emitir antes de contar a nova palavra
                self.current_count = count  # atualizar contagem para nova palavra
                self.current_word = word  # atualizar chave para nova palavra

        if self.current_word == word:
            self.emit()  # emitir a última palavra, se necessário!

    def emit(self):
        print(self.current_word, self.current_count, sep='\t')


if __name__ == "__main__":
    Reducer(sys.stdin)  # aplicar reducer na entrada padrao (vinda do mapper)
