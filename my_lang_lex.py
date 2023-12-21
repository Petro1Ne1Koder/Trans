# Таблиця лексем мови
tableOfLanguageTokens = {'program': 'keyword',
                         'int': 'keyword',
                         'float': 'keyword',
                         'bool': 'keyword',
                         'while': 'keyword',
                         'if': 'keyword',
                         'input': 'keyword',
                         'output': 'keyword',
                         '{': 'brackets_op',
                         '}': 'brackets_op',
                         '=': 'assign_op',
                         '.': 'punct',
                         ',': 'punct',
                         ':': 'punct',
                         ';': 'punct',
                         '\t': 'ws',
                         '\32': 'ws',
                         ' ': 'ws',
                         '\n': 'eol',
                         '\r': 'eol',
                         '\r\n': 'eol',
                         '\n\r': 'eol',
                         '-': 'add_op',
                         '+': 'add_op',
                         '*': 'mult_op',
                         '/': 'mult_op',
                         '^': 'power_op',
                         '(': 'brackets_op',
                         ')': 'brackets_op',
                         '!=': 'rel_op',
                         '>=': 'rel_op',
                         '>': 'rel_op',
                         '==': 'rel_op',
                         '<=': 'rel_op',
                         '<': 'rel_op',
                         'true': 'boolconst',
                         'false': 'boolconst'}
# Решту токенів визначаємо не за лексемою, а за заключним станом
tableIdentFloatInt = {2: 'ident', 4: 'intnum', 7: 'floatnum'}

#  - state-transition_function
stf = {
    (0, 'Letter'): 1, (1, 'Letter'): 1, (1, 'Digit'): 1, (1, 'other'): 2,
    (0, 'Digit'): 3, (3, 'Digit'): 3, (3, 'other'): 4, (3, '.'): 5,
    (5, 'Digit'): 6, (6, 'Digit'): 6,
    (5, 'other'): 102, (6, 'other'): 7,

    (0, 'eol'): 13,
    (0, 'ws'): 0,

    (0, '+'): 14, (0, '-'): 14, (0, '*'): 14, (0, '/'): 14, (0, '^'): 14,
    (0, '('): 14, (0, ')'): 14, (0, '{'): 14, (0, '}'): 14, (0, ';'): 14,
    (0, ','): 14,

    (0, '='): 8, (0, '<'): 8, (0, '>'): 8, (8, 'other'): 9, (8, '='): 11,
    (0, '!'): 10,
    (10, 'other'): 103, (10, '='): 11,

    (0, 'other'): 101,
}

initState = 0  # q0 - стартовий стан
F = {2, 4, 7, 9, 11, 13, 14, 101, 102, 103}  # множина заключних станів
Fstar = {2, 4, 7, 9}  # зірочка
Ferror = {101, 102, 103}  # обробка помилок

tableOfId = {}  # Таблиця ідентифікаторів
tableOfConst = {}  # Таблиць констант
tableOfSymb = {}  # Таблиця символів програми (таблиця розбору)

state = initState  # поточний стан

f = open('test.f', 'r')

sourceCode = f.read()
f.close()

# FSuccess - ознака успішності розбору
FSuccess = (True, 'Lexer')

# номер останнього символа у файлі з кодом програми
lenCode = len(sourceCode) - 1
numLine = 1  # лексичний аналіз починаємо з першого рядка
numChar = -1  # з першого символа (в Python'і нумерація - з 0)
char = ''  # ще не брали жодного символа
lexeme = ''  # ще не починали розпізнавати лексеми


def lex():
    global state, numLine, char, lexeme, numChar, FSuccess
    try:
        while numChar < lenCode:
            char = nextChar()  # прочитати наступний символ
            classCh = classOfChar(char)  # до якого класу належить
            state = nextState(state, classCh)  # обчислити наступний стан
            if (is_final(state)):  # якщо стан заключний
                processing()  # виконати семантичні процедури
            # if state in Ferror:       # якщо це стан обробки помилки
            # break                 #      то припинити подальшу обробку
            elif state == initState:
                lexeme = ''  # якщо стан НЕ заключний, а стартовий - нова лексема
            else:
                lexeme += char  # якщо стан НЕ закл. і не стартовий - додати символ до лексеми
        else:
            char = ' '
            classCh = 'ws'
            state = nextState(state, classCh)
            processing()
        print('Lexer: Лексичний аналіз завершено успішно')

    except SystemExit as e:
        # Встановити ознаку неуспішності
        FSuccess = (False, 'Lexer')
        # Повідомити про факт виявлення помилки
        print(f'Lexer: Аварійне завершення програми з кодом {format(e)}')


