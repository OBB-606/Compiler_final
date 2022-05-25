import ctypes
import sys
import time
from termcolor import cprint

import llvmlite.binding as llvm
from CodeGenerator import Block, GenerateCode, prTr
from Parser import build_tree, getTable

def run(llvm_ir):
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()

    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    mod = llvm.parse_assembly(llvm_ir)
    mod.verify()

    pmb = llvm.create_pass_manager_builder()
    pmb.opt_level = 1
    pm = llvm.create_module_pass_manager()
    pmb.populate(pm)
    pm.run(mod)

    engine = llvm.create_mcjit_compiler(mod, target_machine)
    init_ptr = engine.get_function_address('__init')
    init_func = ctypes.CFUNCTYPE(None)(init_ptr)
    init_func()
    main_ptr = engine.get_function_address('main')
    main_func = ctypes.CFUNCTYPE(None)(main_ptr)
    main_func()

def main():
    from llvm import compile_llvm

    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python3 -m run Tests/filename\n")
        raise SystemExit(1)

    source = open(sys.argv[1]).read()

    tree = build_tree(source)
    cprint("\n---------------------AST---------------------", 'red')
    cprint(tree, 'red')
    cprint("\n---------------------SYMBOLS_TABLE---------------------", 'green')
    tmp = getTable(tree)
    for i in tmp:
        cprint(f"{i} -- {tmp[i]}", 'green')
    # print(getTable(tree))

    block = Block()
    block.inithead('Main')
    block = GenerateCode(block, tree, 'global', False , getTable(tree))
    cprint("\n---------------------THREE-ADDRESS CODE---------------------", 'cyan')
    prTr(block, 1)

    llvm_code = compile_llvm(block)
    with open('Code.ll', 'wb') as f:
        f.write(llvm_code.encode('utf-8'))
        f.flush()

    cprint("\n---------------------LLVM CODE---------------------", 'blue')
    cprint(llvm_code, 'blue')
    cprint("\n---------------------RESULTS--------------------", 'cyan')
    run(llvm_code)

if __name__ == '__main__':
    start = time.time()
    main()
    cprint(f"running time: {time.time() - start} sec", 'magenta')
