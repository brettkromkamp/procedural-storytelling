from typedtree.tree import Tree  # type: ignore

topics_file = open("/home/brettk/Source/procedural-storytelling/worldbuilding/topics.dat", "r")

SPACE = " "
TAB = "\t"
SPACES_PER_TAB = 4

stack = {}
tree = Tree()

for line in topics_file:
    index = int(line.count(SPACE) / SPACES_PER_TAB)
    topic_identifier = line.strip()
    stack[index] = topic_identifier

    if index == 0:  # Root node
        tree.add_node(topic_identifier, node_type='identifier', edge_type='relationship')
    else:
        tree.add_node(topic_identifier, parent_pointer=stack[index -1], node_type='identifier', edge_type='relationship')

tree.display(stack[0])
print(tree['worldbuilding'].children)
print(tree['cosmology'].parent)