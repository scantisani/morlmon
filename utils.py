def split_text(text):
    lines = []
    text_left = text

    while len(text_left) > 18:
        next_18_chars = text_left[:18]
        split_at = 17

        split_character_index = next_18_chars.find('#')
        if not split_character_index == -1:
            split_at = split_character_index
        else:
            last_space_index = next_18_chars.rfind(' ')
            if not last_space_index == -1:
                split_at = last_space_index

        lines.append(text_left[:split_at + 1])
        text_left = text_left[split_at + 1:]

    lines.append(text_left)
    return lines
