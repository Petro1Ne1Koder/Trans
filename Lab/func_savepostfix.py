from Lab.parse_02 import TableOfIdents, postfixCode

def SavePostfixCode(fileName):
    fname = fileName + ".postfix"
    f = open(fname, 'w')
    vars ='.vars(\n'
    for var in TableOfIdents:
       vars += '   ' + var + '   ' + TableOfIdents[var][0] + '\n'
    vars += ')\n\n\n'   
    labels = '.labels(\n'
    constants = '.constants(\n'
    code = '.code(\n'
    for i in range(len(postfixCode)):
        code += '   ' + postfixCode[i][0] + '   ' + postfixCode[i][1] + '\n'
        if postfixCode[i][1] == 'colon':
            labels += '   ' + postfixCode[i-1][0] + '   ' + str(i-1) + '\n'
        if postfixCode[i][1] in ('int', 'float', 'bool'):
            constants += '   ' + postfixCode[i][0] + '   ' + postfixCode[i][1] + '\n'
    constants += ')\n\n\n'
    labels += ')\n\n\n'  
    code += ')'
    f.write('.target: Postfix Machine\n.version: 0.2\n\n\n' + vars + labels + constants + code)

SavePostfixCode('postfixcode')
