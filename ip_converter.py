class Ip_Converter:
    
    def __init__(self) -> None:
        pass

    def dd_to_bin(self, dotted_decimal_tuple: tuple):
        """
        Converts a dotted decimal into a binary string.

        Args:
            dotted_decimal_tuple (tuple): a tuple of integers in the range
                [0, 256).

        Returns:
            str: converted string in binary form, zero padded in blocks of 
                bytes.
        """
        if not dotted_decimal_tuple:
            return
        result = ""
        for decimal in dotted_decimal_tuple:
            binary_rep = format(decimal, "08b")
            result += binary_rep
            result += " "
        return result[:-1]

    def bin_to_dd(self, binary_str: str, tuple_format: bool=False):
        """
        Converts a string of binary characters into a dotted decimal string.
        The string of binary characters must be zero-padded, in blocks of bytes,
        e.g. 192.168.1.1 = "11000000 101010000 00000001 00000001".

        Args:
            binary_str (str): the string of binary characters to convert
            tuple_format (bool): if set, returns the result as a tuple of 
                integers.
        """
        if not binary_str:
            return
        bin_bytes = binary_str.split()
        dec_bytes = []
        result_string = ""
        for bin_byte in bin_bytes:
            bin_byte = "0b" + bin_byte
            dec_bytes.append(int(bin_byte, 2))
        if tuple_format:
            return tuple(dec_bytes)
        for dec in dec_bytes:
            result_string += str(dec) + "."
        return result_string[:-1]

def main():
    converter = Ip_Converter()
    dd = (1, 1, 1, 1)
    binary = "00001010 11111111 00000001 00000000"
    print(f"Convert {dd} to binary:")
    print(converter.dd_to_bin(dd))
    print(f"Convert {binary} to dotted decimal")
    print(converter.bin_to_dd(binary))

if __name__ == "__main__":
    main()