import streamlit as st
from cinemaclub.cc import get_feed, get_user, rounded_img

st.set_page_config(page_title="Letterboxd Feed")
cola, colb = st.columns([3, 1])
cola.markdown(
    f"""<a target="_self" href="https://cinemaclub.streamlit.app"><img src="https://raw.githubusercontent.com/erickfm/cinemaclub/main/images/cc.png" style="display:block;" width="80%" height="100%"></a>""",
    unsafe_allow_html=1)
query_params = st.query_params
if query_params:

    with st.spinner('Loading...'):
        user = get_user(query_params['username'].lower())
    colb.markdown(
        f"""
        <a href="https://letterboxd.com/{user.username}" target="_blank">
            <img src="{user.avatar['url']}" style="border-radius: 15px; width: 100%; max-width: 400px;">
        </a>
        """,
        unsafe_allow_html=True
    )
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
    username = st.text_input("Username", placeholder='username', label_visibility='collapsed',)
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