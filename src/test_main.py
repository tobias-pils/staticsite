import unittest
from htmlnode import HTMLNode
from main import text_node_to_html_node
from textnode import TextNode, TextType

class TestMain(unittest.TestCase):
    def test_text_node_to_html_node_normal(self):
        text_node = TextNode("normal text", TextType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, HTMLNode)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "normal text")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, HTMLNode)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold text")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, HTMLNode)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "italic text")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("code text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, HTMLNode)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "code text")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("link text", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, HTMLNode)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "link text")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, {"href": "https://www.example.com"})

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("image alt text", TextType.IMAGE, "https://www.example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, HTMLNode)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, {
            "src": "https://www.example.com/image.png",
            "alt": "image alt text"
        })

    def test_text_node_to_html_node_invalid_type(self):
        text_node = TextNode("normal text", "invalidtype")
        self.assertRaises(ValueError, text_node_to_html_node, text_node)

if __name__ == "__main__":
    unittest.main()
