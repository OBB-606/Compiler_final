; ModuleID = "module"
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
define void @"main"() 
{
entry:
  %"__str_0" = alloca [17 x i8]
  store [17 x i8] c"testing Continue\00", [17 x i8]* %"__str_0"
  %".3" = bitcast [5 x i8]* @"__str_0" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", [17 x i8]* %"__str_0")
  br label %"whiletest"
exit:
  ret void
whiletest:
  %"__int_3" = load i32, i32* @"a"
  %"__bool_0" = icmp slt i32 %"__int_3", 20
  br i1 %"__bool_0", label %"loop", label %"afterloop"
loop:
  %"__int_5" = load i32, i32* @"a"
  %"__int_7" = add i32 %"__int_5", 1
  store i32 %"__int_7", i32* @"a"
  %"__int_8" = load i32, i32* @"a"
  %"__bool_1" = icmp eq i32 %"__int_8", 10
  %"__int_11" = load i32, i32* @"a"
  %"__int_13" = srem i32 %"__int_11", 2
  %"__bool_2" = icmp eq i32 1, %"__int_13"
  %"__bool_3" = or i1 %"__bool_1", %"__bool_2"
  br i1 %"__bool_3", label %"tblock", label %"fblock"
afterloop:
  store i32 0, i32* @"a"
  %"__str_1" = alloca [14 x i8]
  store [14 x i8] c"testing Break\00", [14 x i8]* %"__str_1"
  %".16" = bitcast [5 x i8]* @"__str_1" to i8*
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16", [14 x i8]* %"__str_1")
  br label %"whiletest.1"
tblock:
  br label %"whiletest"
fblock:
  br label %"endblock"
endblock:
  %"__int_14" = load i32, i32* @"a"
  %".11" = bitcast [5 x i8]* @"__int_14" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 %"__int_14")
  br label %"whiletest"
whiletest.1:
  %"__int_16" = load i32, i32* @"a"
  %"__bool_4" = icmp slt i32 %"__int_16", 20
  br i1 %"__bool_4", label %"loop.1", label %"afterloop.1"
loop.1:
  %"__int_18" = load i32, i32* @"a"
  %"__int_20" = add i32 %"__int_18", 1
  store i32 %"__int_20", i32* @"a"
  %"__int_21" = load i32, i32* @"a"
  %"__bool_5" = icmp eq i32 %"__int_21", 10
  br i1 %"__bool_5", label %"tblock.1", label %"fblock.1"
afterloop.1:
  br label %"exit"
tblock.1:
  br label %"afterloop.1"
fblock.1:
  br label %"endblock.1"
endblock.1:
  %"__int_23" = load i32, i32* @"a"
  %".24" = bitcast [5 x i8]* @"__int_23" to i8*
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24", i32 %"__int_23")
  br label %"whiletest.1"
}

@"__str_0" = internal constant [5 x i8] c"%s \0a\00"
@"__int_14" = internal constant [5 x i8] c"%i \0a\00"
@"__str_1" = internal constant [5 x i8] c"%s \0a\00"
@"__int_23" = internal constant [5 x i8] c"%i \0a\00"