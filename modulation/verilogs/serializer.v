`timescale 1ns/1ns
module serializer(clk, load, data, rst, Ren, out);

    parameter DATA_SIZE = 32;
	
	input clk, load, rst;
	input [DATA_SIZE-1:0] data;
	
	reg [DATA_SIZE-1:0] acc;
	
	output out, Ren;

	integer i;
	
	initial begin
		i = 0;
	end
	
    always @(posedge clk)
    begin
        if(rst)
			begin
				Ren = 1'b1;
				out = 1'b0;
				i = 0;
			end
		else if(Ren and load)
		    begin
				i = 0;
				Ren	= 1'b0;
				acc = data;
			end
		else if (i==DATA_SIZE)
			begin
				Ren = 1'b1;
				out = 1'bx;
			end
		else if (i<DATA_SIZE)
			begin
				out = acc[0];
				acc >> 1;
				i = i + 1;
			end
    end

endmodule
