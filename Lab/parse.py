from my_lang_lex import lex
from my_lang_lex import tableOfSymb  # , tableOfVar, tableOfConst

lex()
print('-' * 30)
print('tableOfSymb:{0}'.format(tableOfSymb))
print('-' * 30)
tableOfIdent = {}

# номер рядка таблиці розбору/лексем/символів ПРОГРАМИ tableOfSymb
numRow = 1

# довжина таблиці символів програми
# він же - номер останнього запису
len_tableOfSymb = len(tableOfSymb)
print(('len_tableOfSymb', len_tableOfSymb))

costyl = 1
# Функція для розбору за правилом
# Program = program StatementList end
# читає таблицю розбору tableOfSymb

def parseProgram():
    try:
        numTabs = 0
        # перевірити наявність ключового слова 'program'
        parseToken('keyword', numTabs, 'program')
        if not parseToken('ident', numTabs, type="program"):
            failParse("відсутній ідентифікатор програми", (numRow, 'program'))
        parseToken('punct', numTabs, '{')

        parseDeclarList(numTabs)
        parseToken("eol", numTabs, "\n")
        parseDoSection(numTabs)
        # перевірити синтаксичну коректність списку інструкцій StatementList
        # parseStatementList()

        parseToken('punct', numTabs, '}')

        # повідомити про синтаксичну коректність програми
        print('Parser: Синтаксичний аналіз завершився успішно')
        print(tableOfIdent)
        return True
    except SystemExit as e:
        # Повідомити про факт виявлення помилки
        print('Parser: Аварійне завершення програми з кодом {0}'.format(e))


# Функція перевіряє, чи у поточному рядку таблиці розбору
# зустрілась вказана лексема lexeme з токеном token
# параметр indent - відступ при виведенні у консоль
def parseToken(token, indent, lexeme=None, type=None):
    # доступ до поточного рядка таблиці розбору
    global numRow, tableOfIdent
    # якщо всі записи таблиці розбору прочитані,
    # а парсер ще не знайшов якусь лексему
    if numRow > len_tableOfSymb:
        failParse('неочікуваний кінець програми', (lexeme, token, numRow))

    # прочитати з таблиці розбору
    # номер рядка програми, лексему та її токен
    numLine, lex, tok = getSymb()

    # чи збігаються лексема та токен таблиці розбору з заданими
    if lexeme:
        # тепер поточним буде наступний рядок таблиці розбору
        numRow += 1

        if (lex, tok) == (lexeme, token):
            # вивести у консоль номер рядка програми та лексему і токен

            print(
                "  " * indent + 'parseToken: В рядку {0} токен {1}'.format(numLine, (lexeme, token)))
            return True
        else:
            # згенерувати помилку та інформацію про те, що
            # лексема та токен таблиці розбору (lex,tok) відрізняються від
            # очікуваних (lexeme,token)
            failParse('невідповідність токенів',
                      (numLine, lex, tok, lexeme, token))
            return False
    else:
        if type:
            tableOfIdent[lex] = type
        if (tok) == (token):
            # тепер поточним буде наступний рядок таблиці розбору
            numRow += 1

            if token == "ident":
                try:
                    print(
                        "  " * indent + 'parseToken: В рядку {0} токен {1}'.format(numLine,
                                                                                   (lex, token, tableOfIdent[lex])))
                except KeyError:
                    failParse("недекларований ідентифікатор", (indent, lex))
            else:
                print(
                    "  " * indent + 'parseToken: В рядку {0} токен {1}'.format(numLine, (lex, token)))

            return True
        else:
            return False


# Прочитати з таблиці розбору поточний запис
# Повертає номер рядка програми, лексему та її токен
def getSymb():
    if numRow > len_tableOfSymb:
        failParse('getSymb(): неочікуваний кінець програми', numRow)
    # таблиця розбору реалізована у формі словника (dictionary)
    # tableOfSymb[numRow]={numRow: (numLine, lexeme, token, indexOfVarOrConst)
    numLine, lexeme, token, _ = tableOfSymb[numRow]
    return numLine, lexeme, token


