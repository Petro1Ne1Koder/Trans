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
       [0]  int32 a,
       [1]  int32 b,
       [2]  float32 x
     )

   .entrypoint
   //.maxstack  8
   ldloca    a
   ldc.i4     2
   ldc.i4     2
   add
   stind.i4
   ldloca    b
   ldc.i4     5
   stind.i4
   brfalse   m1
   ldloc     a
   ldc.i4     5
   ldloca    a
   ldloc     a
   ldc.i4     1
   add
   stind.i4
   br        m2
m1:
m2:
	ldstr "a = "
	call void [mscorlib]System.Console::Write(string) 
	ldloc  a
	call void [mscorlib]System.Console::WriteLine(int32) 
	ldstr "b = "
	call void [mscorlib]System.Console::Write(string) 
	ldloc  b
	call void [mscorlib]System.Console::WriteLine(int32) 
	ldstr "x = "
	call void [mscorlib]System.Console::Write(string) 
	ldloc  x
	call void [mscorlib]System.Console::WriteLine(float32) 
	ret    
}
}