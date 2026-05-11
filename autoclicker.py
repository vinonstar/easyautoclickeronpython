import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from threading import Thread

class AutoClicker:
    def __init__(self, interval=0.1, button=Button.left, start_stop_key=KeyCode(char='s')):
        """
        Initialize the auto clicker.
        
        Args:
            interval: Time in seconds between clicks (default: 0.1)
            button: Mouse button to click (default: left button)
            start_stop_key: Keyboard key to toggle clicking (default: 's')
        """
        self.interval = interval
        self.button = button
        self.start_stop_key = start_stop_key
        self.running = False
        self.mouse = Controller()
    
    def toggle_clicking(self):
        """Toggle the clicking on/off."""
        self.running = not self.running
        status = "started" if self.running else "stopped"
        print(f"Auto clicker {status}. Press 's' to toggle again. Press 'e' to exit.")
    
    def start_clicking(self):
        """Main loop for clicking."""
        while True:
            if self.running:
                self.mouse.click(self.button)
                time.sleep(self.interval)
            else:
                time.sleep(0.01)  # Small sleep to prevent CPU spinning
    
    def on_press(self, key):
        """Handle keyboard press events."""
        try:
            if key == self.start_stop_key:
                self.toggle_clicking()
            elif key == KeyCode(char='e'):  # Press 'e' to exit
                print("Exiting auto clicker...")
                return False
        except AttributeError:
            pass
    
    def start(self):
        """Start the auto clicker."""
        print("=" * 50)
        print("AUTO CLICKER STARTED")
        print("=" * 50)
        print(f"Click interval: {self.interval} seconds")
        print(f"Toggle clicking: Press 's'")
        print(f"Exit program: Press 'e'")
        print("=" * 50)
        
        # Start clicking thread
        click_thread = Thread(target=self.start_clicking, daemon=True)
        click_thread.start()
        
        # Start listening for keyboard input
        with Listener(on_press=self.on_press) as listener:
            listener.join()


if __name__ == "__main__":
    # Configuration
    CLICK_INTERVAL = 0.1  # Time between clicks in seconds (0.1 = 10 clicks per second)
    MOUSE_BUTTON = Button.left  # Can also use Button.right or Button.middle
    TOGGLE_KEY = KeyCode(char='s')  # Key to start/stop clicking
    
    # Create and start the auto clicker
    clicker = AutoClicker(
        interval=CLICK_INTERVAL,
        button=MOUSE_BUTTON,
        start_stop_key=TOGGLE_KEY
    )
    clicker.start()