# Обробити помилки
# вивести поточну інформацію та діагностичне повідомлення

def failParse(str, tuple):
    if str == 'невідповідність токенів':
        (numLine, lexeme, token, lex, tok) = tuple
        print('Parser ERROR: \n   В рядку {0} неочікуваний елемент ({1},{2}). \n   Очікувався - ({3},{4}).'.format(
            numLine, lexeme, token, lex, tok))
        exit(1)
    elif str == 'неочікуваний кінець програми':
        (lexeme, token, numRow) = tuple
        print(
            'Parser ERROR: \n   Неочікуваний кінець програми - в таблиці символів (розбору) немає запису з номером {1}. \n   Очікувалось - {0}'.format(
                (lexeme, token), numRow))
        exit(2)
    elif str == 'getSymb(): неочікуваний кінець програми':
        numRow = tuple
        print(
            'Parser ERROR: \n   Неочікуваний кінець програми - в таблиці символів (розбору) немає запису з номером {0}. \n   Останній запис - {1}'.format(
                numRow, tableOfSymb[numRow - 1]))
        exit(3)
    elif str == 'помилка зчитування ідентифікаторів':
        (numLine) = tuple
        print(
            f"Parser Error: \n   В рядку {numLine} очікувався список ідентифікаторів")
        exit(4)
    elif str == 'неочікувані дані':
        (numLine, location) = tuple
        print(
            f"Parser Error: \n  В рядку {numLine} очікувався {location}")
        exit(5)
    elif str == 'недекларований ідентифікатор':
        (numLine, identificator_name) = tuple
        print(
            f"Parser Error: \n  В рядку {numLine} недекларована змінна {identificator_name}")
        exit(6)
    elif str == 'неправильний boolexpr':
        (numLine, identificator_name) = tuple
        print(
            f"Parser Error: \n  В рядку {numLine} очікувався {identificator_name}")
        exit(7)
    elif str == 'неочікуваний boolexpr':
        (numLine, identificator_name) = tuple
        print(
            f"Parser Error: \n  В рядку {numLine} очікувався {identificator_name}")
        exit(8)
    elif str == 'відсутній ідентифікатор програми':
        (numLine, identificator_name) = tuple
        print(
            f"Parser Error: \n  В рядку {numLine} очікувався ідентифікатор типу {identificator_name}")
        exit(9)


def parseDeclarList(indent):
    global numRow
    indent += 1
    print("  " * indent + "parseDeclarList():")
    while parseDeclar(indent):
        pass
    return True


def parseDeclar(indent):
    indent += 1
    numLine, lex, tok = getSymb()

    if lex in ('int', 'float', 'bool') and tok == "keyword":
        print("  " * indent + "parseDeclar():")
        parseType(indent, numLine, lex, tok)
        parseToken("punct", indent + 2, ";")
        parseToken("eol", indent, "\n")

        return True
    else:
        return False


def parseType(indent, numLine, lex, tok):
    global numRow
    numRow += 1
    indent += 1
    print("  " * indent + "parseType(): " +
          'в рядку {0} - {1}'.format(numLine, (lex, tok)))
    if not parseIdentList(indent, lex):
        failParse('неочікуваний ввід', (numLine, "Declaration"))
    return True


def parseIdentList(indent, type=None):
    indent += 1
    print("  " * indent + "parseIdentList():")
    if not parseToken('ident', indent + 1, type=type):
        return False

    numLine, lex, tok = getSymb()
    while tok == "punct" and lex == ",":
        parseToken('punct', indent + 1, ',')
        parseToken('ident', indent + 1, type=type)
        numLine, lex, tok = getSymb()
    return True


def parseDoSection(indent):
    indent += 1
    print("  " * indent + "parseDoSection():")
    parseStatementList(indent)
    return True


