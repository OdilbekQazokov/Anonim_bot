def escape_markdown_v2(text: str) -> str:

    special_chars = r'_*[]()~`>#+-=|{}.!'
    for char in special_chars:
        text = text.replace(char, f'\{char}')
    return text
