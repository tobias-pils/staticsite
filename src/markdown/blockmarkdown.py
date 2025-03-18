import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    return list(filter(lambda l: l != "", map(str.strip, markdown.split("\n\n"))))

def block_to_block_type(block):
    if re.fullmatch(r"^#{1,6} .*$", block) != None:
        return BlockType.HEADING
    if re.fullmatch(r"^```[\s\S]*```$", block) != None:
        return BlockType.CODE
    if re.fullmatch(r"^>.*(\n>.*)*$", block) != None:
        return BlockType.QUOTE
    if re.fullmatch(r"^- .*(\n- .*)*$", block) != None:
        return BlockType.UNORDERED_LIST
    n = 1
    for line in block.split("\n"):
        if re.fullmatch(f"^{n}" + r"\. .*$", line) == None:
            return BlockType.PARAGRAPH
        n += 1
    return BlockType.ORDERED_LIST
