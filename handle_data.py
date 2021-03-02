import pickle, utils
from build_tree import init


def export(text_name):
    root = init(text_name)
    with open('data_tree.pkl', 'wb') as handle:
        pickle.dump(root, handle, protocol=pickle.HIGHEST_PROTOCOL)


def import_tree():
    with open('data_tree.pkl', 'rb') as handle:
        tree = pickle.load(handle)
        return tree


if __name__=='__main__':
    export('text.txt')
    tree = import_tree()
    utils.print_dict(tree)
    # print(tree)