from random import shuffle
import streamlit as st
from datetime import datetime
import os

# fixed parameters
initial_red_words = ["put", "the", "I", "no", "of",
                     "my", "for", "he", "go", "me", "said",
                     "are", "you", "your", "all", "like", "I've",
                     "want", "call", "we", "be", "baby", "her", "she", "to", "washing",
                     "some", "there", "so", "tall", "ball", "small", "do", "any", "many",
                     "one", "anyone", "come", "they", "here", "have", "was"]
time_format = "%Y-%m-%d %H:%M:%S"
initial_time_path = "time.txt"
final_time_path = "time_final.txt"
end_flag_path = "end_flag.txt"


# functions
@st.cache(allow_output_mutation=True)
def get_red_words_list(fn_text):
    vec = fn_text.split(",")
    return vec, len(vec)


def write_time_0():
    with open(file=initial_time_path, mode="w") as time_file:
        time_file.write(str(datetime.now())[0: 19])
    if os.path.exists(end_flag_path):
        os.remove(end_flag_path)


def read_time_0():
    with open(file=initial_time_path, mode="r") as time_file:
        return datetime.strptime(time_file.read(), time_format)


def write_time_1():
    with open(file=final_time_path, mode="w") as time_file:
        time_file.write(str(datetime.now())[0: 19])


def read_time_1():
    with open(file=final_time_path, mode="r") as time_file:
        return datetime.strptime(time_file.read(), time_format)


def write_end_flag():
    with open(file=end_flag_path, mode="w") as end_flag_file:
        end_flag_file.write(str(datetime.now())[0: 19])


def calculate_time_difference(d_1, d_0):
    return (d_1 - d_0).total_seconds()


if __name__ == '__main__':
    if not os.path.exists(initial_time_path):
        write_time_0()
    else:
        pass
    t0 = read_time_0()
    st.header("TYPING GAME")
    st.write("This game takes a list of words as input, shuffles them, writes them one at a time, and awaits your input to type in each word.")
    st.write("It keeps track of the time and will calculate your average typing velocity.")
    st.subheader("type in the words you want to type separated by a comma in the box below.")
    text_input = st.text_input(label="Typing word list", value=",".join(initial_red_words))
    ls_, ln = get_red_words_list(text_input)
    if len(ls_) != 0:
        if len(ls_) == ln:
            write_time_0()
            t0 = read_time_0()
        cur_word = ls_[-1]
        st.header(cur_word)
        game_input = st.text_input(label=f"type: '{cur_word}' ", value="")
        if game_input == cur_word:
            next_word = st.button(label="CLICK FOR NEXT WORD!")
            ls_.pop()
            shuffle(ls_)
            st.subheader(f"Words completed: {ln - len(ls_)}")
            st.subheader(f"Words remaining: {len(ls_)}")
            t1 = datetime.now()
            delta = calculate_time_difference(t1, t0)
            st.subheader(f"Time elapsed time: {delta} seconds / {round(delta / 60, 2)} minutes")
            st.subheader(f"You started at:  {t0}")
            if next_word:
                pass
        else:
            pass
    else:
        st.subheader("All done!")
        if not os.path.exists(end_flag_path):
            write_end_flag()
            write_time_1()
            t1 = read_time_1()
            delta = calculate_time_difference(t1, t0)
            st.subheader(f"ALL DONE! Total time:  {delta} seconds / {round(delta / 60, 2)} minutes")
            st.subheader(f"Your word velocity was: {round(ln / delta, 2)} words per second")
            st.subheader(f"You started at:  {t0}")
            st.subheader("Write a new set of words to go again!")
        else:
            pass
