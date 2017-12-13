import pprint

from pyparsing import Word
from string import ascii_lowercase


def myParser():
    stuff = [
                ['Link-Flooded', '(', ['T'], ['L'], ')'],
                '->',
                ['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O1'],
                ';',
                'IF',
                'O1', 'THEN', [['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O2'], '||', ['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O3']], 'ELSE IF', 'O1', 'THEN', [['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O4'], '||', ['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O5']], 'ELSE IF', 'O1', 'THEN', [['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O6'], '||', ['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O7']], 'ELSE', [[['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O8'], '||', ['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O9']], ';', ['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O10']]]

    stuff.insert(0, stuff[:])
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(stuff)

[
    ['Link-Flooded', '(', ['T'], ['L'], ')'],
    '->',
    [
        [
            ['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O1'],
            ';',
            'IF', 'O1', 'THEN', [['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O2'], '||', ['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O3']], 'ELSE IF', 'O1', 'THEN', [['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O4'], '||', ['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O5']], 'ELSE IF', 'O1', 'THEN', [['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O6'], '||', ['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O7']], 'ELSE', [[['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O8'], '||', ['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O9']], ';', ['DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY', ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT', 'OUTCOME', 'O10']]]]]



if __name__ == '__main__':
    myParser()
