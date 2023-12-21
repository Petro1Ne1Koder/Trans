from Lab.my_lang_lex import lex, tableOfSymb  # , tableOfVar, tableOfConst

lex()
print('-' * 30)
print('tableOfSymb:{0}'.format(tableOfSymb))
print('-' * 30)



# номер рядка таблиці розбору/лексем/символів ПРОГРАМИ tableOfSymb
numRow = 1

# довжина таблиці символів програми
# він же - номер останнього запису
len_tableOfSymb = len(tableOfSymb)
print(('len_tableOfSymb', len_tableOfSymb))
TableOfIdents = {}
postfixCode = []
postfixCodeCLR = []
tableOfLabel = {}
# # запуск парсера
# parseProgram()
def parseProgram():
    print('parseProgram():')
    parseToken('program', 'keyword', '\t')
    if not parseToken('myprogram', 'ident', '\t'):
        failParse("відсутній ідентифікатор програми", (numRow, 'program'))
    parseToken('{', 'punct', '\t')

    if tableOfSymb:
        while parseStatement():
            pass
        numLine, lex, tok = getSymb()
        if lex:
            failParse('Неочікуваний кінець програми', numLine)
        print('Parser: Синтаксичний аналіз і семантичний аналіз завершився успішно')
    else:
        print('Parser: Синтаксичний аналіз і семантичний аналіз завершився успішно')
def parseStatement():
    print('\t\tparseStatement():')
    # прочитаємо поточну лексему в таблиці розбору
    numLine, lex, tok = getSymb()
    # якщо токен - ідентифікатор
    # обробити інструкцію присвоювання


    if tok == 'ident':
        parseSimplestmt()
        return True
    # if tok ==  'ident':
    #     parseExpression()
    # обробка оголошення змінної
    elif (lex, tok) == ('int', 'keyword') or (lex, tok) == ('float', 'keyword') or (lex, tok) == ('bool', 'keyword'):
        parseVar()
        return True

    elif (lex, tok) == ('for', 'keyword'):
        parseFor()
        return True

    elif (lex, tok) == ('//', 'comment'):
        print('\t\t\tparseComment():')
        parseToken('//', 'comment', '\t' * 4)
        return True

    elif (lex, tok) == ('scan', 'keyword'):
        parseScan()
        return True

    elif (lex, tok) == ('println', 'keyword'):
        parsePrintln()
        return True
        
    elif (lex, tok) == ('if', 'keyword'):
        parseIf()
        return True

    else:
        # жодна з інструкцій не відповідає
        # поточній лексемі у таблиці розбору,
        return False

def getSymb():
    global numRow
    if numRow > len_tableOfSymb:
        return '', '', '',
        # failParse('getSymb(): неочікуваний кінець програми', numRow)
    numLine, lexeme, token, _ = tableOfSymb[numRow]
    return numLine, lexeme, token

def getSymbforSem(numRow):
    if numRow > len_tableOfSymb:
        return '', '', '',
        # failParse('getSymb(): неочікуваний кінець програми', numRow)
    numLine, lexeme, token, _ = tableOfSymb[numRow]
    return numLine, lexeme, token


