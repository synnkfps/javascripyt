import replacer 

javascript = '''
function hi() {
    // Print `Hello World`
    console.log(`Hello, World!`)
}
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

for line in javascript.splitlines():
    line = line.rstrip()

    if '`' in line and (line[line.index('`')-1] == '(' or line[line.index('`')-1] == ')'):
        javascript = javascript.replace(line, line.replace('`', '\''))
    if line.lstrip().startswith('//'):
        javascript = javascript.replace(line, line.replace('//', '#'))
    
    if line.endswith('){'):
        javascript = javascript.replace(line, line.replace('{', ':'))

    if line.endswith(') {'):
        javascript = javascript.replace(line, line.replace(' {', ':'))

    if line.endswith('}'):
        javascript = javascript.replace(line, line.replace('}', ''))
        
print(javascript)
#exec(javascript)
