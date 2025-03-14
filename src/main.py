from textnode import TextType, TextNode

def main():
    print("hello world")
    tn1 = TextNode("hello world", TextType.NORMAL)
    print(f"tn1: {tn1}")
    tn2 = TextNode("hello world", TextType.LINK, "https://boot.dev")
    print(f"tn2: {tn2}")
    tn3 = TextNode("hello world", TextType.NORMAL)
    print(f"tn3: {tn3}")
    print(f"tn1 == tn3: {tn1 == tn3}")
    print(f"tn2 == tn3: {tn2 == tn3}")

if __name__ == "__main__":
    main()
