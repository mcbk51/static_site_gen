from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None): # In textnode.py create a class called TextNode. It should have 3 properties that can be set in the constructor:
        self.text = text # self.text - The text content of the node
        self.text_type = text_type # self.text_type - The type of text this node contains, which is a member of the TextType enum.
        self.url = url # self.url - The URL of the link or image, if the text is a link. Default to None if nothing is passed in.

    def __eq__(self, other): # Create an __eq__ method that returns True if all of the properties of two TextNode objects are equal. Our future unit tests will rely on this method to compare objects.
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self): # Create a __repr__ method that returns a string representation of the TextNode object. It should look like this:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