def parseScan():
    global numRow
    print('\t\t\tparseScan():')
    parseToken('scan', 'keyword', '')
    parseToken('(', 'brackets_op', '')
    parseToken('&', 'punct', '')
    numLine, ident, tok = getSymb()
    if tok == 'ident':
        if IdentCheck(ident):
            numRow += 1
            print(numLine, ident, tok)
        else:
            failParse('Неоголощена змінна', numLine)
    else:
        failParse('Очікувалась змінна всередині scan', numLine)
    postfixCodeGen('lval',(ident, tok))
    postfixCodeCLR.append(f'   ldloca    {ident}')
    numLine, lex, tok = getSymb()
    if lex == ',':
        print(numLine, lex, tok)
        numRow += 1
        postfixCode.append(('IN', 'in_op'))
        postfixCode.append(('=', 'assign_op'))
        typ = TableOfIdents[ident][0]
        if typ == 'int':
            postfixCodeCLR.append(f'   stind.i4')
        else:
            postfixCodeCLR.append(f'   stind.r4')     
        while True:
            parseToken('&', 'punct', '')
            numLine, ident, tok = getSymb()
            if tok == 'ident':
                if IdentCheck(ident):
                    numRow += 1
                    print(numLine, ident, tok)
                else:
                    failParse('Неоголощена змінна', numLine)
            else:
                failParse('Очікувалась змінна всередині scan', numLine)
            postfixCodeGen('lval',(ident, tok))
            postfixCodeCLR.append(f'   ldloca    {ident}')
            numLine, lex, tok = getSymb()
            if lex != ',':
                break
            else:
                print(numLine, lex, tok)
                numRow += 1
                postfixCode.append(('IN', 'in_op'))
                postfixCode.append(('=', 'assign_op'))
                typ = TableOfIdents[ident][0]
                if typ == 'int':
                    postfixCodeCLR.append(f'   stind.i4')
                else:
                    postfixCodeCLR.append(f'   stind.r4')   

    parseToken(')', 'brackets_op', '')
    postfixCode.append(('IN', 'in_op'))
    postfixCode.append(('=', 'assign_op'))
    typ = TableOfIdents[ident][0]
    if typ == 'int':
        postfixCodeCLR.append(f'   stind.i4')
    else:
        postfixCodeCLR.append(f'   stind.r4')    
    parseToken(';','punct','')
    return True


def parseExpression():
    global numRow
    print('\t' * 5 + 'parseExpression():')
    numLine, lex, tok = getSymb()
    parseTerm()
    F = True
    # продовжувати розбирати Доданки (Term)
    # розділені лексемами '+' або '-'
    while F:
        numLine, lex, tok = getSymb()
        if tok in ('add_op'):
            numRow += 1
            print('\t' * 6 + 'в рядку {0} - {1}'.format(numLine, (lex, tok)))
            parseTerm()
            postfixCodeGen('add_op', (lex, tok))
            if lex == '+':
                postfixCodeCLR.append(f'   add')
            else:
                postfixCodeCLR.append(f'   sub')
        else:
            F = False
    return True


def parseTerm():
    global numRow
    print('\t' * 6 + 'parseTerm():')
    parseFactor()
    F = True
    # продовжувати розбирати Множники (Factor)
    # розділені лексемами '*' або '/'
    while F:
        numLine, lex, tok = getSymb()
        if tok in ('mul_op'):
            numRow += 1
            print('\t' * 6 + 'в рядку {0} - {1}'.format(numLine, (lex, tok)))
            parseFactor()
            postfixCodeGen('mul_op', (lex, tok))
            if lex == '*':
                postfixCodeCLR.append(f'   mul')
            else:
                postfixCodeCLR.append(f'   div')
        else:
            F = False
    return True


