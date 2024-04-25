# Python
import streamlit as st

def main():
    st.title('Mood Based Recommendation System')

    start = st.button("Start")
    if start:
        activity = st.selectbox("What are you in the mood for?", ("Watching a movie", "Reading a book", "Reading a manga", "Watching anime", "Watching YouTube"))
        next = st.button("Next")
        if next:
            mood = st.selectbox("What's your current mood?", ("Happy", "Sad", "Excited", "Bored", "Angry"))
            recommend = st.button("Recommend me")
            if recommend:
                st.write(f"Here are some {activity.lower()} recommendations for when you're feeling {mood.lower()}:")

                # Here you can add code to display recommendations based on the selected activity and mood
                # For example:
                if activity == "Watching a movie" and mood == "Happy":
                    st.write("Movie 1, Movie 2, Movie 3")
                elif activity == "Reading a book" and mood == "Sad":
                    st.write("Book 1, Book 2, Book 3")
                # Add more conditions to handle other combinations of activity and mood

if __name__ == "__main__":
    main()
