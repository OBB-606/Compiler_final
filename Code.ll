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
  store double              0x0, double* @"h"
  br label %"exit"
exit:
  ret void
}

@"a" = global i32 0
@"b" = global i32 0
@"c" = global i32 0
@"h" = global double              0x0
define i32 @"factorial"(i32 %".1") 
{
entry:
  %"return" = alloca i32
  %"a" = alloca i32
  store i32 %".1", i32* %"a"
  %"factorial" = alloca i32
  store i32 0, i32* %"factorial"
  %"result" = alloca i32
  store i32 0, i32* %"result"
  %"c" = alloca i32
  store i32 0, i32* %"c"
  %"d" = alloca i32
  store i32 0, i32* %"d"
  %"e" = alloca i32
  store i32 0, i32* %"e"
  store i32 1, i32* %"result"
  store i32 1, i32* %"e"
  br label %"whiletest"
exit:
  %".19" = load i32, i32* %"return"
  ret i32 %".19"
whiletest:
  %"__int_10" = load i32, i32* %"e"
  %"__int_11" = load i32, i32* %"a"
  %"__bool_0" = icmp sle i32 %"__int_10", %"__int_11"
  br i1 %"__bool_0", label %"loop", label %"afterloop"
loop:
  %"__int_12" = load i32, i32* %"result"
  %"__int_13" = load i32, i32* %"e"
  %"__int_14" = mul i32 %"__int_12", %"__int_13"
  store i32 %"__int_14", i32* %"result"
  %"__int_15" = load i32, i32* %"e"
  %"__int_17" = add i32 %"__int_15", 1
  store i32 %"__int_17", i32* %"e"
  br label %"whiletest"
afterloop:
  %"__int_18" = load i32, i32* %"result"
  store i32 %"__int_18", i32* %"factorial"
  %"__int_19" = load i32, i32* %"factorial"
  store i32 %"__int_19", i32* %"return"
  br label %"exit"
}

define void @"main"() 
{
entry:
  %"__str_0" = alloca [11 x i8]
  store [11 x i8] c"factorials\00", [11 x i8]* %"__str_0"
  %".3" = bitcast [5 x i8]* @"__str_0" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", [11 x i8]* %"__str_0")
  store i32 10, i32* @"b"
  store i32 1, i32* @"a"
  br label %"whiletest"
exit:
  ret void
whiletest:
  %"__int_22" = load i32, i32* @"a"
  %"__int_23" = load i32, i32* @"b"
  %"__bool_1" = icmp sle i32 %"__int_22", %"__int_23"
  br i1 %"__bool_1", label %"loop", label %"afterloop"
loop:
  %"__int_24" = load i32, i32* @"a"
  %".9" = call i32 @"factorial"(i32 %"__int_24")
  store i32 %".9", i32* @"c"
  %"__int_26" = load i32, i32* @"c"
  %"__bool_2" = icmp sgt i32 %"__int_26", 6
  br i1 %"__bool_2", label %"tblock", label %"fblock"
afterloop:
  br label %"exit"
tblock:
  %"__str_1" = alloca [6 x i8]
  store [6 x i8] c"Rock!\00", [6 x i8]* %"__str_1"
  %".13" = bitcast [5 x i8]* @"__str_1" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13", [6 x i8]* %"__str_1")
  br label %"endblock"
fblock:
  br label %"endblock"
endblock:
  %"__int_28" = load i32, i32* @"c"
  %".17" = bitcast [5 x i8]* @"__int_28" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i32 %"__int_28")
  %"__int_29" = load i32, i32* @"a"
  %"__int_31" = add i32 %"__int_29", 1
  store i32 %"__int_31", i32* @"a"
  br label %"whiletest"
}

@"__str_0" = internal constant [5 x i8] c"%s \0a\00"
@"__str_1" = internal constant [5 x i8] c"%s \0a\00"
@"__int_28" = internal constant [5 x i8] c"%i \0a\00"