def parseFactor():
    global numRow
    print('\t' * 7 + 'parseFactor():')
    numLine, ident, tok = getSymb()
    numRow += 1
    numLine1, lex1, tok1 = getSymb()
    numRow -= 1
    # numforpow = numRow + 1
    # перша і друга альтернативи для Factor
    # якщо лексема - це константа або ідентифікатор
    if tok1 == 'pow_op':
        parsePower()

    elif tok in ('add_op'):
        _, lex1, _ = getSymb()
        numRow += 1
        numLine, lex, tok = getSymb()
        if tok in ('int', 'float', 'ident'):
            if tok == 'ident':
                if not IdentCheck(ident):
                    failParse('Неоголощена змінна', numLine)
            numRow += 1
            lex = lex1 + lex
            print('\t' * 7 + 'в рядку {0} - {1} '.format(numLine, (lex, tok)))
            if tok == 'ident':
                postfixCodeGen('rval', (lex, tok))
                postfixCodeCLR.append(f'   ldloc     {ident}')
            else:
                postfixCodeGen('const', (lex, tok))
                if tok == 'int':
                    postfixCodeCLR.append(f'   ldc.i4     {lex}')
                else:
                    postfixCodeCLR.append(f'   ldc.r4     {lex}')
        else:
            failParse('невідповідність у Expression.Factor -', numLine)
        
    elif tok in ('int', 'float', 'ident') or ident in ('True', 'False'):
        if tok == 'ident':
            if not IdentCheck(ident):
                failParse('Неоголощена змінна', numLine)        
        numRow += 1
        print('\t' * 7 + 'в рядку {0} - {1}'.format(numLine, (ident, tok)))
        if tok == 'ident':
            postfixCodeGen('rval', (ident, tok))
            postfixCodeCLR.append(f'   ldloc     {ident}')
        elif tok == 'keyword':
            postfixCodeGen('const', (ident, 'bool'))
        else:
            postfixCodeGen('const', (ident, tok))
            if tok == 'int':
                postfixCodeCLR.append(f'   ldc.i4     {ident}')
            else:
                postfixCodeCLR.append(f'   ldc.r4     {ident}')


    # третя альтернатива для Factor
    # якщо лексема - це відкриваюча дужка
    elif ident == '(':
        numRow += 1
        parseExpression()
        parseToken(')', 'brackets_op', '\t' * 7)
        print('\t' * 7 + 'в рядку {0} - {1}'.format(numLine, (ident, tok)))
    else:
        failParse('невідповідність у Expression.Factor', numLine)
    return True

def parsePower():
    global numRow
    print('\t' * 7 + 'parsePower():')
    numLine, lex, tok = getSymb()
    parseFactorforPow()
    parseToken('^', 'pow_op', '\t' * 7)
    parseFactor()
    postfixCodeGen('pow_op', ('^', 'pow_op',)) 
    # pow_op for CLR
    
    return True


def parsePrintln():
    global numRow
    print('\t\t\tparsePrintln():')
    parseToken('println', 'keyword', '')
    parseToken('(', 'brackets_op', '')
    parseExpression()

    numLine, lex, tok = getSymb()
    if lex == ',':
        print(numLine, lex, tok)
        numRow += 1
        postfixCode.append(('OUT','out_op'))
        while True:
            parseExpression()
            numLine, lex, tok = getSymb()
            if lex != ',':
                break
            else:
                print(numLine, lex, tok)
                numRow += 1
                postfixCode.append(('OUT','out_op'))

    parseToken(')', 'brackets_op', '')
    postfixCode.append(('OUT','out_op'))
    parseToken(';','punct','')
    return True


def parseFactorforPow():
    global numRow
    print('\t' * 7 + 'parseFactorforPow():')
    numLine, lex, tok = getSymb()
    # numforpow = numRow + 1
    # перша і друга альтернативи для Factor
    # якщо лексема - це константа або ідентифікатор
    if tok in ('int', 'float', 'ident'):
        numRow += 1
        print('\t' * 7 + 'в рядку {0} - {1}'.format(numLine, (lex, tok)))
        if tok == 'ident':
            postfixCodeGen('rval', (lex, tok))
            postfixCodeCLR.append(f'   ldloc     {lex}')
        else:
            postfixCodeGen('const', (lex, tok))
            if tok == 'int':
                postfixCodeCLR.append(f'   ldc.i4     {lex}')
            else:
                postfixCodeCLR.append(f'   ldc.r4     {lex}')

    # третя альтернатива для Factor
    # якщо лексема - це відкриваюча дужка
    elif lex == '(':
        numRow += 1
        parseExpression()
        parseToken(')', 'brackets_op', '\t' * 7)
        print('\t' * 7 + 'в рядку {0} - {1}'.format(numLine, (lex, tok)))
    
    else:
        failParse('невідповідність у Expression.Factor', numLine)
    return True


