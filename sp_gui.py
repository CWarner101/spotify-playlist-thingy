import sys
import PyQt6.QtCore as core
import PyQt6.QtWidgets as widget


class MainWindow(widget.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spotify Cleaner")
        self.setMinimumSize(core.QSize(400, 300))

        layout = widget.QVBoxLayout()
        widgets = [
            widget.QPushButton,
            widget.QLabel(),
        ]

        for w in widgets:
            layout.addWidget(w())

        widg = widget.QWidget()
        widg.setLayout(layout)

def gui():
    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works too.
    app = widget.QApplication(sys.argv)

    # Create a Qt widget
    window = MainWindow()
    window.show()

    # Start event loop.
    app.exec()

gui()
