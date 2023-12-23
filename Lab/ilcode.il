// Referenced Assemblies.
.assembly extern mscorlib
{
  .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) 
  .ver 4:0:0:0
}

// Our assembly.
.assembly ilcode
{
  .hash algorithm 0x00008004
  .ver 0:0:0:0
}

.module ilcode.exe

// Definition of Program class.
.class private auto ansi beforefieldinit Program
  extends [mscorlib]System.Object
{
    
    .method private hidebysig static void Main(string[] args) cil managed
    {
    .locals (
       [0]  int32 a
     )

   .entrypoint
   //.maxstack  8
   ldloca    a
   ldc.i4     2
   stind.i4
   ldloca    a
   ldc.i4     2
   ldc.i4     2
   mul
   ldc.i4     2
   mul
   ldc.i4     2
   mul
   ldc.i4     2
   mul
   stind.i4
	ldstr "a = "
	call void [mscorlib]System.Console::Write(string) 
	ldloc  a
	call void [mscorlib]System.Console::WriteLine(int32) 
	ret    
}
}