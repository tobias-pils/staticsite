from .inlinemarkdown import text_to_textnodes
from .blockmarkdown import BlockType, block_to_block_type, markdown_to_blocks
from nodes.parentnode import ParentNode
from nodes.textnode import TextNode, TextType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        type = block_to_block_type(block)
        match type:
            case BlockType.PARAGRAPH:
                children = text_to_html_nodes(block)
                html_nodes.append(ParentNode("p", children))
            case BlockType.HEADING:
                level = block.find(" ")
                children = text_to_html_nodes(block[level + 1:])
                html_nodes.append(ParentNode(f"h{level}", children))
            case BlockType.CODE:
                children = [TextNode(block[3:-3], TextType.CODE).to_html_node()]
                html_nodes.append(ParentNode("pre", children))
            case BlockType.QUOTE:
                text = "\n".join(map(lambda l: l[1:], block.split("\n")))
                children = text_to_html_nodes(text)
                html_nodes.append(ParentNode("blockquote", children))
            case BlockType.UNORDERED_LIST:
                children = get_list_items(block)
                html_nodes.append(ParentNode("ul", children))
            case BlockType.ORDERED_LIST:
                children = get_list_items(block)
                html_nodes.append(ParentNode("ol", children))
            case _:
                raise ValueError("Markdown block type not supported")
    return ParentNode("body", html_nodes)

def text_to_html_nodes(block):
    return list(map(TextNode.to_html_node, text_to_textnodes(block)))

def get_list_items(block):
    children = []
    for line in block.split("\n"):
        num_len = line.find(" ") + 1
        line_children = text_to_html_nodes(line[num_len:])
        children.append(ParentNode("li", line_children))
    return children
