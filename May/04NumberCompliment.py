'''
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
'''

# Solution::::::::::::::::::::::
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