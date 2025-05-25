import streamlit as st
import time

from sympy.printing.pretty.pretty_symbology import center

st.set_page_config(page_title="Sorry Mau 🥺", layout="centered")


def typewriter(container, lines, speed=0.5):
    text = ""
    for line in lines:
        text += line + "<br>"
        container.markdown(f"<div style='font-size:20px; text-align:center'>{text}</div>", unsafe_allow_html=True)
        time.sleep(speed)


def animate_wordle(container, guesses, letter_delay=0.3, guess_delay=1):
    """
    Animates each guess line letter by letter, stacking all guesses visible at the end.
    """
    color_map = {
        "green": "#6aaa64",
        "yellow": "#c9b458",
        "grey": "#787c7e"
    }

    max_len = 5
    rows = []
    for _ in guesses:
        cols = container.columns(max_len)
        rows.append([col.empty() for col in cols])

    for guess_i, (word, colors) in enumerate(guesses):
        for letter_i, letter in enumerate(word):
            bg_color = color_map.get(colors[letter_i], "#787c7e")
            rows[guess_i][letter_i].markdown(
                f"""
                <div style="
                    width: 60px;
                    height: 60px;
                    background-color: {bg_color};
                    color: white;
                    font-weight: bold;
                    font-size: 32px;
                    text-align: center;
                    line-height: 60px;
                    border-radius: 8px;
                    user-select:none;
                ">{letter.upper()}</div>
                """,
                unsafe_allow_html=True
            )
            time.sleep(letter_delay)
        for empty_i in range(len(word), max_len):
            rows[guess_i][empty_i].markdown(
                f"""
                <div style="
                    width: 60px;
                    height: 60px;
                    background-color: {color_map['grey']};
                    border-radius: 8px;
                "></div>
                """,
                unsafe_allow_html=True
            )
        time.sleep(guess_delay)


if "stage" not in st.session_state:
    st.session_state.stage = "start"
if "photo_index" not in st.session_state:
    st.session_state.photo_index = 0


def start_apology():
    st.session_state.stage = "apology"
    st.session_state.photo_index = 0


def show_memories():
    st.session_state.stage = "memories"
    st.session_state.photo_index = 0


def forgive():
    st.session_state.stage = "forgiven"


def prev_photo():
    if st.session_state.photo_index > 0:
        st.session_state.photo_index -= 1


def next_photo():
    if st.session_state.photo_index < 6:
        st.session_state.photo_index += 1


if st.session_state.stage == "start":
    st.markdown("## 💔 Hey Mau...", unsafe_allow_html=True)
    st.markdown("#### *Click the button below, I’ve got something to say...*")
    st.image(
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWFucnIzenpmcDF0ZXlnd3lpaG9uZTV6ejZtZ2hzbWZ6ZjRlNnpzaiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/kNSeTs31XBZ3G/giphy.gif",
        use_container_width=True)

    col1, col2, col3,col4, col5 = st.columns([1, 1,1,1, 1])
    with col3:
        st.button("Click me", on_click=start_apology)

elif st.session_state.stage == "apology":
    st.markdown("---")
    with st.spinner("Gathering my courage..."):
        time.sleep(1)

    st.markdown("### I am very sorry for yesterday....")

    apology_lines = [
        "Dear Mau,",
        "",
        "I was a complete gadhav yesterday 🙃.",
        "Instead of validating your feelings, I turned into a defensive dumbo.",
        "You were hurt.. and I just didnt listen to you",
        "",
        "It is very difficult for me to not talk to you ☕🐸💤.",
        "",
        "I’m really sorry Mau. Let’s remember some better moments together? 🥺",
    ]

    container = st.empty()
    typewriter(container, apology_lines, speed=0.6)

    st.image(
        "https://media.giphy.com/media/6ILZ0aHS7uHMQ/giphy.gif?cid=ecf05e4716w3jtqm04gob2hr8uyyoq74mpy7ai5w4igay5iw&ep=v1_gifs_search&rid=giphy.gif&ct=g",
        use_container_width=True)

    st.markdown("---")
    st.markdown("### 🧩 Chal Wordle Khelu")
    st.markdown("*Okay technically it’s not real Wordle*")

    guesses = [
        ("tried", ["green", "yellow", "grey", "grey", "grey"]),
        ("cares", ["grey", "yellow", "green", "grey", "grey"]),
        ("spoke", ["grey", "grey", "yellow", "grey", "grey"]),
        ("laugh", ["grey", "grey", "grey", "yellow", "grey"]),
        ("sorry", ["green", "green", "green", "green", "green"]),
    ]

    wordle_container = st.container()
    typing_gif = st.image("https://media.giphy.com/media/3o7aD6Y1mKVYv4NGXe/giphy.gif", width=100)

    animate_wordle(wordle_container, guesses)

    typing_gif.empty()

    st.markdown("##### I guess the answer today was obvious 😅")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.button("Okay, show me the memories 💞", on_click=show_memories)

elif st.session_state.stage == "memories":
    captions = [
        "Our only photo together 😅",
        "Yeah, this one too but this one's weird 😆",
        "My favourite 😆",
        "Deep talks 😎",
        "I miss those walks 🫶",
        "Your pose 😂",
        "Quack!!!!️"
    ]

    st.image(f"pic{st.session_state.photo_index + 1}.jpg", caption=captions[st.session_state.photo_index],
             use_container_width=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("⬅️ Previous") and st.session_state.photo_index > 0:
            prev_photo()

    with col3:
        if st.button("Next ➡️") and st.session_state.photo_index < 6:
            next_photo()

    st.markdown("---")

    st.markdown("<h3 style='text-align:center;'>Do you forgive your Bindok friend? 🥺</h3>", unsafe_allow_html=True)

    col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1,1])
    with col3:
        st.button("Yes", on_click=forgive)

    with col4:
        st.button("Yup", on_click=forgive)


elif st.session_state.stage == "forgiven":
    st.balloons()
    st.markdown("<h2 style='text-align:center; color:hotpink;'>YAY!! Mau forgives me 💖</h2>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExczU2OGY3YjEwaGJ3b3BiNHV5aTh2a3B3czRwczhqZXdjZnd5ZGRkayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/13G7hmmFr9yuxG/giphy.gif", use_container_width=True)
