#!/usr/bin/env python
"""mapper2.py"""
import sys
import re


class Mapper:
    def __init__(self):
        self.H = dict()

    def map(self, doc):
        for line in doc:
            if line[0] == '#':
                continue  # ignorar linhas comentadas
            words = re.findall(r'[0-9]+', line)  # apenas numeros dos nodos
            for word in words:
                self.H[word] = (self.H[word] + 1) if word in self.H else 1

    def emit(self, item):
        print(item[0], item[1], sep='\t')  # emitir um resultado

    def close(self):
        for item in self.H.items():  # emitir todos resultados
            self.emit(item)


if __name__ == "__main__":
    mapper = Mapper()  # iniciar mapper
    mapper.map(sys.stdin)  # aplicar mapping no documento
    mapper.close()  # finalizar mapper e emitir dados
