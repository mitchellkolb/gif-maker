

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class RandomTextWindow(Gtk.Window):
    def __init__(self, get_random_text_func):
        super().__init__(title="Random Text Window")
        
        self.get_random_text_func = get_random_text_func
        self.text_list = []  # List to store the random text history
        self.current_index = 0  # Keep track of the current index in the text list

        # Set the window size to be a vertical rectangle
        self.set_default_size(300, 300)

        # Create a vertical box to arrange the label and button
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_margin_top(20)
        vbox.set_margin_bottom(20)
        vbox.set_margin_start(20)
        vbox.set_margin_end(20)

        # Create a label to display the random text
        self.label = Gtk.Label(label="")
        self.label.set_wrap(True)  # Enable text wrapping in GTK 4
        self.label.set_justify(Gtk.Justification.CENTER)  # Center the text

        # Get the initial random text from the passed function and add it to the text list
        random_text = self.get_random_text_func()
        self.text_list.append(random_text)
        self.label.set_text(random_text)

        # Create a button to cycle through the text list
        self.button = Gtk.Button(label="Next Text")
        self.button.connect("clicked", self.on_button_clicked)

        # Add the label and button to the vbox
        vbox.append(self.label)
        vbox.append(self.button)

        # Add the vbox to the window
        self.set_child(vbox)

    def on_button_clicked(self, button):
        """Cycle through the text list and update the label."""
        self.current_index += 1

        # If we have already shown all items, get the next random text
        if self.current_index >= len(self.text_list):
            new_text = self.get_random_text_func()
            self.text_list.append(new_text)

        # Update the label with the new text
        self.label.set_text(self.text_list[self.current_index])


class MyApplication(Gtk.Application):
    def __init__(self, get_random_text_func):
        super().__init__(application_id="com.example.MyApp")
        self.get_random_text_func = get_random_text_func

    def do_activate(self):
        window = RandomTextWindow(self.get_random_text_func)
        window.set_application(self)
        window.show()

def start_gui(get_random_text_func):
    """Initialize the GTK application and open the window."""
    app = MyApplication(get_random_text_func)
    app.run(None)
