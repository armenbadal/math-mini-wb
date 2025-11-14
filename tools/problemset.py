from dataclasses import dataclass
import json

@dataclass
class Problem:
    text: str
    answer: str
    language: str
    grade: int

class ProblemSet:
    def __init__(self):
        self.problems = []

    def read(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as fin:
            data = json.load(fin)
        self.problems = [Problem(**p) for p in data]

    def write(self, file_name):
        pass

    def add(self, problem):
        # TODO: ստուգել գոյությունը
        self.problems.append(problem)

    def select(self, query):
        count = query['count']
        print(count)
        for lang, quant in query['group']:
            print(lang, quant)
        return self

        

if __name__ == '__main__':
    pass
