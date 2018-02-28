#!/usr/bin/env python3

import operator
import logging
import sys
import copy

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)

def rotate(stack):
    new_stack = []
    while stack:
        new_stack.append(stack.pop())
    return new_stack

def summation(stack):
    new_stack = copy.deepcopy(stack)
    sum_val = 0
    while new_stack:
        sum_val += new_stack.pop()
    return sum_val

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '&': operator.and_,
    '|': operator.or_,
    '~': operator.inv,
    'r': rotate,
    's': summation,
}
def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            if function == operator.inv:
                stack.append(function(stack.pop()))
            elif function == rotate:
                stack = rotate(stack)
                logger.debug(stack)
                return stack
            elif function == summation:
                stack.append(function(stack))
                logger.debug(stack)
                return stack
            else:
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1, arg2)
                stack.append(result)
        logger.debug(stack)
    if len(stack) != 1:
        raise TypeError
    return stack.pop()
def main():
    while True:
       print(calculate(input('rpn calc> ')))
    
if __name__ == '__main__':
    main()