# def parseVar():
#     global numRow
#     print('\t' * 7 + 'parseVar():')
#     numLine, typeIdent, tok = getSymb()
#     parseToken(typeIdent, 'keyword', '\t' * 7)
#     numLine, ident, tok = getSymb()
#     if tok == 'ident':
#         if ident in TableOfIdents:
#             failParse('Змінна вже оголошена',numLine)
#         else:
#             numRow += 1
#             print('\t' * 7 + 'в рядку {0} - {1}'.format(numLine, (ident, tok)))
#             numLine, typeIdent, tok = getSymb()
#             if typeIdent in ('int', 'float', 'bool'):
#                 numRow += 1
#                 print('\t' * 7 + 'в рядку {0} - {1}'.format(numLine, (typeIdent, tok)))
#                 # postfixCodeGen('lval', (ident, tok))
#                 # postfixCodeCLR.append(f'   ldloca    {ident}')
#                 numLine, lex, tok = getSymb()
#                 if lex == '=':
#                     numRow += 1
#                     numRowForSem = numRow
#                     print(numRowForSem)
#                     print('\t' * 7 + 'в рядку {0} - {1}'.format(numLine, (lex, tok)))
#                     parseExpression()
#                     Expression = parseExpressionForAssign(typeIdent, numRowForSem)
#                     try:
#                         value = eval(Expression)
#                     except ZeroDivisionError:
#                          failParse('Ділення на 0', numLine)
#                     addToTableOfIdents(ident, typeIdent, value, numLine)
#                     postfixCodeGen('assign_op', ('=', 'assign_op'))
#                     if typeIdent == 'int':
#                         postfixCodeCLR.append(f'   stind.i4')
#                     else:
#                         postfixCodeCLR.append(f'   stind.r4')
#                     parseToken(';','punct','')
#                     return True
#                 # else:
#                 #     if typeIdent == 'bool':
#                 #         TableOfIdents[ident] = [typeIdent, 'False']
#                 #         postfixCodeGen('const', ('False', 'bool'))
#                 #     elif typeIdent == 'float':
#                 #         TableOfIdents[ident] = [typeIdent, 0.0]
#                 #         postfixCodeGen('const', ('0.0', 'float'))
#                 #     elif typeIdent == 'int':
#                 #         TableOfIdents[ident] = [typeIdent, 0]
#                 #         postfixCodeGen('const', ('0', 'int'))
#                 #     postfixCodeGen('assign_op', ('=', 'assign_op'))
#                 #     if typeIdent == 'int':
#                 #         postfixCodeCLR.append(f'   stind.i4')
#                 #     else:
#                 #         postfixCodeCLR.append(f'   stind.r4')
#                 #     parseToken(';','punct','')
#                 #     return True
#             else:
#                 failParse('Після назви змінної має бути int | float | bool', numLine)
#     else:
#         failParse('Очікувалась назва змінної', numLine)

