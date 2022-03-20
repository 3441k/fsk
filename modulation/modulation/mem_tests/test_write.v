module t();
integer i;
reg signed [15:0] memory [0:16]; // 8 bit memory with 16 entries

initial begin
    for (i=0; i<16; i = i+1) begin
        memory[i] = i-5;
    end
    memory[16] = -202;
    $writememb("memory_binary.txt", memory);
    $writememh("memory_hex.txt", memory);
end
endmodule