def parseStatementList(indent):
    indent += 1
    print("  " * indent + "parseStatementList():")
    while parseStatement(indent):
        parseToken("eol", indent, "\n")

    return True


def parseStatement(indent):
    indent += 1
    print("  " * indent + "parseStatement():")
    numLine, lex, tok = getSymb()

    # перевірка

    indent += 1
    if tok == 'ident':
        parseAssign(indent)
        return True
    elif (lex, tok) == ('input', 'keyword'):
        parseInput(indent)
        return True
    elif (lex, tok) == ('output', 'keyword'):
        parseOutput(indent)
        return True
    elif (lex, tok) == ('if', 'keyword'):
        parseIf(indent)
        return True
    elif (lex, tok) == ('while', 'keyword'):
        parseWhile(indent)
        return True
    return False


def parseIf(indent):
    indent += 1
    print("  " * indent + "parseIf():")
    if parseToken("keyword", indent, "if"):
        parseToken('brackets_op', indent, '(')
        parseBoolExpression(indent + 2)
        parseToken('brackets_op', indent, ')')
        parseToken('brackets_op', indent, '{')
        parseToken("eol", indent, "\n")
        parseDoSection(indent)
        parseToken('brackets_op', indent, '}')
        return True
    else:
        return False

def parseElif(indent):
    indent += 1
    print("  " * indent + "parseElif():")
    if parseToken("keyword", indent, "elif"):
        parseToken('brackets_op', indent, '(')
        parseBoolExpression(indent + 2)
        parseToken('brackets_op', indent, ')')
        parseToken('brackets_op', indent, '{')
        parseToken("eol", indent, "\n")
        parseDoSection(indent)
        parseToken('brackets_op', indent, '}')
        return True
    else:
        return False


def parseWhile(indent):
    indent += 1
    print("  " * indent + "parseWhile():")
    if parseToken("keyword", indent, "while"):
        parseToken('brackets_op', indent, '(')
        parseBoolExpression(indent + 2)
        parseToken('brackets_op', indent, ')')
        parseToken('brackets_op', indent, '{')
        parseToken("eol", indent, "\n")
        parseDoSection(indent)
        parseToken('brackets_op', indent, '}')

        parseDoSection(indent)
        return True
    else:
        return False


def parseInput(indent):
    indent += 1
    numLine = getSymb()
    print("  " * indent + "parseInput():")
    indent += 1
    parseToken("keyword", indent, "input")
    parseToken("brackets_op", indent, "(")
    if not parseIdentList(indent):
        failParse('неочікуваний ввід', (numLine, "input"))
    parseToken("brackets_op", indent, ")")
    parseToken("punct", indent, ";")
    return True


def parseOutput(indent):
    indent += 1
    numLine = getSymb()
    print("  " * indent + "parseOutput():")
    parseToken("keyword", indent, "output")
    parseToken("brackets_op", indent, "(")
    if not parseIdentList(indent):
        failParse('неочікуваний ввід', (numLine, "output"))
    parseToken("brackets_op", indent, ")")
    parseToken("punct", indent, ";")
    return True


def parseAssign(indent):
    print("  " * indent + "parseAssign():")
    indent += 1
    parseToken('ident', indent)
    if parseToken('assign_op', indent, '='):
        parseExpression(indent)
        parseToken("punct", indent + 2, ";")
        return True
    else:
        # error
        numLine = getSymb()
        failParse('неочікувані дані', (numLine, "assign statement"))


def parseExpression(indent):
    global numRow
    print("  " * indent + "parseExpression():")
    indent += 1
    count = numRow
    if parseBoolExpression(indent):
        return True
    numRow = count
    if parseArithmExpression(indent):
        return True
    else:
        # error
        numLine = getSymb()
        failParse('неочікувані дані', (numLine, "assign statement"))