def parseVar():
    global numRow
    print('\t' * 7 + 'parseVar():')
    numLine, typeIdent, tok = getSymb()
    parseToken(typeIdent, 'keyword', '\t' * 7)
    numLine, ident, tok = getSymb()
    if tok == 'ident':
        if ident in TableOfIdents:
            failParse('Змінна вже оголошена',numLine)
        else:
            numRow += 1
            print('\t' * 7 + 'в рядку {0} - {1}'.format(numLine, (ident, tok)))
            # numLine, typeIdent, tok = getSymb()
            # if typeIdent in ('int', 'float', 'bool'):
            numRow += 1
            print('\t' * 7 + 'в рядку {0} - {1}'.format(numLine, (typeIdent, tok)))
            postfixCodeGen('lval', (ident, tok))
            postfixCodeCLR.append(f'   ldloca    {ident}')
            numLine, lex, tok = getSymb()
            if lex == '=':
                numRow += 1
                numRowForSem = numRow
                print(numRowForSem)
                print('\t' * 7 + 'в рядку {0} - {1}'.format(numLine, (lex, tok)))
                parseExpression()
                Expression = parseExpressionForAssign(typeIdent, numRowForSem)
                try:
                    value = eval(Expression)
                except ZeroDivisionError:
                     failParse('Ділення на 0', numLine)
                addToTableOfIdents(ident, typeIdent, value, numLine)
                postfixCodeGen('assign_op', ('=', 'assign_op'))
                if typeIdent == 'int':
                    postfixCodeCLR.append(f'   stind.i4')
                else:
                    postfixCodeCLR.append(f'   stind.r4')
                parseToken(';','punct','')
                return True
                # else:
                #     if typeIdent == 'bool':
                #         TableOfIdents[ident] = [typeIdent, 'False']
                #         postfixCodeGen('const', ('False', 'bool'))
                #     elif typeIdent == 'float':
                #         TableOfIdents[ident] = [typeIdent, 0.0]
                #         postfixCodeGen('const', ('0.0', 'float'))
                #     elif typeIdent == 'int':
                #         TableOfIdents[ident] = [typeIdent, 0]
                #         postfixCodeGen('const', ('0', 'int'))
                #     postfixCodeGen('assign_op', ('=', 'assign_op'))
                #     if typeIdent == 'int':
                #         postfixCodeCLR.append(f'   stind.i4')
                #     else:
                #         postfixCodeCLR.append(f'   stind.r4')
                #     parseToken(';','punct','')
                #     return True
            # else:
            #     failParse('Після назви змінної має бути int | float | bool', numLine)
    else:
        failParse('Очікувалась назва змінної', numLine)



def parseSimplestmt():
    global numRow
    print('\t' * 5 + 'parseExpression():')
    numLine, ident, tok = getSymb()
    if parseIncDecStmt():
        pass
    elif tok == 'ident':
        if ident not in TableOfIdents:
            failParse('Присвоєння неоголошеній змінній', numLine)
        numRow += 1
        print('\t' * 7 + 'в рядку {0} - {1}'.format(numLine, (ident, tok)))
        postfixCodeGen('lval', (ident, tok))
        postfixCodeCLR.append(f'   ldloca    {ident}')
        numLine, assign, tok = getSymb()
        if tok == 'assign_op':
            numRow += 1
            typeIdent = TableOfIdents[ident][0]
            numRowForSem = numRow
            print('\t' * 7 + 'в рядку {0} - {1}'.format(numLine, (assign, tok)))
            if assign != '=':
                postfixCodeGen('rval', (ident, tok))
                postfixCodeCLR.append(f'   ldloc     {ident}')
            parseExpression()
            Expression = parseExpressionForAssign(typeIdent, numRowForSem)
            if assign != '=':
                value = TableOfIdents[ident][1]
                if assign[0] == '^':
                    Expression = str(value) + '**' + Expression
                else:     
                    Expression = str(value) + assign[0] + Expression
            try:
                value = eval(Expression)
            except ZeroDivisionError:
                failParse('Ділення на 0', numLine)
            addToTableOfIdents(ident, typeIdent, value, numLine) 
            parseToken(';','punct','')
            if assign != '=':
                postfixCodeGen('one_of_assign', (assign[0], 'one_of_assign'))
                if assign[0] == '+':
                    postfixCodeCLR.append(f'   add')
                elif assign[0] == '-':
                    postfixCodeCLR.append(f'   sub')
                elif assign[0] == '*':
                    postfixCodeCLR.append(f'   mul')
                elif assign[0] == '/':
                    postfixCodeCLR.append(f'   div')
                postfixCodeGen('assign_op', ('=', tok))
                if typeIdent == 'int':
                    postfixCodeCLR.append(f'   stind.i4')
                else:
                    postfixCodeCLR.append(f'   stind.r4')
            else:
                postfixCodeGen('assign_op', ('=', tok))
                if typeIdent == 'int':
                    postfixCodeCLR.append(f'   stind.i4')
                else:
                    postfixCodeCLR.append(f'   stind.r4')
            return True
        else:
            failParse('Очікувався assign_op',numLine)

