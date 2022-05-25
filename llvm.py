from llvmlite import binding, ir
from llvmlite.ir import (
    Module, IRBuilder, Function, IntType, DoubleType, VoidType, Constant,
    GlobalVariable, FunctionType , ArrayType
)
from CodeGenerator import GenerateCode, Block, prTr
from Parser import build_tree

int_type = IntType(32)
float_type = DoubleType()
bool_type = IntType(1)
void_type = VoidType()

typemap = {
    'int': int_type,
    'float': float_type,

    'bool': bool_type,
    'void': void_type
}

class GenerateLLVM(object):

    def __init__(self, name='module'):

        self.module = Module(name)
        self.module.triple = binding.get_default_triple()
        self.block = None
        self.builder = None
        self.globals = {}
        self.locals = {}
        self.temps = {}
        self.last_branch = None
     #   self._declare_print_function_int()
        self._declare_print_function_string()

    #def _declare_print_function_int(self):
    #    voidptr_ty = IntType(8).as_pointer()
    #    print_ty = FunctionType(IntType(32), [voidptr_ty], var_arg=True)
    #    printint = Function(self.module, print_ty, name="printint")
    #    self.printint = printint
    def _declare_print_function_string(self):
        self.printf= Function(self.module, FunctionType(IntType(32), [IntType(8).as_pointer()], var_arg=True), name="printf")

    def start_function(self, name, rettypename, parmtypenames):
        rettype = typemap[rettypename]
        parmtypes = [typemap[pname] for pname in parmtypenames]
        func_type = FunctionType(rettype, parmtypes)

        self.function = Function(self.module, func_type, name=name)
        self.block = self.function.append_basic_block("entry")
        self.builder = IRBuilder(self.block)
        self.exit_block = self.function.append_basic_block("exit")
        self.locals = {}
        self.temps = {}

        if rettype is not void_type:
            self.locals['return'] = self.builder.alloca(rettype, name="return")

        self.globals[name] = self.function

    def new_basic_block(self, name=''):
        self.builder = IRBuilder(self.block.instructions)
        return self.function.append_basic_block(name)



    def generate_code(self, ircode):
        for opcode, *args in ircode:
            if hasattr(self, 'emit_' + opcode):
                getattr(self, 'emit_' + opcode)(*args)
            else:
                print('Warning: No emit_' + opcode + '() method')

    def terminate(self):
        # Add a return statement. This connects the last block to the exit
        # block.
        # The return statement is then emitted
        if self.last_branch != self.block:
            self.builder.branch(self.exit_block)
        self.builder.position_at_end(self.exit_block)

        if 'return' in self.locals:
            self.builder.ret(self.builder.load(self.locals['return']))
        else:
            self.builder.ret_void()

    def add_block(self, name):
        # Add a new block to the existing function
        return self.function.append_basic_block(name)

    def set_block(self, block):
        # Sets the current block for adding more code
        self.block = block
        self.builder.position_at_end(block)

    def cbranch(self, testvar, true_block, false_block):

        self.builder.cbranch(self.temps[testvar], true_block, false_block)

    def branch(self, next_block):
        if self.last_branch != self.block:
            self.builder.branch(next_block)
        self.last_branch = self.block

    def emit_literal_int(self, value, target):
        self.temps[target] = Constant(int_type, value)

    def emit_literal_float(self, value, target):
        self.temps[target] = Constant(float_type, value)

    def emit_literal_string(self, value, target):
        value = value + '\0'
        c_str_val =  Constant(ArrayType(IntType(8), len(value)),bytearray(value.encode("utf8")))
        var = self.builder.alloca(c_str_val.type,name= target)
        self.builder.store(c_str_val,var)
        self.temps[target] = var

    def emit_alloc_int(self, name):
        var = self.builder.alloca(int_type, name=name)
        var.initializer = Constant(int_type, 0)
        self.locals[name] = var

    def emit_alloc_float(self, name):
        var = self.builder.alloca(float_type, name=name)
        var.initializer = Constant(float_type, 0)
        self.locals[name] = var

    def emit_global_int(self, name):
        var = GlobalVariable(self.module, int_type, name=name)
        var.initializer = Constant(int_type, 0)
        self.globals[name] = var

    def emit_global_float(self, name):
        var = GlobalVariable(self.module, float_type, name=name)
        var.initializer = Constant(float_type, 0)
        self.globals[name] = var




    def lookup_var(self, name):
        if name in self.locals:
            return self.locals[name]
        else:
            return self.globals[name]

    def emit_load_int(self, name, target):
           self.temps[target] = self.builder.load(self.lookup_var(name), target)

    def emit_load_float(self, name, target):
        self.temps[target] = self.builder.load(self.lookup_var(name), target)

    def emit_store_int(self, source, target):
        self.builder.store(self.temps[source], self.lookup_var(target))

    def emit_store_float(self, source, target):
        self.builder.store(self.temps[source], self.lookup_var(target))

    def emit_add_int(self, left, right, target):
        self.temps[target] = self.builder.add(
            self.temps[left], self.temps[right], target)

    def emit_add_float(self, left, right, target):
        self.temps[target] = self.builder.fadd(
            self.temps[left], self.temps[right], target)


    def emit_sub_int(self, left, right, target):
        self.temps[target] = self.builder.sub(
            self.temps[left], self.temps[right], target)

    def emit_sub_float(self, left, right, target):
        self.temps[target] = self.builder.fsub(
            self.temps[left], self.temps[right], target)

    def emit_mul_int(self, left, right, target):
        self.temps[target] = self.builder.mul(
            self.temps[left], self.temps[right], target)

    def emit_mul_float(self, left, right, target):
        self.temps[target] = self.builder.fmul(
            self.temps[left], self.temps[right], target)


    def emit_div_int(self, left, right, target):
        self.temps[target] = self.builder.sdiv(
            self.temps[left], self.temps[right], target)

    def emit_mod_int(self, left, right, target):
        self.temps[target] = self.builder.srem(
            self.temps[left], self.temps[right], target)

    def emit_mod_float(self, left, right, target):
        self.temps[target] = self.builder.frem(
            self.temps[left], self.temps[right], target)


    def emit_div_float(self, left, right, target):
        self.temps[target] = self.builder.fdiv(
            self.temps[left], self.temps[right], target)

    def emit_convert_to_float(self, source, target):
        self.temps[target] = self.builder.sitofp(self.temps[source],DoubleType(),name=target)

    def emit_uadd_int(self, source, target):
        self.temps[target] = self.builder.add(
            Constant(int_type, 0),
            self.temps[source],
            target)

    def emit_uadd_float(self, source, target):
        self.temps[target] = self.builder.fadd(
            Constant(float_type, 0.0),
            self.temps[source],
            target)


    def emit_usub_int(self, source, target):
        self.temps[target] = self.builder.sub(
            Constant(int_type, 0),
            self.temps[source],
            target)

    def emit_usub_float(self, source, target):
        self.temps[target] = self.builder.fsub(
            Constant(float_type, 0.0),
            self.temps[source],
            target)


    def emit_lt_int(self, left, right, target):
        self.temps[target] = self.builder.icmp_signed(
            '<', self.temps[left], self.temps[right], target)

    def emit_lt_float(self, left, right, target):
        self.temps[target] = self.builder.fcmp_ordered(
            '<', self.temps[left], self.temps[right], target)


    def emit_le_int(self, left, right, target):
        self.temps[target] = self.builder.icmp_signed(
            '<=', self.temps[left], self.temps[right], target)

    def emit_le_float(self, left, right, target):
        self.temps[target] = self.builder.fcmp_ordered(
            '<=', self.temps[left], self.temps[right], target)


    def emit_gt_int(self, left, right, target):
        self.temps[target] = self.builder.icmp_signed(
            '>', self.temps[left], self.temps[right], target)

    def emit_gt_float(self, left, right, target):
        self.temps[target] = self.builder.fcmp_ordered(
            '>', self.temps[left], self.temps[right], target)


    def emit_ge_int(self, left, right, target):
        self.temps[target] = self.builder.icmp_signed(
            '>=', self.temps[left], self.temps[right], target)

    def emit_ge_float(self, left, right, target):
        self.temps[target] = self.builder.fcmp_ordered(
            '>=', self.temps[left], self.temps[right], target)


    def emit_eq_int(self, left, right, target):
        self.temps[target] = self.builder.icmp_signed(
            '==', self.temps[left], self.temps[right], target)

    def emit_eq_bool(self, left, right, target):
        self.temps[target] = self.builder.icmp_signed(
            '==', self.temps[left], self.temps[right], target)

    def emit_eq_float(self, left, right, target):
        self.temps[target] = self.builder.fcmp_ordered(
            '==', self.temps[left], self.temps[right], target)

    def emit_ne_int(self, left, right, target):
        self.temps[target] = self.builder.icmp_signed(
            '!=', self.temps[left], self.temps[right], target)

    def emit_ne_bool(self, left, right, target):
        self.temps[target] = self.builder.icmp_signed(
            '!=', self.temps[left], self.temps[right], target)

    def emit_ne_float(self, left, right, target):
        self.temps[target] = self.builder.fcmp_ordered(
            '!=', self.temps[left], self.temps[right], target)

    def emit_and_bool(self, left, right, target):
        self.temps[target] = self.builder.and_(
            self.temps[left], self.temps[right], target)

    def emit_or_bool(self, left, right, target):
        self.temps[target] = self.builder.or_(
            self.temps[left], self.temps[right], target)

    def emit_not_bool(self, source, target):
        self.temps[target] = self.builder.icmp_signed(
            '==', self.temps[source], Constant(bool_type, 0), target)




    def emit_call_func(self, funcname, *args):
        target = args[-1]
        func = self.globals[funcname]
        argvals = [self.temps[name] for name in args[:-1]]
        self.temps[target] = self.builder.call(func, argvals)

    def emit_call_proc(self, funcname, *args):
        target = void_type
        func = self.globals[funcname]
        argvals = [self.temps[name] for name in args]
        self.temps[target] = self.builder.call(func, argvals)

    def emit_parm_int(self, name, num):
        var = self.builder.alloca(int_type, name=name)
        self.builder.store(self.function.args[num], var)
        self.locals[name] = var

    def emit_parm_float(self, name, num):
        #print(name, num)
        var = self.builder.alloca(float_type, name=name)
        self.builder.store(self.function.args[num], var)
        self.locals[name] = var

    def emit_parm_bool(self, name, num):
        var = self.builder.alloca(bool_type, name=name)
        self.builder.store(self.function.args[num], var)
        self.locals[name] = var

    def emit_return_int(self, source):
        self.builder.store(self.temps[source], self.locals['return'])
        self.branch(self.exit_block)

    def emit_return_float(self, source):
        self.builder.store(self.temps[source], self.locals['return'])
        self.branch(self.exit_block)

    def emit_return_void(self):
        self.branch(self.exit_block)

    def emit_print_float(self, source):
        value = self.temps[source]
        voidprt_ty = IntType(8).as_pointer()
        fmt = "%f \n\0"
        c_fmt = Constant(ArrayType(IntType(8), len(fmt)), bytearray(fmt.encode("utf8")))
        global_fmt = GlobalVariable(self.module, c_fmt.type, name=source)
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_arg = self.builder.bitcast(global_fmt, voidprt_ty)
        self.builder.call(self.printf, [fmt_arg, value])

    def emit_print_int(self, source):
        value = self.temps[source]
        voidprt_ty = IntType(8).as_pointer()
        fmt = "%i \n\0"
        c_fmt = Constant(ArrayType(IntType(8), len(fmt)), bytearray(fmt.encode("utf8")))
        global_fmt = GlobalVariable(self.module, c_fmt.type, name=source)
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_arg = self.builder.bitcast(global_fmt, voidprt_ty)
        self.builder.call(self.printf, [fmt_arg, value])

    def emit_print_string(self, source):
        value = self.temps[source]
        voidprt_ty = IntType(8).as_pointer()
        fmt = "%s \n\0"
        c_fmt = Constant(ir.ArrayType(ir.IntType(8), len(fmt)),bytearray(fmt.encode("utf8")))
        global_fmt = GlobalVariable(self.module, c_fmt.type, name=source)
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_arg = self.builder.bitcast(global_fmt, voidprt_ty)
        self.builder.call(self.printf, [fmt_arg, value])

