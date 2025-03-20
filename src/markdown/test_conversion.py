import unittest
from .conversion import extract_title, markdown_to_html_node

class TestConversion(unittest.TestCase):
    def test_markdown_to_html_node_paragraph(self):
        md = "Hello world!"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><p>Hello world!</p></div>"
        )

    def test_markdown_to_html_node_paragraph_children(self):
        md = "**Hello** _world!_"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><p><b>Hello</b> <i>world!</i></p></div>"
        )

    def test_markdown_to_html_node_heading1(self):
        md = "# Hello world!"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><h1>Hello world!</h1></div>"
        )

    def test_markdown_to_html_node_heading6(self):
        md = "###### Hello world!"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><h6>Hello world!</h6></div>"
        )

    def test_markdown_to_html_node_heading7_paragraph(self):
        md = "####### Hello world!"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><p>####### Hello world!</p></div>"
        )

    def test_markdown_to_html_node_heading3_children(self):
        md = "### **Hello** _world!_"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><h3><b>Hello</b> <i>world!</i></h3></div>"
        )

    def test_markdown_to_html_node_code(self):
        md = """```
Hello world!
```"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><pre><code>Hello world!</code></pre></div>"
        )

    def test_markdown_to_html_node_code_inline_markdown(self):
        md = """```
**Hello** _world!_
```"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><pre><code>**Hello** _world!_</code></pre></div>"
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
            """<div><pre><code>def this_is_a_line_of_code():
    while True:
        return True</code></pre></div>"""
        )

    def test_markdown_to_html_node_quote(self):
        md = """>Hello world!
>Bye world!
>Hello again world!"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            """<div><blockquote>Hello world!
Bye world!
Hello again world!</blockquote></div>"""
        )

    def test_markdown_to_html_node_quote_inline_markdown(self):
        md = """>Hello _world!_
>**Bye world!**
>Hello again world!"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            """<div><blockquote>Hello <i>world!</i>
<b>Bye world!</b>
Hello again world!</blockquote></div>"""
        )

    def test_markdown_to_html_node_quote_spaces(self):
        md = """> Hello world!
> Bye world!
> Hello again world!"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            """<div><blockquote>Hello world!
Bye world!
Hello again world!</blockquote></div>"""
        )

    def test_markdown_to_html_node_unordered_list(self):
        md = """- Hello world!
- Bye world!
- Hello again world!"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Hello world!</li><li>Bye world!</li><li>Hello again world!</li></ul></div>"
        )

    def test_markdown_to_html_node_unordered_list_inline_markdown(self):
        md = """- Hello _world!_
- **Bye world!**
- Hello again world!"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Hello <i>world!</i></li><li><b>Bye world!</b></li><li>Hello again world!</li></ul></div>"
        )

    def test_markdown_to_html_node_ordered_list(self):
        md = """1. Hello world!
2. Bye world!
3. Hello again world!"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Hello world!</li><li>Bye world!</li><li>Hello again world!</li></ol></div>"
        )

    def test_markdown_to_html_node_ordered_list_inline_markdown(self):
        md = """1. Hello _world!_
2. **Bye world!**
3. Hello again world!"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Hello <i>world!</i></li><li><b>Bye world!</b></li><li>Hello again world!</li></ol></div>"
        )

    def test_markdown_to_html_node_ordered_list_double_digits(self):
        md = "1. A\n2. B\n3. C\n4. D\n5. E\n6. F\n7. G\n8. H\n9. I\n10. J\n11. K"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ol><li>A</li><li>B</li><li>C</li><li>D</li><li>E</li><li>F</li><li>G</li><li>H</li><li>I</li><li>J</li><li>K</li></ol></div>"
        )

    def test_extract_title_simple(self):
        md = "# My Title"
        self.assertEqual(extract_title(md), "My Title")

    def test_extract_title_multiple_lines(self):
        md = "\n<building tension>\n\n#   My Title   \n\nnothing to see...\n"
        self.assertEqual(extract_title(md), "My Title")

    def test_extract_title_no_title(self):
        md = " # not a title\nnothing to see...\nbye"
        self.assertRaises(Exception, extract_title, md)

if __name__ == "__main__":
    unittest.main()