def parseFor():
    global numRow
    print('\t' * 5 + 'parseFor():')
    parseToken('for', 'keyword', '\t' * 7)
    mitka2, mitka3, mitka4  = pasreForClause()

    postfixCode.append(mitka3)
    postfixCode.append((':','colon'))
    postfixCodeCLR.append(f'{mitka3[0]}:')
    parseBlock()
    postfixCode.append(mitka4)
    postfixCode.append(('JMP','jump'))
    postfixCodeCLR.append(f'   br        {mitka4[0]}')
    postfixCode.append(mitka2)
    postfixCode.append((':','colon'))
    postfixCodeCLR.append(f'{mitka2[0]}:')
    return True


def pasreForClause():
    global numRow
    print('\t' * 5 + 'parseForClause():')

    ident = parseShortVarDecl()
    parseToken(';', 'punct', '\t' * 7)
    m1 = createLabel()
    postfixCode.append(m1) # Трансляцiя
    postfixCode.append((':','colon'))
    parseCondition()
    m2 = createLabel()
    postfixCode.append(m2)
    postfixCode.append(('JF','jf'))
    postfixCodeCLR.append(f'   brfalse   {m3[0]}')
    m3 = createLabel()
    postfixCode.append(m3)
    postfixCode.append(('JMP','jump'))
    postfixCodeCLR.append(f'   br        {m3[0]}')


    parseToken(';', 'punct', '\t' * 7)

    m4 = createLabel()
    postfixCode.append(m4) # Трансляцiя
    postfixCode.append((':','colon'))
    postfixCodeCLR.append(f'{m4[0]}:')
    parseIncDecStmt()
    postfixCode.append(m1)
    postfixCode.append(('JMP','jump'))
    postfixCodeCLR.append(f'   br        {m1[0]}')
    return m2, m3, m4


def parseShortVarDecl():
    global numRow
    print('\t' * 5 + 'parseShortVarDecl():')
    numLine, ident, tok = getSymb()
    if tok == 'ident':
        if ident in TableOfIdents:
            failParse('Змінна вже оголошена',numLine)
        numRow += 1
        typeIdent = 'int'
        print('\t' * 7 + 'в рядку {0} - {1}'.format(numLine, (ident, tok)))
        postfixCodeGen('lval',(ident,tok))
        postfixCodeCLR.append(f'   ldloca    {ident}') 
        parseToken(':=', 'assign_op', '\t' * 7)
        numRowForSem = numRow 
        parseExpression()
        Expression = parseExpressionForAssign(typeIdent, numRowForSem)
        try:
            value = eval(Expression)
        except ZeroDivisionError:
            failParse('Ділення на 0', numLine)
        addToTableOfIdents(ident, typeIdent, value, numLine)
        postfixCodeGen('assign_op',('=','assign_op'))
        if typeIdent == 'int':
            postfixCodeCLR.append(f'   stind.i4')
        else:
            postfixCodeCLR.append(f'   stind.r4') 
        return ident
    else:
        failParse('Очікувалась змінна', numLine)
    


def parseCondition():
    global numRow
    Numforsem = numRow
    print('\t' * 5 + 'parseCondition():')
    parseExpression()
    Expression1 = parseExpForCond(Numforsem)
    if Expression1 == 'True' or Expression1 == 'False':
        typeExp1 = 'bool'
    else:
        try:
            typeExp1 = type(eval(Expression1))
        except ZeroDivisionError:
            failParse('Ділення на 0', numLine)
    numLine, lex, tok = getSymb()
    if tok == 'rel_op':
        numRow += 1
        Numforsem = numRow
        print('\t' * 7 + 'в рядку {0} - {1}'.format(numLine, (lex, tok)))
        parseExpression()
        Expression2 = parseExpForCond(Numforsem)
        if Expression2 == 'True' or Expression2 == 'False':
            typeExp2 = 'bool'
        else:
            try:
                typeExp2 = type(eval(Expression2))
            except ZeroDivisionError:
                failParse('Ділення на 0', numLine)
        if typeExp1 == 'bool' and typeExp2 in (int, float) or typeExp2 == 'bool' and typeExp1 in (int, float):
            failParse('Порівняння значень типу bool та int | float', numLine)
        postfixCodeGen('rel_op',(lex,tok))
        if lex == '>':
            postfixCodeCLR.append('   cgt')
        elif lex == '<':
            postfixCodeCLR.append('   clt')
        elif lex == '==':
            postfixCodeCLR.append('   ceq')
    return True

