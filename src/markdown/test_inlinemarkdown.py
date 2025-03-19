import unittest
from .inlinemarkdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    text_to_textnodes
)
from nodes.textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        old_nodes = [TextNode("This is text with a `code block` word", TextType.NORMAL)]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
        ])

    def test_split_nodes_delimiter_bold_italic(self):
        old_nodes = [
            TextNode("This is text with a **bold** word", TextType.NORMAL),
            TextNode("This is text with a _italic_ word", TextType.NORMAL),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.NORMAL),
            TextNode("This is text with a _italic_ word", TextType.NORMAL),
        ])
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.NORMAL),
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.NORMAL),
        ])

    def test_split_nodes_delimiter_beginning_end(self):
        old_nodes = [TextNode("_Italic_ word in the beginning, at the end _too_", TextType.NORMAL)]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("Italic", TextType.ITALIC),
            TextNode(" word in the beginning, at the end ", TextType.NORMAL),
            TextNode("too", TextType.ITALIC),
        ])

    def test_split_nodes_delimiter_single_occurance(self):
        old_nodes = [TextNode("There is nothing **bold here", TextType.NORMAL)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("There is nothing **bold here", TextType.NORMAL),
        ])

    def test_extract_markdown_images_simple(self):
        old_nodes = [TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.NORMAL)]
        self.assertListEqual(extract_markdown_images(old_nodes), [
            TextNode("This is text with an ", TextType.NORMAL),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
        ])

    def test_extract_markdown_images_multiple(self):
        old_nodes = [
            TextNode("This is text with multiple images:", TextType.NORMAL),
            TextNode("this ![image](https://i.imgur.com/zjjcJKZ.png) and that ![other image](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.NORMAL)
        ]
        self.assertListEqual(extract_markdown_images(old_nodes), [
            TextNode("This is text with multiple images:", TextType.NORMAL),
            TextNode("this ", TextType.NORMAL),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and that ", TextType.NORMAL),
            TextNode("other image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ])

    def test_extract_markdown_images_no_alt(self):
        old_nodes = [TextNode("This is text with an ![](https://i.imgur.com/zjjcJKZ.png)", TextType.NORMAL)]
        self.assertListEqual(extract_markdown_images(old_nodes), [
            TextNode("This is text with an ", TextType.NORMAL),
            TextNode("", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
        ])

    def test_extract_markdown_images_no_url(self):
        old_nodes = [TextNode("This is text with an ![image]()", TextType.NORMAL)]
        self.assertListEqual(extract_markdown_images(old_nodes), old_nodes)

    def test_extract_markdown_images_link(self):
        old_nodes = [TextNode("This is text with a [link](https://www.example.com)", TextType.NORMAL)]
        self.assertListEqual(extract_markdown_images(old_nodes), old_nodes)

    def test_extract_markdown_links_simple(self):
        old_nodes = [TextNode("This is text with a [link](https://www.example.com)", TextType.NORMAL)]
        self.assertListEqual(extract_markdown_links(old_nodes), [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://www.example.com")
        ])

    def test_extract_markdown_links_multiple(self):
        old_nodes = [
            TextNode("This is text with multiple links:", TextType.NORMAL),
            TextNode("this [link](https://www.example.com) and that [other link](https://www.example.com/home)", TextType.NORMAL),
        ]
        self.assertListEqual(extract_markdown_links(old_nodes), [
            TextNode("This is text with multiple links:", TextType.NORMAL),
            TextNode("this ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://www.example.com"),
            TextNode(" and that ", TextType.NORMAL),
            TextNode("other link", TextType.LINK, "https://www.example.com/home")
        ])

    def test_extract_markdown_links_no_text(self):
        old_nodes = [TextNode("This is text with a [](https://www.example.com)", TextType.NORMAL)]
        self.assertListEqual(extract_markdown_links(old_nodes), [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("", TextType.LINK, "https://www.example.com")
        ])

    def test_extract_markdown_links_no_url(self):
        old_nodes = [TextNode("This is text with a [link]()", TextType.NORMAL)]
        self.assertListEqual(extract_markdown_links(old_nodes), old_nodes)

    def test_extract_markdown_links_beginning(self):
        old_nodes = [TextNode("[link](https://www.example.com) is a link", TextType.NORMAL)]
        self.assertListEqual(extract_markdown_links(old_nodes), [
            TextNode("link", TextType.LINK, "https://www.example.com"),
            TextNode(" is a link", TextType.NORMAL)
        ])

    def test_extract_markdown_links_image(self):
        old_nodes = [TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.NORMAL)]
        self.assertListEqual(extract_markdown_links(old_nodes), old_nodes)

    def test_text_to_textnodes_all_types(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(text_to_textnodes(text), [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

    def test_text_to_textnodes_code_before_bold(self):
        text = "There is nothing **bold** in my `code **block**`"
        self.assertListEqual(text_to_textnodes(text), [
            TextNode("There is nothing ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" in my ", TextType.NORMAL),
            TextNode("code **block**", TextType.CODE),
        ])

    def test_text_to_textnodes_bold_before_italic(self):
        text = "There is nothing _italic_ in my **bold _text_**"
        self.assertListEqual(text_to_textnodes(text), [
            TextNode("There is nothing ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" in my ", TextType.NORMAL),
            TextNode("bold _text_", TextType.BOLD),
        ])

if __name__ == "__main__":
    unittest.main()
