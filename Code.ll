; ModuleID = "I want zachot"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

define void @"__init"() 
{
entry:
  store i32 0, i32* @"a"
  store i32 0, i32* @"b"
  store i32 0, i32* @"c"
  br label %"exit"
exit:
  ret void
}

@"a" = global i32 0
@"b" = global i32 0
@"c" = global i32 0
define void @"main"() 
{
entry:
  store i32 5, i32* @"a"
  store i32 10, i32* @"b"
  %"__int_5" = load i32, i32* @"a"
  %"__int_6" = load i32, i32* @"b"
  %"__int_7" = mul i32 %"__int_5", %"__int_6"
  store i32 %"__int_7", i32* @"c"
  %"__str_0" = alloca [8 x i8]
  store [8 x i8] c"a * b =\00", [8 x i8]* %"__str_0"
  %".6" = bitcast [5 x i8]* @"__str_0" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", [8 x i8]* %"__str_0")
  %"__int_8" = load i32, i32* @"c"
  %".8" = bitcast [5 x i8]* @"__int_8" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %"__int_8")
  br label %"exit"
exit:
  ret void
}

@"__str_0" = internal constant [5 x i8] c"%s \0a\00"
@"__int_8" = internal constant [5 x i8] c"%i \0a\00"