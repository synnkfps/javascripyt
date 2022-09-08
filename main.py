import replacer 

javascript = '''
// store input numbers
const num1 = parseInt(prompt('Enter the first number '));
const num2 = parseInt(prompt('Enter the second number '));

//add two numbers
const sum = num1 + num2;

// display the sum
console.log(`The sum of ${num1} and ${num2} is ${sum}`);
'''

replacer.target = javascript

d = {
    '`' : '\'',
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

print(replacer.target)

#exec(javascript)