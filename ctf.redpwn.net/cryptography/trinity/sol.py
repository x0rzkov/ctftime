code = '1202010210201201021011200200021121112010202012010210102012102021000200121200210002021210112111200121200002111200121102000021211120010200212001020020102000212'

mapping = {'0': '.', '1': '-', '2': ' '}

morse = ''
for c in code:
	morse += mapping[c]

print morse