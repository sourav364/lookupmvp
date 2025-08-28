"""Streamlit UI for lookup MVP."""
from __future__ import annotations

import httpx
import streamlit as st

from components import charts, tiles

API_URL = "http://localhost:8000"


def main() -> None:
    """Render the Streamlit application."""

    st.sidebar.selectbox("Video (dashboard)", ["video1"], key="video_id")
    video_id: str = st.session_state.video_id

    ask_tab, explore_tab, dash_tab = st.tabs(["Ask", "Explore", "Dashboards"])

    with ask_tab:
        question = st.text_input("Ask a question")
        if st.button("Submit") and question:
            resp = httpx.post(f"{API_URL}/qa", json={"video_id": video_id, "question": question})
            st.session_state.qa_response = resp.json()
        if "qa_response" in st.session_state:
            st.json(st.session_state.qa_response)
            if st.button("Pin to Dashboard"):
                httpx.post(
                    f"{API_URL}/dashboards/{video_id}/pin",
                    json={"video_id": video_id, "spec": {"question": question}},
                )

    with explore_tab:
        st.line_chart(charts.dummy_chart())

    with dash_tab:
        resp = httpx.get(f"{API_URL}/dashboards", params={"video_id": video_id})
        for tile in resp.json():
            tiles.render_tile(tile)


if __name__ == "__main__":
    main()
