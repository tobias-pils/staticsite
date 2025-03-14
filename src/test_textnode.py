import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_with_url(self):
        node1 = TextNode("This is a link node", TextType.LINK, "http://localhost:8888")
        node2 = TextNode("This is a link node", TextType.LINK, "http://localhost:8888")
        self.assertEqual(node1, node2)

    def test_neq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a bold text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.BOLD, "http://localhost:8888")
        self.assertNotEqual(node1, node2)
        self.assertNotEqual(node1, node3)
        self.assertNotEqual(node1, node4)

    def test_neq_with_url(self):
        node1 = TextNode("This is a node with url", TextType.LINK, "http://localhost:8888")
        node2 = TextNode("This is a link node", TextType.LINK, "http://localhost:8888")
        node3 = TextNode("This is a node with url", TextType.IMAGE, "http://localhost:8888")
        node4 = TextNode("This is a node with url", TextType.LINK, "http://www.example.com")
        self.assertNotEqual(node1, node2)
        self.assertNotEqual(node1, node3)
        self.assertNotEqual(node1, node4)


if __name__ == "__main__":
    unittest.main()
