import re
from global_graph import Fact


def add_rule_to_global_graph(line):
    before, after = line.split('=>')
    pattern = re.compile('[A-Z]')
    list_fact_before = pattern.findall(before)
    list_fact_after = pattern.findall(after)

    for fact in list_fact_before:
        if fact not in Fact.dict_facts:
            obj_fact = Fact(fact)
        else:
            obj_fact = Fact.dict_facts[fact]
        obj_fact.append_rule(before, list_fact_after)
    for fact in list_fact_after:
        if fact not in Fact.dict_facts:
            Fact(fact)


def cycle_facts():
    for fact in Fact.dict_facts:
        obj_fact = Fact.dict_facts[fact]
        try:
            obj_fact.process_rules()
        except RecursionError:
            continue


def save_init_facts(line):
    pattern = re.compile('[A-Z]')
    list_init_facts = pattern.findall(line)
    for fact in list_init_facts:
        if fact not in Fact.dict_facts:
            obj_fact = Fact(fact)
        else:
            obj_fact = Fact.dict_facts[fact]
        obj_fact.status = True
        try:
            obj_fact.process_rules()
        except RecursionError:
            continue


def save_queries(line):
    pattern = re.compile('[A-Z]')
    list_queries = pattern.findall(line)
    dict_queries = {}
    for query in list_queries:
        if query not in Fact.dict_facts:
            obj_fact = Fact(query)
        else:
            obj_fact = Fact.dict_facts[query]
        dict_queries[query] = obj_fact.status
    return dict_queries


def is_contradiction(init_facts):
    Fact.check_contradiction = True
    if init_facts.strip() == '=':
        cycle_facts()
    save_init_facts(init_facts)


def expert_system(list_rules, init_facts, query):
    for rule in list_rules:
        add_rule_to_global_graph(rule)
    cycle_facts()
    save_init_facts(init_facts)
    dict_queries = save_queries(query)
    if is_contradiction(init_facts):
        pass
    return dict_queries
