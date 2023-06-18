from w3lib import html


def clean_text(text: str) -> str:
    no_code = html.remove_tags_with_content(
        text=text, which_ones=["code", "pre"]
    )
    no_tags = html.remove_tags(text=no_code)
    return no_tags
