import operator
from pyparsing import Literal, Word, Combine, Optional, ZeroOrMore, Forward, nums, \
    alphas
from collections import defaultdict


def main():
    global exprStack
    exprStack = []
    global varStack
    varStack = []
    global variables
    variables = defaultdict(float)
    l = ['x=1', 'y=abs(2)', 'x+=y']
    for item in l:
        source = item
        L = BNF().parseString(source)
        print(L)
        result = evaluateStack(exprStack[:])
        print(varStack)
        print(result)
        variables[varStack.pop()] = result
        print(variables)


def Scalar(x):
    return x


def pushFirst(strg, loc, toks):
    exprStack.append(toks[0])


def assignVar(strg, loc, toks):
    varStack.append(toks[0])


bnf = None


def BNF():
    """
    expop   :: '^'
    multop  :: '*' | '/'
    addop   :: '+' | '-'
    integer :: ['+' | '-'] '0'..'9'+
    atom    :: real | fn '(' expr ')' | '(' expr ')'
    factor  :: atom [ expop factor ]*
    term    :: factor [ multop factor ]*
    expr    :: term [ addop term ]*
    iaddop  :: '+='
    assign  :: '='
    """
    global bnf
    if not bnf:
        point = Literal(".")
        fnumber = Combine(Word("+-" + nums, nums) +
                          Optional(point + Optional(Word(nums))))
        ident = Word(alphas + "_", alphas + nums + "_")

        plus = Literal("+")
        minus = Literal("-")
        mult = Literal("*")
        div = Literal("/")
        lpar = Literal("(").suppress()
        rpar = Literal(")").suppress()
        addop = plus | minus
        multop = mult | div
        expop = Literal("^")
        assign = Literal("=")
        iaddop = Literal("+=")

        expr = Forward()
        atom = (fnumber | ident + lpar + expr + rpar | ident).setParseAction(pushFirst) | (
        lpar + expr.suppress() + rpar)

        # by defining exponentiation as "atom [ ^ factor ]..." instead of "atom [ ^ atom ]...", we get right-to-left exponents, instead of left-to-righ
        # that is, 2^3^2 = 2^(3^2), not (2^3)^2.
        factor = Forward()
        factor << atom + ZeroOrMore((expop + factor).setParseAction(pushFirst))

        term = factor + ZeroOrMore((multop + factor).setParseAction(pushFirst))
        expr << term + ZeroOrMore((addop + term).setParseAction(pushFirst))
        bnf = ident.setParseAction(assignVar) + (assign | iaddop.setParseAction(pushFirst)) + expr
    return bnf


# map operator symbols to corresponding arithmetic operations
opn = {"+": operator.add,
       "-": operator.sub,
       "*": operator.mul,
       "/": operator.truediv,
       "^": operator.pow,
       "+=": operator.iadd}
fn = {"Max": max,
      "Min": min,
      "abs": abs,
      "Scalar": Scalar}


def evaluateStack(s):
    op = s.pop()
    if op in "+-*/^" or op in '+=':
        op2 = evaluateStack(s)
        op1 = evaluateStack(s)
        return opn[op](op1, op2)
    elif op in fn:
        return fn[op](evaluateStack(s))
    elif op in variables:
        return variables[op]
    else:
        return float(op)


if __name__ == '__main__':
    main()