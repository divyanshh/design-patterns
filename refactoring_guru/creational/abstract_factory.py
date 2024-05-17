from abc import ABC, abstractmethod


# Abstract Products
class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class TextBox(ABC):
    @abstractmethod
    def input_text(self, text):
        pass


# Concrete Products for macOS
class MacOSButton(Button):
    def click(self):
        return "MacOS button clicked."


class MacOSTextBox(TextBox):
    def input_text(self, text):
        return f"Typed '{text}' on MacOS textbox."


# Concrete Products for Windows
class WindowsButton(Button):
    def click(self):
        return "Windows button clicked."


class WindowsTextBox(TextBox):
    def input_text(self, text):
        return f"Typed '{text}' on Windows textbox."


# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_textbox(self):
        pass


# Concrete Factory for macOS
class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_textbox(self):
        return MacOSTextBox()


# Concrete Factory for Windows
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_textbox(self):
        return WindowsTextBox()


# Client code
def create_gui(factory):
    button = factory.create_button()
    textbox = factory.create_textbox()
    return button, textbox


# Create GUI for macOS
macos_factory = MacOSFactory()
macos_button, macos_textbox = create_gui(macos_factory)
print(macos_button.click())  # Output: MacOS button clicked.
print(macos_textbox.input_text("Hello"))  # Output: Typed 'Hello' on MacOS textbox.

# Create GUI for Windows
windows_factory = WindowsFactory()
windows_button, windows_textbox = create_gui(windows_factory)
print(windows_button.click())  # Output: Windows button clicked.
print(windows_textbox.input_text("World"))  # Output: Typed 'World' on Windows textbox.
