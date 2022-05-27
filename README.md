# Compiler_final
Курсовая работа по дисциплине "Прикладные алгоритмы".
-----------------------------------------------------------------------------------------------------------------------------------------------------
В качестве целевой платформы была выбрана llvm
В результате работы программы получается файл Code.ll, который можно преобразовать в obj и запустить с помощью gcc.
```
llc -filetype=obj -relocation-model=pic Code.ll
gcc Code.o -o output
./output
```
-----------------------------------------------------------------------------------------------------------------------------------------------------
Используемые библиотеки:
    ```
    - PLY
    - llvmlite
    ```
-----------------------------------------------------------------------------------------------------------------------------------------------------
Запуск компиляции осуществляется путем запуска main файла, передав ему в качестве аргумента исходный текст программы. Запуск осуществляется как из 
терминала, так и из IDE. Для узлов AST генерируются соответсвующие инструкции, которые в свою очередь преобразовываются в инструкции объектного кода для llvm.
AST
![image](https://user-images.githubusercontent.com/76222113/170652464-3743ecf3-f78b-42c2-9037-1a6a3db75c77.png)
Text program:
```
program Hello;
var a,b,c : integer
begin
    a = 5;
    b = 10;
    c = a * b;
    print("a * b =");
    print(c)
end.
```
```
---------------------THREE-ADDRESS CODE---------------------
   __init   | void []	
      ('global_int', 'a')
      ('literal_int', 0, '__int_0')
      ('store_int', '__int_0', 'a')
      ('global_int', 'b')
      ('literal_int', 0, '__int_1')
      ('store_int', '__int_1', 'b')
      ('global_int', 'c')
      ('literal_int', 0, '__int_2')
      ('store_int', '__int_2', 'c')
      ('return_void',)
   main   | void []	
      ('literal_int', 5, '__int_3')
      ('store_int', '__int_3', 'a')
      ('literal_int', 10, '__int_4')
      ('store_int', '__int_4', 'b')
      ('load_int', 'a', '__int_5')
      ('load_int', 'b', '__int_6')
      ('mul_int', '__int_5', '__int_6', '__int_7')
      ('store_int', '__int_7', 'c')
      ('literal_string', 'a * b =', '__str_0')
      ('print_string', '__str_0')
      ('load_int', 'c', '__int_8')
      ('print_int', '__int_8')
[('literal_int', 5, '__int_3')]
[('store_int', '__int_3', 'a')]
[('literal_int', 10, '__int_4')]
[('store_int', '__int_4', 'b')]
[('load_int', 'a', '__int_5')]
[('load_int', 'b', '__int_6')]
[('mul_int', '__int_5', '__int_6', '__int_7')]
[('store_int', '__int_7', 'c')]
[('literal_string', 'a * b =', '__str_0')]
[('print_string', '__str_0')]
[('load_int', 'c', '__int_8')]
[('print_int', '__int_8')]
```
```
---------------------LLVM CODE---------------------
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
```
RESULT:
![image](https://user-images.githubusercontent.com/76222113/170652782-dadaac96-d4d7-4eb0-a989-44e27d66e5e7.png)


