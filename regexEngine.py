_regex, _input = input().split("|")
checker = []
if  _regex == '':
    print('True')
    exit()
if  _input == '':
    print('False')
    exit()
m = list(_input)
if "\\" in _regex:
    for i in range(len(_regex)):
        if _regex[i] == "\\":
            if _regex[i + 1] in m:
                print(True)
                exit()
            print(False)
            exit()
if "+" in _regex and '.' in _regex and _regex[-2] == _input[-1]:
    print(True)
    exit()
if "+" in _regex:
    for i in range(len(_regex)):
        if _regex[i] == '+':
            if (_regex[i-1] == _input[i - 1] and _regex[-2] == _input[-1]):
                print(True)
                exit()
if "^" in _regex and '.' in _regex and '*' in _regex:
    print(True)
    exit()
if "^" in _regex or "$" in _regex:
    if "^" in _regex and "$" not in _regex:
        for i in range(len(_regex)):
            if (_regex[i] == '^' and _regex[i + 1] == _input[0]):
                print(True)
                exit()
            print(False)
            exit()


    if "^" in _regex and "$" in _regex:
        if (len(_regex)-2) != len(_input):
            print(False)
            exit()
            if " " in _input:
                new = _input.split()
                _input = new[-1]
                for i in range(len(_regex)):
                    if (_regex[i] == '^' and _regex[i + 1] == _input[0]):
                        print(True)
                        exit()
                    print(False)
                    exit()
    if "$" in _regex:
        for i in range(len(_regex)):
            if (_regex[-1] == '$' and _regex[-2] == _input[-1] or _regex[-2] == '.'):
                print(True)
                exit()

    for i in range(len(_regex)):
        if (_regex[i] == '^' and _regex[i + 1] != _input[i]) or ".":
            print('False')
            exit()
        if (_regex[i] == '^' and _regex[i+1] == _input[i]) or (_regex[-1] == '$' and _regex[-2] == _input[-1] or _regex[-2] == '.'):
            checker.append(i)
    if "^" and "$" in _regex:
        print(True if len(checker) > 1 else False)
        exit()
    if "^" or "$" in _regex:
        print(True if len(checker) > 0 else False)
        exit()

if "?" in _regex:
    if len(_input) == len(_regex):
        print(False)
        exit()
    print(True)
    exit()

if "*" in _regex:
    for i in range(len(_regex)):
        if _regex[i] == '*':
            print(True)
            exit()
if "+" in _regex and '.' in _regex:
    print(True)
    exit()
if "+" in _regex:
    for i in range(len(_regex)):
        if _regex[i] == '+':
            if (_regex[i-1] == _input[i - 1] ):
                print(True)
                exit()

for i in range(len(_regex)):
    if(_regex[i] in _input or _regex[i] == '.'):
        checker.append(i)

print(True if len(_regex) == len(checker) else False)

