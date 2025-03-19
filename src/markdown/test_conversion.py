import unittest
from .conversion import markdown_to_html_node

class TestConversion(unittest.TestCase):
    def test_markdown_to_html_node_paragraph(self):
        md = "Hello world!"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<body><p>Hello world!</p></body>"
        )

    def test_markdown_to_html_node_paragraph_children(self):
        md = "**Hello** _world!_"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<body><p><b>Hello</b> <i>world!</i></p></body>"
        )

    def test_markdown_to_html_node_heading1(self):
        md = "# Hello world!"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<body><h1>Hello world!</h1></body>"
        )

    def test_markdown_to_html_node_heading6(self):
        md = "###### Hello world!"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<body><h6>Hello world!</h6></body>"
        )

    def test_markdown_to_html_node_heading7_paragraph(self):
        md = "####### Hello world!"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<body><p>####### Hello world!</p></body>"
        )

    def test_markdown_to_html_node_heading3_children(self):
        md = "### **Hello** _world!_"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<body><h3><b>Hello</b> <i>world!</i></h3></body>"
        )

    def test_markdown_to_html_node_code(self):
        md = "```Hello world!```"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<body><pre><code>Hello world!</code></pre></body>"
        )

    def test_markdown_to_html_node_code_inline_markdown(self):
        md = "```**Hello** _world!_```"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<body><pre><code>**Hello** _world!_</code></pre></body>"
        )

    def test_markdown_to_html_node_multiple_lines(self):
        md = """```
def this_is_a_line_of_code():
    while True:
        return True
```"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            """<body><pre><code>
def this_is_a_line_of_code():
    while True:
        return True
</code></pre></body>"""
        )

    def test_markdown_to_html_node_quote(self):
        md = """>Hello world!
>Bye world!
>Hello again world!"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            """<body><blockquote>Hello world!
Bye world!
Hello again world!</blockquote></body>"""
        )

    def test_markdown_to_html_node_quote_inline_markdown(self):
        md = """>Hello _world!_
>**Bye world!**
>Hello again world!"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            """<body><blockquote>Hello <i>world!</i>
<b>Bye world!</b>
Hello again world!</blockquote></body>"""
        )

    def test_markdown_to_html_node_unordered_list(self):
        md = """- Hello world!
- Bye world!
- Hello again world!"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<body><ul><li>Hello world!</li><li>Bye world!</li><li>Hello again world!</li></ul></body>"
        )

    def test_markdown_to_html_node_unordered_list_inline_markdown(self):
        md = """- Hello _world!_
- **Bye world!**
- Hello again world!"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<body><ul><li>Hello <i>world!</i></li><li><b>Bye world!</b></li><li>Hello again world!</li></ul></body>"
        )

    def test_markdown_to_html_node_ordered_list(self):
        md = """1. Hello world!
2. Bye world!
3. Hello again world!"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<body><ol><li>Hello world!</li><li>Bye world!</li><li>Hello again world!</li></ol></body>"
        )

    def test_markdown_to_html_node_ordered_list_inline_markdown(self):
        md = """1. Hello _world!_
2. **Bye world!**
3. Hello again world!"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<body><ol><li>Hello <i>world!</i></li><li><b>Bye world!</b></li><li>Hello again world!</li></ol></body>"
        )

    def test_markdown_to_html_node_ordered_list_double_digits(self):
        md = "1. A\n2. B\n3. C\n4. D\n5. E\n6. F\n7. G\n8. H\n9. I\n10. J\n11. K"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<body><ol><li>A</li><li>B</li><li>C</li><li>D</li><li>E</li><li>F</li><li>G</li><li>H</li><li>I</li><li>J</li><li>K</li></ol></body>"
        )

if __name__ == "__main__":
    unittest.main()
