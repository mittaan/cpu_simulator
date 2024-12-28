from memory import Memory
from cpu import CPU
from inscodes import *

def main():
    memory = Memory()
    cpu = CPU()
    cpu.Debug = True

    memory.Data[0x00] = MOV
    memory.Data[0x01] = Addr_RegIm8
    memory.Data[0x02] = Code_EAX
    memory.Data[0x03] = 42

    cpu.LoadMemory(memory)
    cycles = cpu.Execute(5)
    print(cycles)
    print(cpu.EAX)


if __name__ == "__main__":
    main()