tokenTable = {
    'program': 'keyword',
    'True': 'keyword',
    'False': 'keyword',
    'if': 'keyword',
    'else': 'keyword',
    'while': 'keyword',
    'output': 'keyword',
    'input': 'keyword',
    ':=': 'assign_op',
    '=': 'assign_op',
    '+=': 'assign_op',
    '-=': 'assign_op',
    '*=': 'assign_op',
    '/=': 'assign_op',
    '%=': 'assign_op',
    '^=': 'assign_op',
    '+': 'add_op',
    '-': 'add_op',
    '*': 'mul_op',
    '/': 'mul_op',
    '%': 'mul_op',
    '^': 'pow_op',
    '++': 'post_op',
    '--': 'post_op',
    '==': 'rel_op',
    '!=': 'rel_op',
    '>': 'rel_op',
    '>=': 'rel_op',
    '<': 'rel_op',
    '<=': 'rel_op',
    '(': 'brackets_op',
    ')': 'brackets_op',
    '{': 'punct',
    '}': 'punct',
    '&': 'punct',
    ',': 'punct',
    ';': 'punct',
    '"': 'quotes',
    '//': 'comment',
    '.': 'dot',
    ' ': 'ws',
    '\t': 'ws',
    '\n': 'eol',
    'float': 'keyword',
    'int': 'keyword',
    'bool': 'keyword',
}

tokStateTable = {2: 'ident', 6: 'float', 8: 'int'}

stf = {
    (0, 'Letter'): 1, (1, 'Letter'): 1, (1, 'Digit'): 1, (1, 'other'): 2,
    (0, 'ws'): 0,
    (0, 'Digit'): 3, (3, 'Digit'): 3, (3, 'dot'): 4, (4, 'Digit'): 5, (5, 'Digit'): 5, (5, 'other'): 6,
    (4, 'other'): 104, (3, 'other'): 8,
    (0, '/'): 9, (9, '/'): 10, (9, 'other'): 11, (9, '='): 19, (10, 'NotNewLine'): 10, (10, 'nl'): 50,
    (0, '^'): 12, (0, '>'): 12, (0, '<'): 12, (0, '%'): 12, (0, '*'): 12, (12, 'other'): 13, (12, '='): 19,
    (0, ':'): 14, (14, 'other'): 101, (14, '='): 19,
    (0, '-'): 15, (15, '-'): 16, (15, 'other'): 17, (15, '='): 19,
    (0, '='): 18, (18, 'other'): 20, (18, '='): 19,
    (0, '+'): 21, (21, 'other'): 23, (21, '+'): 22, (21, '='): 19,
    (0, '!'): 24, (24, 'other'): 102, (24, '='): 25,
    (0, 'other'): 103,
    (0, ';'): 26, (0, ','): 26, (0, '('): 26, (0, ')'): 26, (0, '{'): 26, (0, '}'): 26, (0, '&'): 26,
    (0, 'nl'): 27,
}

initState = 0
F = {2, 6, 8, 11, 13, 19, 20, 22, 23, 25, 26, 27, 16, 17, 101, 102, 103, 104, 50}
Fstar = {2, 6, 8, 13, 17, 20, 23, 50}
Ferror = {101, 102, 103, 104}

tableOfId = {}
tableOfConst = {}
tableOfSymb = {}

state = initState

f = open('test.f', 'r')
sourceCode = f.read()
sourceCode += '\n'
f.close()

FSuccess = (True, 'Lexer')

lenCode = len(sourceCode) - 1
numLine = 1
numChar = -1
char = ''
lexeme = ''


def lex():
    global state, numLine, char, lexeme, numChar, FSuccess
    try:
        while numChar < lenCode:
            char = nextChar()
            classCh = classOfChar(char, state)
            state = nextState(state, classCh)
            if is_final(state):
                processing()
            elif state == initState:
                lexeme = ''
            else:
                lexeme += char
        print('\033[32mLexer: Лексичний аналіз завершено успішно\033[0m')
    except SystemExit as e:
        FSuccess = (False, 'Lexer')
        print(f'\033[31mLexer: Аварійне завершення програми з кодом {e}\033[0m')


