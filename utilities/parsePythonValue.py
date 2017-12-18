# parsePythonValue.py
#
# Copyright, 2006, by Paul McGuire
#
# -*- coding: utf-8 -*-

from pyparsing import *

cvtInt = lambda toks: int(toks[0])
cvtReal = lambda toks: float(toks[0])
cvtTuple = lambda toks: tuple(toks.asList())
cvtDict = lambda toks: dict(toks.asList())

# define punctuation as suppressed literals
lparen, rparen, lbrack, rbrack, lbrace, rbrace, colon, phi = \
    map(Suppress, "()[]{}:∅")

integer = Combine(Optional(oneOf("+ -")) + Word(nums)) \
    .setName("integer") \
    .setParseAction(cvtInt)
real = Combine(Optional(oneOf("+ -")) + Word(nums) + "." +
               Optional(Word(nums)) +
               Optional(oneOf("e E") + Optional(oneOf("+ -")) + Word(nums))) \
    .setName("real") \
    .setParseAction(cvtReal)
tupleStr = Forward()
listStr = Forward()
dictStr = Forward()

listItem = real | integer | quotedString.setParseAction(removeQuotes) | \
           Group(listStr) | tupleStr | dictStr

tupleStr << (Suppress("(") + Optional(delimitedList(listItem)) +
             Optional(Suppress(",")) + Suppress(")"))
tupleStr.setParseAction(cvtTuple)

listStr << (lbrack + Optional(delimitedList(listItem) +
                              Optional(Suppress(","))) + rbrack)

dictEntry = Group(listItem + colon + listItem)
dictStr << (lbrace + Optional(delimitedList(dictEntry) + \
                              Optional(Suppress(","))) + rbrace)
dictStr.setParseAction(cvtDict)
