from memory import Memory
from cpu import CPU
from inscodes import *

def main():
    memory = Memory(size=0xF000F)
    cpu = CPU()
    # cpu.Debug = True

    memory.Data[0x100] = ord("H")
    memory.Data[0x101] = ord("e")
    memory.Data[0x102] = ord("l")
    memory.Data[0x103] = ord("l")
    memory.Data[0x104] = ord("o")
    memory.Data[0x105] = ord(",")
    memory.Data[0x106] = ord(" ")
    memory.Data[0x107] = ord("w")
    memory.Data[0x108] = ord("o")
    memory.Data[0x109] = ord("r")
    memory.Data[0x10A] = ord("l")
    memory.Data[0x10B] = ord("d")
    memory.Data[0x10C] = ord("!")

    memory.Data[0x00] = MOV
    memory.Data[0x01] = Addr_RegIm8
    memory.Data[0x02] = Code_EAX
    memory.Data[0x03] = 4
    memory.Data[0x04] = MOV
    memory.Data[0x05] = Addr_RegIm8
    memory.Data[0x06] = Code_EBX
    memory.Data[0x07] = 1
    memory.Data[0x08] = MOV
    memory.Data[0x09] = Addr_RegIm16
    memory.Data[0x0A] = Code_ECX
    memory.Data[0x0B] = 0x01
    memory.Data[0x0C] = 0x00
    memory.Data[0x0D] = MOV
    memory.Data[0x0E] = Addr_RegIm8
    memory.Data[0x0F] = Code_EDX
    memory.Data[0x10] = 13

    memory.Data[0x11] = INT
    memory.Data[0x12] = 0X80

    cpu.LoadMemory(memory)
    cycles = cpu.Execute(21 + 2 + 13)
    # print(cycles)
    print()


if __name__ == "__main__":
    main()