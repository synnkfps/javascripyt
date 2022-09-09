import replacer 

javascript = '''
import random
// generating a random number
const a = random.random() * (10-1) + 1
console.log(`Random value between 1 and 10 is ${a}`);
'''

replacer.target = javascript

d = {
    'console.log' : 'print',
    'function' : 'def',
    #'//' : '#',
    #';' : '',
    'parseInt': 'int',
    'const ' : '',
    'let ' : '',
    'var ' : '',
    'prompt': 'input'
}

# Basic Replacing
replacer.translate('console.log', 'print')
for i in d:
    replacer.translate(i, d[i])

javascript = replacer.target

def replace_string(target, index, new):
    temp = []
    for i in target:
        temp.append(i)
    temp[index] = new 
    return ''.join(temp)

transpiled = ''''''

for line in javascript.splitlines():
    if 'Math' in line:
        if 'Math.random' in line:
            pass
        else:
            transpiled += 'import math\n'
            line = line.replace('Math', 'math')

    if '`' in line and ('(' in line or ')' in line):
        line = line.replace('`', '\'')
    
    if '${' in line:
        if line.split('${')[0].split('\'')[0][-1] == 'f':
            print('Match F-String') 
        else:
            line = line.split('\'')[0] + 'f'+ ''.join(line).replace(line.split('\'')[0], '')
        line = line.replace('${', '{')

    if line.lstrip().startswith('//'):
        line = line.replace('//', '#')
    
    if line.endswith('{') and line.replace(' ', '')[-2] == ')':
        line = line.replace('{', ':')

    if line.lstrip().startswith('}') and line.rstrip().endswith('}'):
        line = line.replace('}', '')
    
    if line.endswith(';'):
        line = line.replace(';', '')
    
    line += '\n'

    transpiled += line 

print(transpiled)
#exec(transpiled)
