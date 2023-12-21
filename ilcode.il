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
       [0]  float32 x,
       [1]  float32 c
     )

   .entrypoint
   //.maxstack  8
   ldloca    x
   ldc.r4     7.5
   stind.r4
   ldloca    c
   ldloc     x
   ldc.i4     3
   sub
   stind.r4
   ldloc     x
   ldloc     c
   clt
   brfalse   m1
   ldloc     x
   br        m2
m1:
   ldc.i4     15
m2:
	ldstr "x = "
	call void [mscorlib]System.Console::Write(string) 
	ldloc  x
	call void [mscorlib]System.Console::WriteLine(float32) 
	ldstr "c = "
	call void [mscorlib]System.Console::Write(string) 
	ldloc  c
	call void [mscorlib]System.Console::WriteLine(float32) 
	ret    
}
}