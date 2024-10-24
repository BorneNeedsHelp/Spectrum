import llvmlite.ir as ir
import llvmlite.binding as llvm
from decimal import Decimal, getcontext
import ctypes


class SpectrumPrecision:
    def __init__(self, precision):
        getcontext().prec = precision


class SpectrumParsing:
    def __init__(self, a, b, c, cbackwards='abc'):
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()

        self.float_type = ir.FloatType()
        self.module = ir.Module(name="SpectrumPrec")
        self.a = Decimal(str(a))
        self.b = Decimal(str(b))
        self.c = Decimal(str(c))
        self.cbackwards = str(cbackwards)
        self.builder = None
        self.engine = None

    def Trio_HP_Addition(self):
        func_type = ir.FunctionType(self.float_type, [])
        calc_func = ir.Function(self.module, func_type, name="Trio_HP_Addition")
        block = calc_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        if self.cbackwards == 'cba':
            result = self.c + self.b + self.a
        elif self.cbackwards == 'bca':
            result = self.b + self.c + self.a
        elif self.cbackwards == 'cab':
            result = self.c + self.a + self.b
        elif self.cbackwards == 'bac':
            result = self.b + self.a + self.c
        elif self.cbackwards == 'acb':
            result = self.a + self.c + self.b
        elif self.cbackwards == 'abc' or self.cbackwards != 'abc':
            result = self.a + self.b + self.c

        llvm_result = ir.Constant(self.float_type, float(result))
        self.builder.ret(llvm_result)

    def Trio_HP_Subtraction(self):
        func_type = ir.FunctionType(self.float_type, [])
        calc_func = ir.Function(self.module, func_type, name="Trio_HP_Subtraction")
        block = calc_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        if self.cbackwards == 'cba':
            result = self.c - self.b - self.a
        elif self.cbackwards == 'bca':
            result = self.b - self.c - self.a
        elif self.cbackwards == 'cab':
            result = self.c - self.a - self.b
        elif self.cbackwards == 'bac':
            result = self.b - self.a - self.c
        elif self.cbackwards == 'acb':
            result = self.a - self.c - self.b
        elif self.cbackwards == 'abc' or self.cbackwards != 'abc':
            result = self.a - self.b - self.c

        llvm_result = ir.Constant(self.float_type, float(result))
        self.builder.ret(llvm_result)

    def Trio_HP_Multiplication(self):
        func_type = ir.FunctionType(self.float_type, [])
        calc_func = ir.Function(self.module, func_type, name="Trio_HP_Multiplication")
        block = calc_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        if self.cbackwards == 'cba':
            result = self.c * self.b * self.a
        elif self.cbackwards == 'bca':
            result = self.b * self.c * self.a
        elif self.cbackwards == 'cab':
            result = self.c * self.a * self.b
        elif self.cbackwards == 'bac':
            result = self.b * self.a * self.c
        elif self.cbackwards == 'acb':
            result = self.a * self.c * self.b
        elif self.cbackwards == 'abc' or self.cbackwards != 'abc':
            result = self.a * self.b * self.c

        llvm_result = ir.Constant(self.float_type, float(result))
        self.builder.ret(llvm_result)

    def Trio_HP_Division(self):
        func_type = ir.FunctionType(self.float_type, [])
        calc_func = ir.Function(self.module, func_type, name="Trio_HP_Division")
        block = calc_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        if self.cbackwards == 'cba':
            result = self.c / self.b / self.a
        elif self.cbackwards == 'bca':
            result = self.b / self.c / self.a
        elif self.cbackwards == 'cab':
            result = self.c / self.a / self.b
        elif self.cbackwards == 'bac':
            result = self.b / self.a / self.c
        elif self.cbackwards == 'acb':
            result = self.a / self.c / self.b
        elif self.cbackwards == 'abc' or self.cbackwards != 'abc':
            result = self.a / self.b / self.c

        llvm_result = ir.Constant(self.float_type, float(result))
        self.builder.ret(llvm_result)

    def Trio_HP_Exponentiation(self):
        func_type = ir.FunctionType(self.float_type, [])
        calc_func = ir.Function(self.module, func_type, name="Trio_HP_Exponentiation")
        block = calc_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        if self.cbackwards == 'cba':
            result = self.c ** self.b ** self.a
        elif self.cbackwards == 'bca':
            result = self.b ** self.c ** self.a
        elif self.cbackwards == 'cab':
            result = self.c ** self.a ** self.b
        elif self.cbackwards == 'bac':
            result = self.b ** self.a ** self.c
        elif self.cbackwards == 'acb':
            result = self.a ** self.c ** self.b
        elif self.cbackwards == 'abc' or self.cbackwards != 'abc':
            result = self.a ** self.b ** self.c

        llvm_result = ir.Constant(self.float_type, float(result))
        self.builder.ret(llvm_result)

    def Trio_HP_Modulation(self):
        func_type = ir.FunctionType(self.float_type, [])
        calc_func = ir.Function(self.module, func_type, name="Trio_HP_Modulation")
        block = calc_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        if self.cbackwards == 'cba':
            result = self.c % self.b % self.a
        elif self.cbackwards == 'bca':
            result = self.b % self.c % self.a
        elif self.cbackwards == 'cab':
            result = self.c % self.a % self.b
        elif self.cbackwards == 'bac':
            result = self.b % self.a % self.c
        elif self.cbackwards == 'acb':
            result = self.a % self.c % self.b
        elif self.cbackwards == 'abc' or self.cbackwards != 'abc':
            result = self.a % self.b % self.c

        llvm_result = ir.Constant(self.float_type, float(result))
        self.builder.ret(llvm_result)

    def Trio_HP_ABS(self):
        func_type = ir.FunctionType(self.float_type, [])
        calc_func = ir.Function(self.module, func_type, name="Trio_HP_ABS")
        block = calc_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        if self.cbackwards == 'b':
            result = -self.b if self.b < 0 else self.b
        elif self.cbackwards == 'c':
            result = -self.c if self.c < 0 else self.c
        elif self.cbackwards == 'abc' or self.cbackwards != 'abc':
            result = -self.a if self.a < 0 else self.a

        llvm_result = ir.Constant(self.float_type, float(result))
        self.builder.ret(llvm_result)

    def Trio_HP_SR(self):
        func_type = ir.FunctionType(self.float_type, [])
        calc_func = ir.Function(self.module, func_type, name="Trio_HP_SR")
        block = calc_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        if self.cbackwards == 'b':
            self.b = abs(self.b).sqrt()
        elif self.cbackwards == 'c':
            self.c = abs(self.c).sqrt()
        elif self.cbackwards == 'abc' or self.cbackwards != 'abc':
            self.a = abs(self.a).sqrt()

        llvm_result = ir.Constant(self.float_type, float(result))
        self.builder.ret(llvm_result)

    def compile_ir(self):
        target = llvm.Target.from_default_triple()
        target_machine = target.create_target_machine()
        llvm_module = llvm.parse_assembly(str(self.module))
        llvm_module.verify()
        self.engine = llvm.create_mcjit_compiler(llvm_module, target_machine)
        self.engine.finalize_object()
        self.engine.run_static_constructors()

        print("Compilation complete and ready for execution.")

    def EXECUTE_FUNCTION(self, func_name):
        if not self.engine:
            raise RuntimeError("LLVM execution engine is not initialized. Call compile_ir() first.")

        func_ptr = self.engine.get_function_address(func_name)
        if not func_ptr:
            raise RuntimeError(f"Function '{func_name}' could not be found in the compiled module.")

        cfunc = ctypes.CFUNCTYPE(ctypes.c_float)(func_ptr)
        result = cfunc()
        print(f"Result of {func_name}: {result}")
        return result

    def generate_llvm_ir(self):
        print("Generated LLVM IR:")
        print(self.module)

# Copyright (c), with the: Full Restricted Code Usage; license