def processing():
    global state, lexeme, char, numLine, numChar, tableOfSymb
    if state == 13:  # \n
        print('{0:<3d} {1:<10s} {2:<10s} '.format(
            numLine, lexeme, 'eol', ''))
        tableOfSymb[len(tableOfSymb) + 1] = (numLine, "\n", 'eol', '')
        numLine += 1
        state = initState
    if state in (2, 4, 7, 9):  # keyword, ident, float, int, boolval
        token = getToken(state, lexeme)
        if token != 'keyword':  # не keyword
            index = indexIdConst(state, lexeme)
            print('{0:<3d} {1:<10s} {2:<10s} {3:<2d} '.format(
                numLine, lexeme, token, index))
            tableOfSymb[len(tableOfSymb) + 1] = (numLine, lexeme, token, index)
        else:  # якщо keyword
            # print(numLine,lexeme,token)
            print('{0:<3d} {1:<10s} {2:<10s} '.format(numLine, lexeme, token))
            tableOfSymb[len(tableOfSymb) + 1] = (numLine, lexeme, token, '')
        lexeme = ''
        numChar = putCharBack(numChar)  # зірочка
        state = initState
    if state in (11, 14):  # 8:         # assign_op # in (8,10):
        lexeme += char
        token = getToken(state, lexeme)
        print('{0:<3d} {1:<10s} {2:<10s} '.format(numLine, lexeme, token))
        tableOfSymb[len(tableOfSymb) + 1] = (numLine, lexeme, token, '')
        lexeme = ''
        state = initState
    if state in Ferror:  # (101,102,103,104):  # ERROR
        fail()


def fail():
    global state, numLine, char
    print(numLine)
    if state == 101:
        print('Lexer: у рядку ', numLine,
              ' неочікуваний символ ' + "'" + char + "'")
        exit(101)
    if state == 102:
        my_error = f'Lexer: у рядку {numLine} очікувалось цифра, а не '
        if char in " \t":
            print(my_error + "ws")
        elif char in "\n\r":
            print(my_error + "eol")
        else:
            print(my_error + "'" + char + "'")
        exit(102)
    if state == 103:
        my_error = f"Lexer: у рядку {numLine} очікувався символ '=', а не "
        if char in " \t":
            print(my_error + "ws")
        elif char in "\n\r":
            print(my_error + "eol")
        else:
            print(my_error + "'" + char + "'")
        exit(103)


def is_final(state):
    if (state in F):
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


def classOfChar(char):
    if char in 'abcdefghijklmnopqrstuvwxyz':
        res = "Letter"
    elif char in "0123456789":
        res = "Digit"
    elif char in " \t":
        res = "ws"
    elif char in "\n\r":
        res = "eol"
    elif char in "+-*/^=(){},;<>!.":
        res = char
    else:
        res = 'символ не належить алфавіту'
    return res


def getToken(state, lexeme):
    try:
        return tableOfLanguageTokens[lexeme]
    except KeyError:
        return tableIdentFloatInt[state]


def indexIdConst(state, lexeme):
    indx = 0
    if state == 2:
        indx = tableOfId.get(lexeme)
        #       token=getToken(state,lexeme)
        if indx is None:
            indx = len(tableOfId) + 1
            tableOfId[lexeme] = indx
    if state == 4:
        indx = tableOfConst.get(lexeme)
        if indx is None:
            indx = len(tableOfConst) + 1
            tableOfConst[lexeme] = indx
    if state == 7:
        indx = tableOfConst.get(lexeme)
        if indx is None:
            indx = len(tableOfConst) + 1
            tableOfConst[lexeme] = indx
    return indx


# запуск лексичного аналізатора
lex()

# Таблиці: розбору, ідентифікаторів та констант
print('-' * 50)
print('tableOfSymb:{0}'.format(tableOfSymb))
print('tableOfId:{0}'.format(tableOfId))
print('tableOfConst:{0}'.format(tableOfConst))
