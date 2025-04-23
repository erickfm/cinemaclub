import streamlit as st
from cinemaclub.cc import get_feed, get_user
from cinemaclub.style import single_image, dual_image, feed_image

st.set_page_config(page_title="CinemaClub", page_icon='https://raw.githubusercontent.com/erickfm/cinemaclub/main/images/film.png')
query_params = st.query_params
if query_params:
    with st.spinner('Loading...'):
        user = get_user(query_params['username'].lower())
    st.markdown(dual_image(user), unsafe_allow_html=True)
    st.write('')
    with st.spinner('Loading...'):
        feed = get_feed(query_params['username'])
    for idx, (log_id, log) in enumerate(feed["logs"].items()):
        st.write('\n\n\n')
        feed_user = get_user(log.get('username'))
        if log["event_type"] == 'review':
            text = log.get("title") + ' ' + log.get("film")
            st.markdown(feed_image(feed_user, text, log.get("review")), unsafe_allow_html=True)
        else:
            st.markdown(feed_image(feed_user, log.get("title")), unsafe_allow_html=True)
        if idx == 100:  # limit preview
            break
else:
    st.markdown(single_image, unsafe_allow_html=True)
    st.write('')
    username = st.text_input("Username", placeholder='username', label_visibility='collapsed')
    if username:
        query_params["username"] = username
        st.rerun()

# if about_page:
#     st.markdown('# About \n')
#     st.write('Built by [Erick](https://github.com/erickfm) using Letterboxd and Streamlit.')
#     st.markdown(f"""<div><a href="https://github.com/erickfm/CineBot"><img src="https://raw.githubusercontent.com/erickfm/CineBot/main/images/github-mark.png" style="padding-right: 10px;" width="6%" height="6%"></a>""", unsafe_allow_html=1)