from parse_file import is_query
from expert_system import save_queries
from colour_print import colour_print


def interactive():
    print('input a query - <?ABC>')
    line = input()
    while line != 'exit':
        if is_query(line):
            dict_queries = save_queries(line)
            colour_print(dict_queries)
        else:
            print('wrong syntax of query')
            print('input <exit> to quit')
        print('input a query - <?ABC>')
        line = input()
