import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_to_html_no_children(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_parent_to_html_leaf_children(self):
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent_to_html_mixed_children(self):
        node = ParentNode("div", [
            ParentNode("span", [
                ParentNode("p", children=[
                    LeafNode(None, "Normal text"),
                    LeafNode("b", "Bold text"),
                ]),
            ]),
            ParentNode("p", children=[
                LeafNode(None, "Normal text"),
            ]),
        ])
        self.assertEqual(node.to_html(), "<div><span><p>Normal text<b>Bold text</b></p></span><p>Normal text</p></div>")

    def test_parent_to_html_with_props(self):
        node = ParentNode("div", [
            ParentNode("a", [
                LeafNode(None, "Normal text"),
            ],
            {"href": "https://www.example.com", "font-size": "35px"}),
        ])
        self.assertEqual(node.to_html(), '<div><a href="https://www.example.com" font-size="35px">Normal text</a></div>')

    def test_parent_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode(None, "Normal text")])
        self.assertRaises(ValueError, node.to_html)

    def test_parent_to_html_children_missing(self):
        node = ParentNode("span", None)
        self.assertRaises(ValueError, node.to_html)

if __name__ == "__main__":
    unittest.main()
