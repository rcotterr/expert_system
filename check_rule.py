from parse_file import is_rule

file = 'rules.txt'
with open(file, 'r') as f:
    content = f.readlines()
    for line in content:
        print(line)
        if is_rule(line):
            print('True')
        else:
            print('False')


c = eval("False and True is not True")
print('c - ', c)
