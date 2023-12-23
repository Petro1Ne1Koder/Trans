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
       [2]  int32 c,
       [3]  float32 x,
       [4]  int32 i,
       [5]  float32 y
     )

   .entrypoint
   //.maxstack  8
   ldloca    a
   ldc.i4     2
   stind.i4
   ldloca    b
   ldc.i4     5
   stind.i4
   ldloca    a
   ldloc     a
   ldc.i4     3
   add
   stind.i4
   ldloca    a
   stind.i4
   ldloca    b
   stind.i4
   ldloca    b
   ldloc     b
   ldc.i4     2
   mul
   stind.i4
   ldloc     a
   ldloc     b
   ldloca    a
   ldloc     a
   ldc.i4     2
   sub
   stind.i4
   ldloca    x
   ldloc     a
   ldloc     b
   stind.r4
   ldloca    i
   ldc.i4     0
   stind.i4
   ldloc     x
   ldc.i4     2
   brfalse   m1
   ldloc     x
   br        m2
m1:
m2:
   brfalse   m3
   ldloc     i
   ldc.i4     3
   ldloca    i
   ldloc     i
   ldc.i4     1
   add
   stind.i4
   ldloc     i
   br        m4
m3:
m4:
	ldstr "a = "
	call void [mscorlib]System.Console::Write(string) 
	ldloc  a
	call void [mscorlib]System.Console::WriteLine(int32) 
	ldstr "b = "
	call void [mscorlib]System.Console::Write(string) 
	ldloc  b
	call void [mscorlib]System.Console::WriteLine(int32) 
	ldstr "c = "
	call void [mscorlib]System.Console::Write(string) 
	ldloc  c
	call void [mscorlib]System.Console::WriteLine(int32) 
	ldstr "x = "
	call void [mscorlib]System.Console::Write(string) 
	ldloc  x
	call void [mscorlib]System.Console::WriteLine(float32) 
	ldstr "i = "
	call void [mscorlib]System.Console::Write(string) 
	ldloc  i
	call void [mscorlib]System.Console::WriteLine(int32) 
	ldstr "y = "
	call void [mscorlib]System.Console::Write(string) 
	ldloc  y
	call void [mscorlib]System.Console::WriteLine(bool32) 
	ret    
}
}