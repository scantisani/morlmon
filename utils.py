def split_text(text):
    lines = []
    text_left = text

    while len(text_left) > 18:
        next_17_chars = text_left[:18]
        last_space_index = next_17_chars.rfind(' ')
        if last_space_index == -1:
            last_space_index = 17

        lines.append(text_left[:last_space_index + 1])
        text_left = text_left[last_space_index + 1:]

    lines.append(text_left)
    return lines
