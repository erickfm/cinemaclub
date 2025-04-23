import streamlit as st
from cinemaclub.cc import get_feed, get_user, rounded_img

import streamlit as st

st.set_page_config(page_title="CinemaClub")
query_params = st.query_params

cinemaclub_link = 'https://cinemaclub.streamlit.app'
cinemaclub_image = 'https://raw.githubusercontent.com/erickfm/cinemaclub/main/images/cc.png'



if query_params:
    cola, colb = st.columns([1, 1])
    colb.markdown(f"""<a target="_self" href="https://cinemaclub.streamlit.app"><img src="https://raw.githubusercontent.com/erickfm/cinemaclub/main/images/cc.png" style="display:block;" width="50%" height="100%"></a>""", unsafe_allow_html=1)
    with st.spinner('Loading...'):
        user = get_user(query_params['username'].lower())

    # Relative size controls (change these to tweak)
    img1_weight = 1
    img2_weight = 3

    # HTML with dynamic flex weights
    st.markdown(f"""
    <style>
    .image-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 600px;
        margin: 0 auto;
        gap: 1rem;
        overflow: hidden;
        flex-wrap: nowrap;
    }}

    .image-wrapper1, .image-wrapper2 {{
        flex-shrink: 1;
        flex-basis: 0;
        min-width: 0;
    }}

    .image-wrapper1 {{
        flex-grow: {img1_weight};
    }}

    .image-wrapper2 {{
        flex-grow: {img2_weight};
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
        <a href="https://letterboxd.com/{user.username}" target="_blank" class="image-wrapper1">
            <img src="{user.avatar['url']}">
        </a>
        <a href="{cinemaclub_link}" target="_blank" class="image-wrapper2">
            <img src="{cinemaclub_image}">
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <style>
    .image-row {{
        display: flex;
        justify-content: left;
        align-items: center;
        gap: 1rem;
        flex-wrap: nowrap;
    }}

    .image1 {{
        width: 100%;
        border-radius: 15px;
    }}

    .image2 {{
        width: 100%;
        border-radius: 15px;
    }}

    @media (max-width: 768px) {{
        .image-row {{
            flex-wrap: nowrap;
        }}
        .image1, .image2 {{
            max-width: 100%;
        }}
    }}
    </style>

    <div class="image-row">
        <a href="https://letterboxd.com/{user.username}" target="_blank">
            <img src="{user.avatar['url']}" class="image1">
        </a>
        <a href="{cinemaclub_link}" target="_blank">
            <img src="{cinemaclub_image}" class="image2">
        </a>
    </div>
    """, unsafe_allow_html=True)
    with st.spinner('Loading...'):
        feed = get_feed(query_params['username'])
    st.write(f"pulled {feed['total_logs']} logs")
    for idx, (log_id, log) in enumerate(feed["logs"].items()):
        st.write('\n\n\n')
        if log["event_type"] == 'review':
            st.write(log_id, log.get("title"), log.get("film"))
            st.write(log.get("review"))
        else:
            st.write(log_id, log["username"], log.get("film") or log.get("title"), log["event_type"])
        if idx == 20:  # limit preview to 10 lines
            break
else:
    # cola, colb = st.columns([4, 1])
    cola, colb = st.columns([1, 9])
    colb.markdown(f"""<a target="_self" href="https://cinemaclub.streamlit.app"><img src="https://raw.githubusercontent.com/erickfm/cinemaclub/main/images/cc.png" style="display:block;" width="50%" height="100%"></a>""", unsafe_allow_html=1)
    cola.write('')
    username = st.text_input("Username", placeholder='username', label_visibility='collapsed')
    # spacer = colb.write("")
    # spacer = colb.write("")
    # submit_clicked = colb.button("Submit")

    if username:
        query_params["username"] = username
        st.rerun()

# if about_page:
#     st.markdown('# About \n')
#     st.write('Built by [Erick](https://github.com/erickfm) using Letterboxd and Streamlit.')
#     st.markdown(f"""<div><a href="https://github.com/erickfm/CineBot"><img src="https://raw.githubusercontent.com/erickfm/CineBot/main/images/github-mark.png" style="padding-right: 10px;" width="6%" height="6%"></a>""", unsafe_allow_html=1)