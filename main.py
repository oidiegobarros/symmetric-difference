def symmetric_difference(args):
    should_be = set()
    for arg in args:
        for i in arg:
            just_pass = True
            if i in should_be and i in arg:
                should_be.remove(i)
                just_pass = False
            if just_pass and i not in should_be and i in arg:
                should_be.add(i)
    return sorted(should_be)



