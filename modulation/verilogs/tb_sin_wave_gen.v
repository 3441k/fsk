`timescale 1ns/1ns
`include "sin_wave_gen.v"
module tb();

    reg clk;
    wire [15:0] sin_out;

    sinus_gen sin_wave(.clk(clk), .sinus(sin_out));
    always #2 clk=~clk;

    initial
	begin
   	    clk = 1'b0;
	    #3000 $finish;
	end

endmodule