def processing():
    global state, lexeme, char, numLine, numChar, tableOfSymb
    if state == 27:  # \n
        numLine += 1
        state = initState
    if state in (2, 6, 8):
        token = getToken(state, lexeme)
        if token != 'keyword':
            index = indexIdConst(state, lexeme)
            print(f'{numLine:<3d} {lexeme:<10s} {token:<10s} {index:<2d}')
            tableOfSymb[len(tableOfSymb) + 1] = (numLine, lexeme, token, index)
        else:
            print(f'{numLine:<3d} {lexeme:<10s} {token:<10s}')
            tableOfSymb[len(tableOfSymb) + 1] = (numLine, lexeme, token, '')
        lexeme = ''
        numChar = putCharBack(numChar)
        state = initState
    if state in (11, 13, 17, 20, 23):
        token = getToken(state, lexeme)
        print(f'{numLine:<3d} {lexeme:<10s} {token:<10s}')
        numChar = putCharBack(numChar)
        tableOfSymb[len(tableOfSymb) + 1] = (numLine, lexeme, token, '')
        lexeme = ''
        state = initState
    if state in (19, 16, 22, 25, 26):
        lexeme += char
        token = getToken(state, lexeme)
        print(f'{numLine:<3d} {lexeme:<10s} {token:<10s}')
        tableOfSymb[len(tableOfSymb) + 1] = (numLine, lexeme, token, '')
        lexeme = ''
        state = initState
    if state == 50:
        numChar = putCharBack(numChar)
        token = 'comment'
        lexeme = '//'
        print(f'{numLine:<3d} {lexeme:10s} {token:10s}')
        tableOfSymb[len(tableOfSymb) + 1] = (numLine, '//', 'comment', '')
        lexeme = ''
        state = initState
    if state in Ferror:
        fail()


def fail():
    global state, numLine, char
    if state == 101:
        print(f'\033[31mLexer: у рядку {numLine}, очікувався символ = після ":", а не {char}\033[0m')
        exit(101)
    if state == 102:
        print(f'\033[31mLexer: у рядку {numLine}, очікувався символ = після "!", а не {char}\033[0m')
        exit(102)
    if state == 103:
        print(f'\033[31mLexer: у рядку {numLine} невідомий символ {char}\033[0m')
        exit(103)
    if state == 104:
        print(f'\033[31mLexer: у рядку {numLine} очікувався Digit після крапки\033[0m')
        exit(104)


def is_final(state):
    if state in F:
        return True
    else:
        return False


def nextState(state, classCh):
    try:
        return stf[(state, classCh)]
    except KeyError:
        return stf[(state, 'other')]


def nextChar():
    global numChar
    numChar += 1
    return sourceCode[numChar]


def putCharBack(numChar):
    return numChar - 1


def classOfChar(char, state):
    if state == 10:
        if char not in '\n':
            return 'NotNewLine'
        else:
            return 'nl'
    if char in '.':
        res = 'dot'
    elif char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_':
        res = 'Letter'
    elif char in '0123456789':
        res = 'Digit'
    elif char in ' \t':
        res = 'ws'
    elif char in '\n':
        res = 'nl'
    elif char in '+-:=*/()><!^}{%,;&"':
        res = char
    else:
        res = 'символ не належить алфавіту'
    return res


def getToken(state, lexeme):
    try:
        return tokenTable[lexeme]
    except KeyError:
        return tokStateTable[state]


def indexIdConst(state, lexeme):
    indx = 0
    if state == 2:
        indx = tableOfId.get(lexeme)
        if indx is None:
            indx = len(tableOfId) + 1
            tableOfId[lexeme] = indx
    if state in (6, 8):
        indx = tableOfConst.get(lexeme)
        if indx is None:
            indx = len(tableOfConst) + 1
            tableOfConst[indx] = (tokStateTable[state], lexeme)
    return indx


lex()
print('-' * 50)

print(f'tableOfSymb: {tableOfSymb}\n')
print(f'tableOfId: {tableOfId}\n')
print(f'tableOfConst: {tableOfConst}\n')


