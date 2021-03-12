def colour_print(result):
    for key, val in result.items():
        if val:
            print("\033[36m {}:{}\033[0m".format(key, val))
        else:
            print("\033[31m {}:{}\033[0m".format(key, val))
