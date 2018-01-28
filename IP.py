# -*- coding: utf-8 -*-     
import sys
import socket
import struct
import itertools

def Tips():
	print("warining:too small argv")
	print("Simple: IP.py 127.0.0.1")

#纯8进制
def ip_split_by_comma_oct(ip):
	"""
	set函数是一个无序不重复的元素集，用于关系测试和去重
	print ip_split_oct -> ['0177', '0', '0', '01']
	print parsed_result -> set(['0177.0.0.01'])
	"""
	parsed_result = set()
	ip_split = str(ip).split('.')
	ip_split_oct = [oct(int(_)) for _ in ip_split]
	parsed_result.add('.'.join(ip_split_oct))
	return parsed_result
	
#纯16进制
def ip_split_by_comma_hex(ip):
	"""
	print ip_split_hex -> ['0x7f', '0x0', '0x0', '0x1']
	print parsed_result -> set(['0x7f.0x0.0x0.0x1'])
	"""
	parsed_result = set()
	ip_split = str(ip).split('.')
	ip_split_hex = [hex(int(_)) for _ in ip_split]
	parsed_result.add('.'.join(ip_split_hex))
	return parsed_result

#10进制，8进制
def combination_oct_int_ip(ip):
	"""
	itertools.combinations(iterable,r)
	创建一个迭代器，返回iterable中长度为r的序列。
	print oct_2 -> [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
	print oct_3 -> [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
	enumerate用来枚举函数
	tuple表示元组
	"""
	result = set()
	parsed_result = set()
	ip_split = str(ip).split('.')
	oct_2 = list(itertools.combinations([0, 1, 2, 3], 2))
	oct_3 = list(itertools.combinations([0, 1, 2, 3], 3))
	#变化ip的一段
	for n, _ in enumerate(ip_split):
		_tmp = oct(int(_))
		#ip_split[:n] -> []读取前面的数  ip_split[n+1:]-> ['0', '0', '1']读取后面的数
		_delete = ip_split[:n] + ip_split[n+1:]
		_delete.insert(n, _tmp)
		result.add(tuple(_delete))
	#变化ip的两段
	for _ in oct_2:
		_tmp_ip = ip_split[:]
		_tmp1 = oct(int(ip_split[_[0]]))
		_tmp2 = oct(int(ip_split[_[1]]))
		del _tmp_ip[_[0]]
		del _tmp_ip[_[1]-1]
		_tmp_ip.insert(_[0], _tmp1)
		_tmp_ip.insert(_[1], _tmp2)
		result.add(tuple(_tmp_ip))
	#变化ip的三段
	for _ in oct_3:
		_tmp_ip = ip_split[:]
		_tmp1 = oct(int(ip_split[_[0]]))
		_tmp2 = oct(int(ip_split[_[1]]))
		_tmp3 = oct(int(ip_split[_[2]]))
		del _tmp_ip[_[0]]
		del _tmp_ip[_[1] - 1]
		del _tmp_ip[_[2] - 2]
		_tmp_ip.insert(_[0], _tmp1)
		_tmp_ip.insert(_[1], _tmp2)
		_tmp_ip.insert(_[2], _tmp3)
		result.add(tuple(_tmp_ip))
	for _ in result:
		parsed_result.add('.'.join(_))
	return parsed_result
	
#16进制，10进制
def combination_hex_int_ip(ip):
    """
    :param ip:
    :return:
    """
    result = set()
    parsed_result = set()
    ip_split = str(ip).split('.')
    hex_2 = list(itertools.combinations([0, 1, 2, 3], 2))
    hex_3 = list(itertools.combinations([0, 1, 2, 3], 3))
    for n, _ in enumerate(ip_split):
        _tmp = hex(int(_))
        _delete = ip_split[:n] + ip_split[n+1:]
        _delete.insert(n, _tmp)
        result.add(tuple(_delete))
    for _ in hex_2:
        _tmp_ip = ip_split[:]
        _tmp1 = hex(int(ip_split[_[0]]))
        _tmp2 = hex(int(ip_split[_[1]]))
        del _tmp_ip[_[0]]
        del _tmp_ip[_[1] - 1]
        _tmp_ip.insert(_[0], _tmp1)
        _tmp_ip.insert(_[1], _tmp2)
        result.add(tuple(_tmp_ip))
    for _ in hex_3:
        _tmp_ip = ip_split[:]
        _tmp1 = hex(int(ip_split[_[0]]))
        _tmp2 = hex(int(ip_split[_[1]]))
        _tmp3 = hex(int(ip_split[_[2]]))
        del _tmp_ip[_[0]]
        del _tmp_ip[_[1] - 1]
        del _tmp_ip[_[2] - 2]
        _tmp_ip.insert(_[0], _tmp1)
        _tmp_ip.insert(_[1], _tmp2)
        _tmp_ip.insert(_[2], _tmp3)
        result.add(tuple(_tmp_ip))
    for _ in result:
        parsed_result.add('.'.join(_))
    return parsed_result
	
#10进制，16进制，8进制
def combination_hex_int_oct_ip(ip):
	"""
	:param ip:
	:return:
	"""
	result = set()
	parsed_result = set()
	ip_split = str(ip).split('.')
	hex_3 = list(itertools.combinations([0, 1, 2, 3], 3))
	for n1, n2, n3 in hex_3:
		_tmp_ip = ip_split[:]
		_tmp_2 = oct(int(_tmp_ip[n2]))
		_tmp_3 = hex(int(_tmp_ip[n3]))
		del _tmp_ip[n2]
		del _tmp_ip[n3 - 1]
		_tmp_ip.insert(n2, _tmp_2)
		_tmp_ip.insert(n3, _tmp_3)
		result.add(tuple(_tmp_ip))
	for _ in result:
		parsed_result.add('.'.join(_))
	return parsed_result
	
'''
socket.inet_aton() 把IPV4地址转化为32位打包的二进制格式 -> 检查是否为ipv4
struct.unpack(fmt,string) 按照给定的格式(fmt)解析字节流string，返回解析出来的tuple
!L: ! = network(=big-endian)  L = unsigned long
'''
if __name__ == '__main__':
	if len(sys.argv)==2:
		ip = sys.argv[1]
		ip_int = struct.unpack('!L', socket.inet_aton(ip))[0]
		ip_oct_no_comma = oct(ip_int)
		ip_hex_no_comma = hex(ip_int)
		ip_oct_by_comma = ip_split_by_comma_oct(ip)
		ip_hex_by_comma = ip_split_by_comma_hex(ip)
		all_result = ip_oct_by_comma | ip_hex_by_comma | combination_oct_int_ip(ip) | combination_hex_int_ip(ip) | combination_hex_int_oct_ip(ip)
		print ip_int
		print ip_oct_no_comma
		print ip_hex_no_comma
		for _ip in all_result:
			print _ip
	else:
		Tips()		
		