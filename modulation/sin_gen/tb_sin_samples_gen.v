module tb_sin_wave_sample_gen();

    reg [10:0] i;
    wire [15:0] out;

    sin_wave_sample_gen u1(.i(i), .out(out));

    initial begin
        i = 0;
        #2 i = 594
        #4 i = 836
        #6 i = 812
        #8 i = 148
        #10 i = 85

    end

endmodule
