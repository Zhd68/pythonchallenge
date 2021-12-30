coding_information = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

#way1

coding = '''abcdefghijklmnopqrstuvwxyz',.() '''
decoding = '''cdefghijklmnopqrstuvwxyzab',.() '''
decoding_dict = dict(zip(coding, decoding))
decoding_information = ''.join(decoding_dict[lit] for lit in coding_information)
print(decoding_information)

coding_result = 'map'
decoding_result = ''.join(decoding_dict[lit] for lit in coding_result)
print(decoding_result)

#way2

print(coding_information.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')))
print(coding_result.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')))