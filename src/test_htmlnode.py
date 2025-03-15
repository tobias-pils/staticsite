import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_no_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_one_prop(self):
        node = HTMLNode(props={"href": "https://www.example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com"')

    def test_props_to_html_two_props(self):
        node = HTMLNode(props={"width": "32px", "height": "42px"})
        self.assertEqual(node.props_to_html(), ' width="32px" height="42px"')

    def test_props_to_html_other_params(self):
        node = HTMLNode("div", "some value", [], {"width": "32px", "height": "42px"})
        self.assertEqual(node.props_to_html(), ' width="32px" height="42px"')

if __name__ == "__main__":
    unittest.main()
