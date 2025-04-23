import streamlit as st
from letterboxdpy import user
from datetime import datetime
import requests
from PIL import Image, ImageDraw
from io import BytesIO


@st.cache_resource
def get_feed(username):
    # feed generator for a Letterboxd user’s *following* list
    root = user.User(username)
    following = root.get_following()
    combined_logs = {
        log_id: {**log, "username": u}
        for u in following
        for log_id, log in user.User(u).get_activity()["logs"].items()
    }
    combined_logs = dict(
        sorted(
            combined_logs.items(),
            key=lambda item: datetime(**item[1]["time"]),
            reverse=True,
        )
    )
    return {"logs": combined_logs, "total_logs": len(combined_logs)}


def get_user(username):
    return user.User(username)


def rounded_img(url, radius=1000):
    """Fetches an image from a URL and returns it with rounded corners."""
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert("RGB")

    # Create rounded corner mask
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, img.size[0], img.size[1]], radius=radius, fill=255)

    # Apply mask and return image with alpha
    img = img.convert("RGBA")
    img.putalpha(mask)
    return img
