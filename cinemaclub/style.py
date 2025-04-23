cinemaclub_link = 'https://cinemaclub.streamlit.app'
cinemaclub_image = 'https://raw.githubusercontent.com/erickfm/cinemaclub/main/images/cc.png'

img_avatar_weight = 1
img_cinemaclub_weight = 5
img_placeholder_weight = 1  # matches the old avatar weight

def dual_image(user):
    return f"""
    <style>
    .image-row {{
        display: flex;
        justify-content: left;
        align-items: center;
        max-width: 600px;
        gap: 1rem;
        overflow: hidden;
        flex-wrap: nowrap;
    }}

    .avatar-wrapper, .club-wrapper {{
        flex-shrink: 1;
        flex-basis: 0;
        min-width: 0;
    }}

    .club-wrapper {{
        flex-grow: {img_cinemaclub_weight};
    }}

    .avatar-wrapper {{
        flex-grow: {img_avatar_weight};
    }}

    .image-row img {{
        width: 100%;
        height: auto;
        border-radius: 15px;
        display: block;
        object-fit: contain;
        max-width: 100%;
    }}
    </style>

    <div class="image-row">
        <a href="{cinemaclub_link}" target="_blank" class="club-wrapper">
            <img src="{cinemaclub_image}">
        </a>
        <a href="https://letterboxd.com/{user.username}" target="_blank" class="avatar-wrapper">
            <img src="{user.avatar['url']}">
        </a>
    </div>
    """

single_image = f"""
    <style>
    .image-row {{
        display: flex;
        justify-content: left;
        align-items: center;
        max-width: 600px;
        gap: 1rem;
        overflow: hidden;
        flex-wrap: nowrap;
    }}

    .club-wrapper, .placeholder-wrapper {{
        flex-shrink: 1;
        flex-basis: 0;
        min-width: 0;
    }}

    .club-wrapper {{
        flex-grow: {img_cinemaclub_weight};
    }}

    .placeholder-wrapper {{
        flex-grow: {img_placeholder_weight};
    }}

    .image-row img {{
        width: 100%;
        height: auto;
        border-radius: 15px;
        display: block;
        object-fit: contain;
        max-width: 100%;
    }}

    .invisible {{
        visibility: hidden;
    }}
    </style>

    <div class="image-row">
        <a href="{cinemaclub_link}" target="_blank" class="club-wrapper">
            <img src="{cinemaclub_image}">
        </a>
        <div class="placeholder-wrapper">
            <div class="invisible">.</div>
        </div>
    </div>
    """


def feed_image(user, text, subtext='', img_weight=1, text_block_weight=9):
    row_class = f"feed_row_{user.username.replace('-', '_')}"
    if subtext:
        subtext = '"' + subtext + '"'
    text_html = f"<h5 style='margin: 0;'>{text}</h4>" \
                f"<p style='margin-top: 0.25rem;'>{subtext}</p>"

    return f"""
<style>
.{row_class}-container {{
    display: flex;
    justify-content: left;
    align-items: top;
    max-width: 600px;
    gap: 1rem;
    overflow: hidden;
    flex-wrap: nowrap;
}}

.{row_class}-image, .{row_class}-text {{
    flex-shrink: 1;
    flex-basis: 0;
    min-width: 0;
}}

.{row_class}-image {{
    flex-grow: {img_weight};
}}

.{row_class}-text {{
    flex-grow: {text_block_weight};
}}

.{row_class}-container img {{
    width: 100%;
    height: auto;
    border-radius: 15px;
    display: block;
    object-fit: contain;
    max-width: 100%;
}}
</style>

<div class="{row_class}-container">
    <a href="https://letterboxd.com/{user.username}" target="_blank" class="{row_class}-image">
        <img src="{user.avatar['url']}">
    </a>
    <div class="{row_class}-text">
        {text_html}
    </div>
</div>
"""