class GenerateBlocksLLVM( object ):

    def partition(self, block):
        for i in block.instructions:
            if i.__class__ == tuple:
                if i[0] == 'break':
                    afterloopik = afterloops.pop()[0]
                    self.gen.branch(afterloopik)
                    print([i])
                    return
                elif i[0] == 'continue':
                    afterloopik = afterloops.pop()[1]
                    self.gen.branch(afterloopik)
                    print([i])
                    return
                else:
                    print([i])
                    self.visit_BasicBlock([i])
            elif i.head == 'IfBlock':
                self.visit_IfBlock(i)
            elif i.head == 'WhileBlock':
                self.visit_WhileBlock(i)
            else:
                self.partition(i)
    def __init__(self, generator):
        self.gen = generator

    def generate_function(self, func):
        name = func.head
        if func.head.startswith('func'):
            name = func.head[5:]
        if func.head.startswith('proc'):
            name = func.head[5:]

        self.gen.start_function(name, func.return_type, func.params)
        if name == '__init':
            self.visit_BasicBlock(func.instructions)

        else:
            self.partition(func)
        self.gen.terminate()



    def visit_BasicBlock(self, block):

        self.gen.generate_code(block)

    def visit_IfBlock(self, block):

        self.gen.generate_code(block.instructions[0].instructions)
        tblock = self.gen.add_block("tblock")
        fblock = self.gen.add_block("fblock")
        endblock = self.gen.add_block("endblock")

        testvar = block.instructions[0].instructions[len(block.instructions[0].instructions)-1][len(block.instructions[0].instructions[len(block.instructions[0].instructions)-1])-1]
        #print(testvar)

        self.gen.cbranch(testvar, tblock, fblock)

        self.gen.set_block(tblock)
        self.partition(block.instructions[1])
        self.gen.branch(endblock)

        self.gen.set_block(fblock)
        self.gen.branch(endblock)

        self.gen.set_block(endblock)

    def visit_WhileBlock(self, block):
        test_block = self.gen.add_block("whiletest")
        testvar = block.instructions[0].instructions[len(block.instructions[0].instructions) - 1][len(block.instructions[0].instructions[len(block.instructions[0].instructions) - 1]) - 1]
        self.gen.branch(test_block)
        self.gen.set_block(test_block)

        self.gen.generate_code(block.instructions[0].instructions)

        loop_block = self.gen.add_block("loop")
        after_loop = self.gen.add_block("afterloop")
        afterloops.append([after_loop, test_block])  # добавляем названия label'ов для break и continue

        self.gen.cbranch(testvar, loop_block, after_loop)

        self.gen.set_block(loop_block)
        self.partition(block.instructions[1])
        self.gen.branch(test_block)

        self.gen.set_block(after_loop)
