import Spectrum_Parsing, SpectrumFunctionLoader

class SpectrumEasyparse:
    @staticmethod
    def Execute(function, a, b, c, cbackwards, precision):
        Spectrum_Parsing.SpectrumPrecision(precision)
        spectrum_parser = Spectrum_Parsing.SpectrumParsing(a, b, c, cbackwards)

        if hasattr(spectrum_parser, function):
            getattr(spectrum_parser, function)()
        else:
            raise ValueError(f"The function '{function}' does not exist in SpectrumParsing.")

        spectrum_parser.generate_llvm_ir()
        spectrum_parser.compile_ir()
        spectrum_parser.EXECUTE_FUNCTION(function)

    @staticmethod
    def Save_Function(function_name, a, b, c, operation, cbackwards, precision, save_as_function=True):
        SpectrumFunctionLoader.SpectrumFunctionLoader.save_function(function_name, a, b, c, operation, cbackwards, precision, save_as_function)

    @staticmethod
    def Parse_File(File_Name):
        print(SpectrumFunctionLoader.SpectrumFunctionLoader.parse_file(File_Name))
