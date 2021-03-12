import re


class Fact:
    dict_facts = {}
    check_contradiction = False

    def __init__(self, name):
        self.name = name
        self.status = False
        self.dict_facts[self.name] = self
        self.rules = []

    def append_rule(self, before, list_facts_after):
        self.rules.append([before, list_facts_after])

    def info(self):
        print("Info about fact ", self.name)
        print(" status - ", self.status)
        print(" rules: ")
        print(self.rules)

    def _check_rule(self, rule):
        list_rule = list(rule)
        list_ops = []
        pattern_fact = r'[A-Z]'
        for item in list_rule:
            if re.match(pattern_fact, item):
                obj_fact = self.dict_facts[item]
                list_ops.append(str(bool(obj_fact.status)))
            elif item == '+':
                list_ops.append('and')
            elif item == '|':
                list_ops.append('or')
            elif item == '^':
                list_ops.append('is not')
            elif item == '(' or item == ')':
                list_ops.append(item)
            elif item == '!':
                list_ops.append('not')
        str_ops = ' '.join(list_ops)
        try:
            eval(str_ops)
        except SyntaxError:
            print('Syntax error in rule <{}>'.format(rule))
            exit()
        if eval(str_ops):
            return True
        return False

    def process_rules(self):
        for item in self.rules:
            rule, list_change = item
            status_fact = self._check_rule(rule)
            for fact in list_change:
                obj_fact = self.dict_facts[fact]
                if Fact.check_contradiction and obj_fact.status != status_fact:
                    print('There is a contradiction!')
                    exit()
                obj_fact.status = status_fact
                obj_fact.process_rules()
