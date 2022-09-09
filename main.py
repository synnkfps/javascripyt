import replacer 

javascript = '''
// program to check if a number is prime or not

// take input from the user
const number = parseInt(prompt("Enter a positive number: "));
let isPrime = true;

// check if number is equal to 1
if (number === 1) {
    console.log("1 is neither prime nor composite number.");
}

// check if number is greater than 1
else if (number > 1) {

    // looping through 2 to number-1
    for (let i = 2; i < number; i++) {
        if (number % i == 0) {
            isPrime = false;
            break;
        }
    }

    if (isPrime) {
        console.log(`${number} is a prime number`);
    } else {
        console.log(`${number} is a not prime number`);
    }
}

// check if number is less than 1
else {
    console.log("The number is not a prime number.");
}
'''

replacer.target = javascript

d = {
    'console.log' : 'print',
    'function' : 'def',
    'else if' : 'elif',
    '===': '==',
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
    if 'true' in line and ('=' in line or '==' in line): line = line.replace('true', 'True')
    if 'false' in line and ('=' in line or '==' in line): line = line.replace('false', 'False')

    if '}' in line.strip() and 'else' in line.strip():
        line = line.replace('} else', 'else')
    if '{' in line.strip() and 'else' in line.strip():
        line = line.replace('else {', 'else') 

    if 'Math' in line:
        transpiled += 'import math\nimport random\n\n'
        line = line.replace('Math', 'math')
        line = line.replace('math.random', 'random.random')

    if '`' in line and ('(' in line or ')' in line):
        line = line.replace('`', '\'')
    
    if '${' in line:
        if line.split('${')[0].split('\'')[0][-1] == 'f':
            print('Match F-String') 
        else:
            line = line.split('\'')[0] + 'f'+ ''.join(line).replace(line.split('\'')[0], '')
        line = line.replace('${', '{')

    if 'else' in line and not line.split('else')[1]:  line = line.replace('else', 'else:')
    if line.lstrip().startswith('//'): line = line.replace('//', '#')
    
    if line.endswith('{') and (line.replace(' ', '')[-2] == ')' or line.replace(' ', '').split('{')[0] == 'else'):
        line = line.replace('{', ':')

    if line.lstrip().startswith('}') and line.rstrip().endswith('}'):
        line = line.replace('}', '')
    
    if line.endswith(';'):
        line = line.replace(';', '')
    
    line += '\n'

    transpiled += line 

print(transpiled)
#exec(transpiled)
