from cudatext import *

class Command:
    def run(self):
        s = dlg_input('Unicode hex code:', '')
        if not s:
            return

        s = s.upper()
        if s.startswith('0X'):
            s = s[2:]

        if len(s) == 2:
            s = '00' + s

        if len(s) != 4:
            msg_status('Not valid hex code: ' + s)
            return

        try:
            text = chr(int(s, 16))
        except:
            msg_status('Not valid hex code: ' + s)
            return

        x0, y0, x1, y1 = ed.get_carets()[0]
        ed.insert(x0, y0, text)
        msg_status('Char inserted: U+' + s)
