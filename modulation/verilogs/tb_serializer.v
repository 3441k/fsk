`timescale 1ns/1ns
`include "serializer.v"
module tb();

    reg clk, load, rst;
    reg [31:0] data;
    wire Ren, out;

    serializer serial(.clk(clk), .load(load), .rst(rst), .data(data), .Ren(Ren), .out(out));
    always #1 clk=~clk;

    initial
	begin
   	    clk = 1'b0;
        rst = 1'b1;
        
        #2
         load = 1'b1;
         rst = 1'b0;
         data = 32'b01100101110110010110101101100110;       
        
        #40
         data = 32'b00000000000111111111111111111100;
        
        #30
         load = 1'b1;
         rst = 1'b0;
	    #20 $finish;
	end

endmodule

