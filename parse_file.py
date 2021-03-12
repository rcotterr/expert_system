import re


def is_rule(line):
    result = re.match(
        r'^\s*(\(?!?!?|!?!?\(?)\s*[A-Z]\s*((\+|\^|\|)\s*\(?!?!?\s*'
        r'[A-Z]\)?\s*)*=>\s*?[A-Z]\s*(\+\s*?[A-Z]\s*)*$', line)
    if result:
        return True
    return False


def is_init_facts(line):
    result = re.match(r'^\s*=\s*[A-Z]*\s*$', line)
    if result:
        return True
    return False


def is_query(line):
    result = re.match(r'^\s*\?\s*[A-Z]*\s*$', line)
    if result:
        return True
    return False


def parse_file(file):
    list_rules = []
    init_facts = ""
    query = ""
    with open(file, 'r') as f:
        content = f.readlines()
        for ind, line in enumerate(content):
            if line.startswith('#'):
                continue
            if '#' in line:
                index = line.find('#')
                line = line[:index]
            if not line or line.isspace():
                continue
            if is_rule(line):
                list_rules.append(line)
            elif is_init_facts(line) and not init_facts:
                init_facts = line
            elif is_query(line) and not query:
                query = line
            else:
                print("Syntax error in line ", ind + 1)
                exit()
    if list_rules and init_facts and query:
        return list_rules, init_facts, query
    if not list_rules:
        print('No rule')
    if not init_facts:
        print('No fact')
    if not query:
        print('No query')
    exit()
