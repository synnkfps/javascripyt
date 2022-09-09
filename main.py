import replacer 

javascript = '''
function hi(){
    // Print `Hello World`
    console.log(`Hello, World!`);
}
hi();
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
    if '(`' in line: line = line.replace('(`', '(\'')
    if '`)' in line: line = line.replace('`)', '\')')

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
# exec(transpiled)
