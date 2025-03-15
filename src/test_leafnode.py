import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("div", "I am a rectangle", {"width": "32px", "height": "42px"})
        self.assertEqual(node.to_html(), '<div width="32px" height="42px">I am a rectangle</div>')

    def test_leaf_to_html_only_value(self):
        node = LeafNode(None, "I have value!")
        self.assertEqual(node.to_html(), "I have value!")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("span", None)
        self.assertRaises(ValueError, node.to_html)

if __name__ == "__main__":
   unittest.main()
