from node import *
from source import *
import utils


def init(file_path):
    root = create_tree(file_path)
    source = Source(file_path, 0, 0)
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if not line.isspace():
                fixed_line = utils.fix_sentence(line)
                add_sentence(root, fixed_line, source.copy_inc_line(i))
    return root


def create_tree(file_path):
    s = Source(file_path, 0, 0)
    return Node("1", None, s)


def add_sentence(node, sentence, source):
    root = node
    for i in range(len(sentence)):
        depth = min(i + 20, len(sentence))
        for j in range(i, depth):
            node = node.add_son(sentence[j], source.copy_inc_offset(j))
        node = root
