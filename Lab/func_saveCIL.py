from Lab.parse_02 import TableOfIdents, postfixCodeCLR

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
.assembly """ +fileName+ """
{
  .hash algorithm 0x00008004
  .ver 0:0:0:0
}

.module """ +fileName+ """.exe

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
    if tp == 'int': tpil = 'int32' 
    else: tpil = 'float32'
    
    if index == cntVars-1: comma = "\n     )"
    localVars += "       [{0}]  {1} {2}".format(index-0,tpil, x) + comma + "\n"
    index += 1
  # print((x,a))
  entrypoint = """
   .entrypoint
   //.maxstack  8\n"""
  code = ""
  for instr in postfixCodeCLR:
    code += instr + "\n"
    
  # виведення значень змінних
  values = ""
  for x in TableOfIdents:
    values += "\t" + 'ldstr "' + x + ' = "\n'
    values += "\t" + "call void [mscorlib]System.Console::Write(string) \n"
    tp,_ = TableOfIdents[x]
    tp += '32'
    values += "\t" + "ldloc  " + x + "\n"
    values += "\t" + "call void [mscorlib]System.Console::WriteLine(" +tp + ") \n" 
    
  f.write(header + localVars + entrypoint +code + values +"\tret    \n}\n}")
  f.close()
  print(f"IL-програма для CLR збережена у файлі {fname}")


saveCIL('ilcode')