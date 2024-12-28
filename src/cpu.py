from typing import Any
from memory import Memory
from inscodes import *

class Flags:
    def __init__(self):
        self.Z = 0 # ALU Returns Zero Result
        self.C = 0 # ALU Returns > 32-bit Limit "Borrow"
        self.O = 0 # Overflow, Carry-in and Carry-out are opposite
        self.S = 0 # Sign, "Negative"

        self.B = 0 # Busy
        self.T = 0 # Single-step, Trap Flag
        self.I = 0 # Interrupt Disable
        self.E = 0 # Detected Interrupt

    def full(self):
        ps = self.Z << 7 | self.C << 6 | self.O << 5 | self.S << 4 | self.B << 3 | self.T << 2 | self.I << 1 | self.E
        return ps

class CPU:
    def __init__(self):
        self.PC = 0 # Program Counter Register
        self.PS = Flags()

        # Registers
        self.EAX = 0 # Extended (32-bit) General Purpose Register A
        self.EBX = 0
        self.ECX = 0
        self.EDX = 0

        self.EDI = 0 # Destionation Index
        self.ESI = 0 # Source Index
        self.ESP = 0 # Stack Pointer
        self.EBP = 0 # Address Offset

        self.AX = 0 # (16-bit) General Purpose
        self.BX = 0
        self.CX = 0
        self.DX = 0
        self.BAX = 0 # Byte (8-bit), X (General Purpose)
        self.BBX = 0
        self.BCX = 0
        self.BDX = 0

        self.Memory = Memory().Data
        self.Buffer = len(self.Memory)
        self.Debug = False
        self.Cycles = 0
        self.InInterrupt = False

    def LoadMemory(self, memory: Memory) -> None:
        self.Memory = memory.Data
        self.Buffer = len(self.Memory)

    def __WriteReg(self, code: int, value: int) -> None:
        if code == Code_EAX:
                self.EAX = value

        elif code == Code_EBX:
                self.EBX = value

        elif code == Code_ECX:
                self.ECX = value

        elif code == Code_EDX:
                self.EDX = value

        self.Cycles -= 1

    def __FetchByte(self) -> int:
        value = self.Memory[self.PC]
        self.PC += 1
        self.Cycles -= 1

        return value
    
    def __FetchWord(self) -> int:
         return self.__FetchByte() << 8 | self.__FetchByte()
    
    def Execute(self, cycles: int) -> Any:
        self.Cycles = cycles
        
        while (self.Cycles > 0):
            ins = self.__FetchByte()
            
            if ins == NOP:
                pass

            elif ins == HLT:
                return
            
            elif ins == MOV:
                mod = self.__FetchByte()

                if mod == Addr_RegIm8:
                    reg = self.__FetchByte()
                    value = self.__FetchByte()
                    self.__WriteReg(reg, value)

                elif mod == Addr_RegIm16:
                    reg = self.__FetchByte()
                    value = self.__FetchWord()
                    self.__WriteReg(reg, value)

            else:
                print(f"InvalidOpcode: {hex(ins)} at address {hex(self.PC-1)}")

        return_value = None

        if self.Debug:
            return_value = cycles - self.Cycles

        return return_value