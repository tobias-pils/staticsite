from nodes.textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        text_parts = old_node.text.split(delimiter)
        for i in range(len(text_parts)):
            if i % 2 != 0:
                if i != len(text_parts) - 1:
                    new_nodes.append(TextNode(text_parts[i], text_type))
                else:
                    new_nodes[-1].text += delimiter + text_parts[i]
            elif text_parts[i] != "":
                new_nodes.append(TextNode(text_parts[i], TextType.NORMAL))
    return new_nodes

def extract_markdown_images(old_nodes):
    return split_nodes_regex(old_nodes, r"!\[(?P<text>.*?)\]\((?P<url>.+?)\)", TextType.IMAGE)

def extract_markdown_links(old_nodes):
    return split_nodes_regex(old_nodes, r"(?P<prefix>[^!]|^)\[(?P<text>.*?)\]\((?P<url>.+?)\)", TextType.LINK)

def split_nodes_regex(old_nodes, pattern, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        matches = re.finditer(pattern, text)
        for match in matches:
            prefix_length = 0 if "prefix" not in match.groupdict() else len(match["prefix"])
            pos = text.find(match[0])
            if text[:pos + prefix_length] != "":
                new_nodes.append(TextNode(text[:pos + prefix_length], TextType.NORMAL))
            new_nodes.append(TextNode(match["text"], text_type, match["url"]))
            text = text[pos + len(match[0]):]
        if text != "":
            new_nodes.append(TextNode(text, TextType.NORMAL))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    nodes = extract_markdown_images(nodes)
    nodes = extract_markdown_links(nodes)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    return nodes
