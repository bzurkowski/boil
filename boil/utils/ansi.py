ANSI_CODES = {
    'black': '30',
    'white': '37',
    'blue': '34',
    'green': '32',
    'cyan': '36',
    'red': '31',
    'purple': '35',
    'yellow': '33',
    'magenta': '35',
    'bold': '1',
    'reset': '0'
}

ANSI_CODE_PATTERN = "\33[%sm"


def format(text, color=None, bold=False):
    styles = []
    if color:
        styles.append(color)
    if bold:
        styles.append('bold')

    start_code = ''.join([ansi_code(style) for style in styles])
    end_code = ansi_code('reset')

    formatted = []
    for line in text.split('\n'):
        formatted.append("%s%s%s" % (start_code, line, end_code))

    return '\n'.join(formatted)


def ansi_code(style):
    return ANSI_CODE_PATTERN % ANSI_CODES[style]
