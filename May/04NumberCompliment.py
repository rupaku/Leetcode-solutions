class Solution:
    def findComplement(self, num: int) -> int:
        bits = '{0:b}'.format(num)
        print('bits',bits)
        complement_bits = ''.join('1' if bit == '0' else '0' for bit in bits)
        return int(complement_bits, 2)
        
#solution2
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 2 ** (len(bin(num)) - 2) - 1 - num