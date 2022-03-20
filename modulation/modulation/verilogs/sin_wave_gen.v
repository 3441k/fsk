`timescale 1ns/1ns
module sinus_gen(
    input clk ,
    output reg signed [15:0] sinus
    );

    parameter SIZE = 1024;    

    reg [15:0] rom_memory [SIZE-1:0];
    integer i;

    initial begin
        $readmemh("sine.mem", rom_memory); //File with the signal
        i = 0;
    end    
    //At every positive edge of the clock, output a sine wave sample.

    always@(posedge clk)
    begin
        sinus = rom_memory[i];
        $display(sinus);
        i = i+ 1;
        if(i == SIZE) i = 0;
    end

endmodule