def parseIncDecStmt():
    global numRow
    numLine, ident, tok = getSymb()
    numRow += 1
    numLine1, post_op, tok1 = getSymb()
    numRow -= 1
    try: 
        typeIdent = TableOfIdents[ident][0]
    except:
        return False
    if ident not in TableOfIdents:
        failParse('неоголошена змінна',numLine)
    if typeIdent == 'bool':
        failParse('Змінна типу bool не може використовувати post_op',numLine)
    if tok1 == 'post_op':
        print('\t' * 5 + 'parseIncDecStmt():')
        numRow += 1
        print('\t' * 7 + 'в рядку {0} - {1}'.format(numLine, (ident, tok)))
        postfixCodeGen('lval',(ident, tok))
        postfixCodeCLR.append(f'   ldloca    {ident}')
        postfixCodeGen('rval',(ident, tok))
        postfixCodeCLR.append(f'   ldloc     {ident}')
        postfixCodeGen('const',('1', 'int'))
        postfixCodeCLR.append(f'   ldc.i4    1')
        if post_op == '++':
            TableOfIdents[ident][1] += 1
            postfixCodeGen('add_op',('+', 'add_op'))
            postfixCodeCLR.append(f'   add')
        elif post_op == '--':
            TableOfIdents[ident][1] -= 1
            postfixCodeGen('add_op',('-', 'add_op'))
            postfixCodeCLR.append(f'   sub')
        numRow += 1
        print('\t' * 7 + 'в рядку {0} - {1}'.format(numLine, (post_op, tok1)))
        postfixCodeGen('assign_op',('=', 'assign_op'))
        if typeIdent == 'int':
            postfixCodeCLR.append(f'   stind.i4')
        else:
            postfixCodeCLR.append(f'   stind.r4')
        return True
    return False

def parseBlock():
    parseToken('{', 'punct', '\t' * 7)
    while parseStatement():
        pass
    parseToken('}', 'punct', '\t' * 7)
    return True


def parseIf():
    global numRow
    print('\t' * 5 + 'parseif():')
    parseToken('if', 'keyword', '\t' * 7)
    parseCondition()
    m1 = createLabel()
    postfixCode.append(m1) # Трансляцiя
    postfixCode.append(('JF','jf'))
    postfixCodeCLR.append(f'   brfalse   {m1[0]}')
    parseBlock()
    m2 = createLabel()
    postfixCode.append(m2) # Трансляцiя
    postfixCode.append(('JMP','jump'))
    postfixCodeCLR.append(f'   br        {m2[0]}')
    postfixCode.append(m1) # Трансляцiя
    postfixCode.append((':','colon'))
    postfixCodeCLR.append(f'{m1[0]}:')
    numLine, lex, tok = getSymb()
    if lex == 'else':
        numRow += 1
        parseBlock()
    postfixCode.append(m2) # Трансляцiя
    postfixCode.append((':','colon'))
    postfixCodeCLR.append(f'{m2[0]}:')
    return True