afterloops =[]
def compile_llvm(source):



    functions = source.instructions
    #print(functions)
    generator = GenerateLLVM()
    blockgen = GenerateBlocksLLVM(generator)
    for func in functions:
        blockgen.generate_function(func)


    return str(generator.module)


def main():
    data = '''
    program Hello;
    var a,b,c : integer
    var h : real
    function Sejvil (o : integer; f: integer ) : integer; 
    var v: real
    var g: real
       begin
       end;
    function Mumima (dfss, dss : integer; sdfsdf: integer ) : real; 
    var vaad: real
       begin
       end;   
    procedure Tafa (o : integer ; nbnb : real); 
    var  jkjhkg, h: real
       begin
       end;
    function fd1234 (a , b : integer ) : integer; 
    var vfffasd: real
       begin
       end;
    begin
      if ((0.0 + h * 3.2) > (20))
        then  
            begin
               write(a);
               write(b)

            end ;

      while (a > 10) and ( a < 2) do
      begin
        a := fd1234( 42,b)
      end;
      a := 10;
      b := 20
    end. 
    '''

    tree = build_tree(data)
    bloc = Block()
    bloc.inithead('Main')
    bloc = GenerateCode(bloc, tree, 'global',False)
    prTr(bloc,1)
    llvm_code = compile_llvm(bloc)
if __name__ == '__main__':
    main()
