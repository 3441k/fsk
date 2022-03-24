import math
import random
from textwrap import dedent
from gen_sin_wave import generate_sine_samples


class GenVerilog:
    def __init__(self, sin_samples=[]):
        
        self.samples = sin_samples
        
        samples_count = len(self.samples)
        self.samples_bit_count = math.ceil(math.log2(samples_count))

        samples_max_value = max(self.samples, key=abs)
        self.samples_max_value_count = math.ceil(math.log2(samples_max_value + 1)) # +1 for sign bit
        
        self.verilog_template = self.gen_verilog_template()
        self.verilog_tb_template = self.gen_verilog_tb_template()
        
        self.case_statements = self.gen_cases()
        self.tb_cases = self.gen_tb_cases()
        
        self.final_verilog_code = self.gen_verilog_code()
        self.final_verilog_tb_code = self.gen_verilog_tb_code()
        
        
    
    def gen_cases(self):
        case_statement_space_count = 12
        i_max_len = max(len(str(len(self.samples))), len("default"))
        case_statements = ""
        
        for i, sample in enumerate(self.samples):
            case_statements += f"{' ' * case_statement_space_count}{i}:{' ' * (i_max_len - len(str(i)) + 1)}out = {sample}\n"
        
        case_statements += f"{' ' * case_statement_space_count}default:{' ' * (i_max_len - len('default') + 1)}out = 0\n"
        
        return case_statements.lstrip()
        
    
    def gen_tb_cases(self):
        # .format(samples_bit_count=self.samples_bit_count, samples_max_value_count=self.samples_max_value_count)
        case_space_count = 8
        number_of_cases = 5
        start_time = 2
        time_step = 2
        cases = ""
        number_of_cases = min(number_of_cases, len(self.samples))

        for i in random.sample(range(len(self.samples)), number_of_cases):
            cases += f"{' ' * case_space_count}#{start_time} i = {i}\n"
            start_time += time_step
            
        return cases.lstrip()
        
    
    def gen_verilog_code(self):
        return self.verilog_template.format(samples_bit_count=self.samples_bit_count, 
                                            samples_max_value_count=self.samples_max_value_count,
                                            case_statements=self.case_statements)

    def gen_verilog_tb_code(self):
        return self.verilog_tb_template.format(samples_bit_count=self.samples_bit_count, 
                                            samples_max_value_count=self.samples_max_value_count,
                                            cases=self.tb_cases)

    def get_verilog_code(self):
        return self.final_verilog_code

    
    def get_verilog_tb_code(self):
        return self.final_verilog_tb_code

    
    def save_into_file(self, verilog_file_name="sin_samples_gen.v"):
        if not verilog_file_name.strip().endswith('.v'):
            verilog_file_name += ".v"
        
        with open(verilog_file_name, "w") as VF:
            VF.write(self.final_verilog_code)
        

    def save_tb_into_file(self, verilog_file_name="tb_sin_samples_gen.v"):
        if not verilog_file_name.strip().endswith('.v'):
            verilog_file_name += ".v"
        
        with open(verilog_file_name, "w") as VF:
            VF.write(self.final_verilog_tb_code)
        

    @staticmethod
    def gen_verilog_template():
        return dedent("""
        module sin_wave_sample_gen(i, out);

            input [{samples_bit_count}:0] i;
            output reg [{samples_max_value_count}:0] out;
            
            always @(i) begin
                case(i)
                    {case_statements}
                endcase
            end
        endmodule
        """).lstrip()

    @staticmethod
    def gen_verilog_tb_template():
        return dedent("""
        module tb_sin_wave_sample_gen();

            reg [{samples_bit_count}:0] i;
            wire [{samples_max_value_count}:0] out;
            
            sin_wave_sample_gen u1(.i(i), .out(out));
            
            initial begin
                i = 0;
                {cases}
            end
            
        endmodule
        """).lstrip()


    

if __name__ == '__main__':
    samples = generate_sine_samples()
    generated_verilog = GenVerilog(sin_samples=samples)
    # print(generated_verilog.gen_verilog_code())
    generated_verilog.save_into_file()
    # print(generated_verilog.gen_verilog_tb_code())
    generated_verilog.save_tb_into_file()