def parseToken(lexeme, token, indent):
    # доступ до поточного рядка таблиці розбору
    global numRow

    # якщо всі записи таблиці розбору прочитані,
    # а парсер ще не знайшов якусь лексему
    if numRow > len_tableOfSymb:
        failParse('неочікуваний кінець програми', numRow)

    # прочитати з таблиці розбору
    # номер рядка програми, лексему та її токен
    numLine, lex, tok = getSymb()

    # тепер поточним буде наступний рядок таблиці розбору
    numRow += 1

    # чи збігаються лексема та токен таблиці розбору з заданими
    if (lex, tok) == (lexeme, token):
        # вивести у консоль номер рядка програми та лексему і токен
        print(indent + 'parseToken: В рядку {0} токен {1}'.format(numLine, (lexeme, token)))
        return True
    else:
        # згенерувати помилку та інформацію про те, що
        # лексема та токен таблиці розбору (lex,tok) відрізняються від
        # очікуваних (lexeme,token)
        failParse('Неочікуваний символ або пропущений символ', numLine)
        return False

# # Обробити помилки
# # вивести поточну інформацію та діагностичне повідомлення
def failParse(str, numLine):
    print('Parse:ERROR ' + str + ' у рядку ' + f'{numLine}')
    exit(1)


def parseExpressionForAssign(typeIdent, numRow):
    Expression = []
    Tokens = []
    numLine, PartOfExp, tok = getSymbforSem(numRow)
    while PartOfExp != ';':
        Expression.append(PartOfExp)
        Tokens.append(tok)
        numRow += 1
        _, PartOfExp, tok = getSymbforSem(numRow)
    for i, v in enumerate(Expression):
        if v in TableOfIdents:
            if typeIdent != TableOfIdents[v][0]:
                if typeIdent == 'float' and TableOfIdents[v][0] == 'int':
                    Expression[i] = str(TableOfIdents[v][1])
                else:
                    failParse('Невідповідність типів',numLine)
            else:
                Expression[i] = str(TableOfIdents[v][1])
        elif Tokens[i] == 'ident':
            failParse('Неоголошена змінна',numLine)
        elif v == '^':
            Expression[i] = '**'
    Expression = " ".join(Expression)
    return Expression


def parseExpForCond(numRow):
    Expression = []
    Tokens = []
    numLine, PartOfExp, tok = getSymbforSem(numRow)
    while tok not in ('rel_op', 'punct'):
        Expression.append(PartOfExp)
        Tokens.append(tok)
        numRow += 1
        _, PartOfExp, tok = getSymbforSem(numRow)
    for i, v in enumerate(Expression):
        if v in TableOfIdents:
            Expression[i] = str(TableOfIdents[v][1])
        elif Tokens[i] == 'ident':
            failParse('Неоголошена змінна',numLine)
        elif v == '^':
            Expression[i] = '**'
    if Expression[0] in ('True','False') and len(Expression) > 1:
        failParse('Невідповідність типів', numLine)
    Expression = " ".join(Expression)
    return Expression


def addToTableOfIdents(ident, typeIdent, value, numLine):
    print('Added to table of idents of updated')
    if typeIdent == 'float' and type(value) in (int, float):
        TableOfIdents[ident] = [typeIdent, float(value)]
    elif typeIdent == 'bool' and isinstance(value, bool):
        TableOfIdents[ident] = [typeIdent, value]
    elif typeIdent == 'int' and type(value) == int:
        TableOfIdents[ident] = [typeIdent, value]
    else:
        failParse('Невідповідність типів',numLine) 


def IdentCheck(ident):
    if ident in TableOfIdents:
        return True
    return False


def postfixCodeGen(case,toTran):
    if case == 'lval':
        lex,tok = toTran
        postfixCode.append((lex,'l-val'))
    elif case == 'rval':
        lex,tok = toTran
        postfixCode.append((lex,'r-val'))
    else:
        lex,tok = toTran
        postfixCode.append((lex,tok))


def createLabel():
    global tableOfLabel
    nmb = len(tableOfLabel)+1
    lexeme = "m"+str(nmb)
    val = tableOfLabel.get(lexeme)
    if val is None:
        tableOfLabel[lexeme] = 'val_undef'
        tok = 'label'
    else:
        tok = 'Конфлiкт мiток'
        print(tok)
        exit(1003)
    return (lexeme,tok)


parseProgram()


print(tableOfLabel)
print(TableOfIdents)
print('-'*30)
[print(i) for i in postfixCode]