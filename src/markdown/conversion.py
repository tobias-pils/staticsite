import os
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
                children = [TextNode(block[4:-4], TextType.CODE).to_html_node()]
                html_nodes.append(ParentNode("pre", children))
            case BlockType.QUOTE:
                text = "\n".join(map(lambda l: l[1:].strip(), block.split("\n")))
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
    return ParentNode("div", html_nodes)

def text_to_html_nodes(block):
    return list(map(TextNode.to_html_node, text_to_textnodes(block)))

def get_list_items(block):
    children = []
    for line in block.split("\n"):
        num_len = line.find(" ") + 1
        line_children = text_to_html_nodes(line[num_len:])
        children.append(ParentNode("li", line_children))
    return children

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[1:].strip()
    raise Exception("Markdown does not contain a title")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if not os.path.exists(from_path):
        raise Exception(f"'From' file {from_path} does not exist")

    if os.path.isdir(from_path):
        raise Exception(f"{from_path} is not a file")

    if not os.path.exists(template_path):
        raise Exception(f"'Template' file {template_path} does not exist")

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(from_path, encoding="utf-8") as from_file:
        markdown = from_file.read()
    with open(template_path, encoding="utf-8") as template_file:
        template = template_file.read()
    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    with open(dest_path, "w") as dest_file:
        dest_file.write(html)
