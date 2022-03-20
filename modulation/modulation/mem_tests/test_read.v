module t();
integer i;
reg signed [15:0] memory [0:16]; // 8 bit memory with 16 entries

initial begin
    $display("-----------------------------------------------rdata:");
    $readmemh("memory_hex.txt", memory);
    $display(memory[0]);
    $display(memory[1]);
    $display(memory[2]);
    $display(memory[16]);
end
endmodule