def parseBoolExpression(indent):
    global tableOfIdent
    print("  " * indent + "parseBoolExpression():")
    numLine, lex, tok = getSymb()
    indent += 1
    if parseToken("boolconst", indent) or tableOfIdent.get(lex, False) == "bool":
        if tableOfIdent.get(lex, False) == "bool":
            parseToken("ident", indent)
        numLine, lex, tok = getSymb()
        if parseToken("rel_op", indent):
            numLine, lex, tok = getSymb()
            if tok == "boolconst":
                parseToken("boolconst", indent)
            elif tableOfIdent.get(lex, False) == "bool":
                parseToken("ident", indent)
            elif lex == '(':
                parseExpression(indent)
            else:
                failParse("неправильний boolexpr",
                          (numLine, "boolconst або ident(bool)"))
            return True
        elif lex == ")" or lex == ";":
            return True
        else:
            failParse("неправильний boolexpr", (numLine, "rel_op"))
    elif parseArithmExpression(indent):
        if parseToken("rel_op", indent):
            numLine, lex, tok = getSymb()
            if tok in ("intnum", "floatnum") or tableOfIdent.get(lex, False) in ("int", "float"):
                if tableOfIdent.get(lex, False) in ("intnum", "floatnum"):
                    parseToken("ident", indent)
                return parseArithmExpression(indent)
            elif lex == '(':
                parseArithmExpression(indent)
                return True
            else:
                failParse('неочікуваний boolexpr',
                          (numLine, "intnum, floatnum, ident(int, float)"))
        else:
            return True
    else:
        # error
        numLine = getSymb()
        failParse('неочікувані дані', (numLine, "assign statement"))


def parseArithmExpression(indent):
    print("  " * indent + "parseArithmExpression():")
    indent += 1
    parseToken("add_op", indent)

    if not parseTerm(indent):
        return False

    while parseToken("add_op", indent) and parseTerm(indent):
        pass
    return True


def parseTerm(indent):
    print("  " * indent + "parseTerm():")
    indent += 1
    if not parseChunk(indent):
        return False

    while parseToken("mult_op", indent) and parseChunk(indent):
        pass
    return True


def parseChunk(indent):
    print("  " * indent + "parseChunk():")
    indent += 1
    if not parseFactor(indent):
        return False

    while parseToken("power_op", indent) and parseFactor(indent):
        pass
    return True


def parseFactor(indent):
    global tableOfIdent
    global numRow
    print("  " * indent + "parseFactor():")
    indent += 1
    numLine, lex, tok = getSymb()
    if tok in ("intnum", "floatnum", "expnum", "boolconst", "ident"):
        numRow -= 1
        _numLine, _lex, _tok = getSymb()
        if _tok in ("mult_op", "power_op", "add_op"):
            numRow += 1
            _numLine, _lex, _tok = getSymb()
            if _tok == "boolconst" or tableOfIdent.get(_lex, False) == "bool":
                failParse('неочікуваний boolexpr',
                          (numLine, "intnum, floatnum, ident(int, float)"))
            else:
                numRow -= 1
        numRow += 2
        if tok == "ident":
            try:
                print(
                    "  " * indent + 'parseToken: В рядку {0} токен {1}'.format(numLine, (lex, tok, tableOfIdent[lex])))
            except KeyError:
                failParse("недекларований ідентифікатор", (indent, lex))
        else:
            print(
                "  " * indent + 'parseToken: В рядку {0} токен {1}'.format(numLine, (lex, tok)))

    elif lex == "(":
        numRow += 1
        print(
            "  " * indent + 'В рядку {0} токен {1}'.format(numLine, (lex, tok)))
        parseExpression(indent)
        parseToken("brackets_op", indent, ")")

        while parseToken("rel_op", indent):
            numLine, lex, tok = getSymb()
            if lex == "!":
                parseToken("rel_op", indent, "!")
            parseExpression(indent)
    elif lex == "!":
        numRow += 1
        print(
            "  " * indent + 'В рядку {0} токен {1}'.format(numLine, (lex, tok)))
        parseExpression(indent)
    else:
        # error
        numLine = getSymb()
        failParse('неочікувані дані', (numLine, "assign statement"))
    return True


parseProgram()
