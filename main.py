import tkinter as tk
from tkinter import scrolledtext as stxt
from markdown import markdown as md
from tkhtmlview import HTMLLabel


class Mithlond:
    def __init__(self, root):
        self.root = root
        self.root.title("Mithlond")

        # Text area for notes
        self.text_area = stxt.ScrolledText(root, wrap = tk.WORD, width = 60, height = 20)
        self.text_area.pack(pady = 10)

        # preview button
        self.preview_button = tk.Button(root, text = 'Preview', command = self.render_markdown)
        self.preview_button.pack (pady = 10)

        # display rendered markdown
        self.render_area = HTMLLabel(root, html = "", width = 60, height = 20)
        self.render_area.pack(pady = 10)


    def render_markdown(self):
        # get text from text area
        markdown_text = self.text_area.get("1.0", tk.END)

        # convert markdwon to HTML
        html_content = md(markdown_text)

        # update the render area
        self.render_area.set_html(html_content)


if __name__ == "__main__":
    root = tk.Tk()
    app = Mithlond(root)
    root.mainloop()

