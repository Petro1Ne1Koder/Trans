from parse_02 import TableOfIdents, postfixCodeCLR


def saveCIL(fileName):
    fname = fileName + ".il"
    f = open(fname, 'w')
    header = """// Referenced Assemblies.
.assembly extern mscorlib
{
  .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) 
  .ver 4:0:0:0
}

// Our assembly.
.assembly """ + fileName + """
{
  .hash algorithm 0x00008004
  .ver 0:0:0:0
}

.module """ + fileName + """.exe

// Definition of Program class.
.class private auto ansi beforefieldinit Program
  extends [mscorlib]System.Object
{

    .method private hidebysig static void Main(string[] args) cil managed
    {
    .locals (
"""
    # f.write(header)

    cntVars = len(TableOfIdents)
    print(cntVars)
    localVars = ""
    comma = ","
    index = 0
    for x in TableOfIdents:
        tp, _ = TableOfIdents[x]
        if tp == 'int':
            tpil = 'int32'
        else:
            tpil = 'float32'

        if index == cntVars - 1: comma = "\n     )"
        localVars += "       [{0}]  {1} {2}".format(index - 0, tpil, x) + comma + "\n"
        index += 1
    # print((x,a))
    entrypoint = """
   .entrypoint
   //.maxstack  8\n"""
    code = ""
    num = 0

    while num < len(postfixCodeCLR):
        if 'ldloc' in postfixCodeCLR[num] or 'ldc' in postfixCodeCLR[num]:
            if postfixCodeCLR[num + 1] == 'OUT' and 'ldloc' in postfixCodeCLR[num]:
                tp, _ = TableOfIdents[postfixCodeCLR[num][13]]
                tp += '32'
                code += "\t" + 'ldstr "' + postfixCodeCLR[num][13] + ' = "\n'
                code += "\t " + "call void [mscorlib]System.Console::Write(string) \n"
                code += "\t " + "ldloc  " + postfixCodeCLR[num][13] + "\n"
                code += "\t " + "call void [mscorlib]System.Console::WriteLine(" + tp + ") \n"
            elif postfixCodeCLR[num + 1] == 'OUT' and 'ldc' in postfixCodeCLR[num]:
                code += "\t" + 'ldstr " ' + postfixCodeCLR[num][14] + ' "' + "\n"
                code += "\t " + "call void [mscorlib]System.Console::WriteLine(string) \n"
            else:
                code += postfixCodeCLR[num] + "\n"
        elif postfixCodeCLR[num] == 'OUT':
            pass
        else:
            code += postfixCodeCLR[num] + "\n"
        num += 1
    # for instr in postfixCodeCLR:
    #   # if instr == 'OUT':

    #   code += instr + "\n"

    # виведення значень змінних
    values = ""
    for x in TableOfIdents:
        values += "\t" + 'ldstr "' + x + ' = "\n'
        values += "\t" + "call void [mscorlib]System.Console::Write(string) \n"
        tp, _ = TableOfIdents[x]
        tp += '32'
        values += "\t" + "ldloc  " + x + "\n"
        values += "\t" + "call void [mscorlib]System.Console::WriteLine(" + tp + ") \n"

    f.write(header + localVars + entrypoint + code + values + "\tret    \n}\n}")
    f.close()
    print(f"IL-програма для CLR збережена у файлі {fname}")


print(postfixCodeCLR)
saveCIL('ilcode')