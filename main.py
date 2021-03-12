import argparse
from parse_file import parse_file
from expert_system import expert_system
from colour_print import colour_print
from interactive import interactive


def main():
    parser = argparse.ArgumentParser(description='Arguments for expert system')
    parser.add_argument('file', action='store',
                        help='File in .txt')
    parser.add_argument("-i", action="store",
                        help='Interactive queries')
    args = parser.parse_args()
    try:
        list_rules, init_facts, query = parse_file(args.file)
        result = expert_system(list_rules, init_facts, query)
        colour_print(result)
        if args.i:
            interactive()
    except Exception as e:
        print('Expert System exception ', e)
        exit()


if __name__ == "__main__":
    main()
