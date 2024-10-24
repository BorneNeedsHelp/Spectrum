import os
import Spectrum_Parsing

class SpectrumFunctionLoader:
    @staticmethod
    def parse_file(file_path):
        if not file_path.endswith('.spcl'):
            raise ValueError(f"Invalid file extension for '{file_path}'. Must be '.spcl'.")

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

        if len(lines) != 7:
            raise ValueError(
                "File is not formatted correctly. Expected 7 lines for function_name, a, b, c, operation, cbackwards, and precision.")

        function_name = lines[0].strip()

        try:
            a = float(lines[1].strip())
            b = float(lines[2].strip())
            c = float(lines[3].strip())

        except ValueError:
            raise ValueError("Parameters 'a', 'b', and 'c' must be numeric values.")

        operation = lines[4].strip()
        cbackwards = lines[5].strip()

        try:
            precision = int(lines[6].strip())

        except ValueError:
            raise ValueError("Precision must be an integer value.")

        SpectrumFunctionLoader.parse_calculator(a, b, c, operation, cbackwards, precision)

    @staticmethod
    def save_function(function_name, a, b, c, operation, cbackwards, precision):
        extension = '.spcl'
        file_name = f"{function_name}{extension}"

        with open(file_name, 'w') as saved_file:
            saved_file.write(f"{function_name}\n{a}\n{b}\n{c}\n{operation}\n{cbackwards}\n{precision}")

        print(f"Function '{function_name}' saved to '{file_name}'.")

    @staticmethod
    def parse_calculator(a, b, c, operation, cbackwards, precision):
        Spectrum_Parsing.SpectrumPrecision(precision)
        spectrum_parser = Spectrum_Parsing.SpectrumParsing(a, b, c, cbackwards)
        operation_map = {
            'addition': 'Trio_HP_Addition',
            'subtraction': 'Trio_HP_Subtraction',
            'multiplication': 'Trio_HP_Multiplication',
            'division': 'Trio_HP_Division',
            'exponentiation': 'Trio_HP_Exponentiation',
            'modulation': 'Trio_HP_Modulation',
            'abs': 'Trio_HP_ABS',
            'sr': 'Trio_HP_SR'
        }

        func_name = operation_map.get(operation.lower())

        if not func_name:
            raise ValueError(f"Unsupported operation: {operation}")

        getattr(spectrum_parser, func_name)()

        spectrum_parser.compile_ir()
        result = spectrum_parser.EXECUTE_FUNCTION(func_name)
