import unittest
from .blockmarkdown import BlockType, block_to_block_type, markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
# This is a heading

# And another heading

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "# And another heading",
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading1(self):
        block = "# this is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_heading2(self):
        block = "## this is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_heading3(self):
        block = "### this is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_heading4(self):
        block = "#### this is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_heading5(self):
        block = "##### this is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_heading6(self):
        block = "###### this is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_heading7(self):
        block = "####### this is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_code_one_line(self):
        block = """```
this is a line of code
```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_type_code_multiple_lines(self):
        block = """```
def this_is_a_line_of_code():
    while True:
        return True
```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_type_code_end_missing(self):
        block = """```
def this_is_a_line_of_code():
    while True:
        return True
"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_quote_one_line(self):
        block = "> this is a short quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_to_block_type_quote_multiple_lines(self):
        block = """> this is a longer quote
> over multiple
> lines"""
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_to_block_type_quote_missing_line_start(self):
        block = """> this is a longer quote
 over multiple
> lines"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list_one_line(self):
        block = "- this is a short list"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_unordered_list_multiple_lines(self):
        block = """- this is a longer list
- over multiple
- lines"""
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_unordered_list_space_missing(self):
        block = "-this is a short list"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list_missing_line_start(self):
        block = """- this is a longer list
 over multiple
- lines"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list_one_line(self):
        block = "1. this is a short list"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_block_to_block_type_ordered_list_multiple_lines(self):
        block = """1. this is a longer list
2. over multiple
3. lines"""
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_block_to_block_type_ordered_list_space_missing(self):
        block = "1.this is a short list"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list_dot_missing(self):
        block = "1 this is a short list"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list_missing_line_start(self):
        block = """1. this is a longer list
 over multiple
2. lines"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list_broken_sequence(self):
        block = """1. this is a longer list
2. over multiple
4. lines"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
