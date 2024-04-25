# Python
import streamlit as st

def main():
    st.title('Mood Based Recommendation System')

    activity = st.selectbox("What are you in the mood for?", ("Watching a movie", "Reading a book", "Reading a manga", "Watching anime", "Watching YouTube"))
    
    if st.button("Next"):
        mood = st.selectbox("What's your current mood?", ("Happy", "Sad", "Excited", "Bored", "Angry"))
        
        if st.button("Recommend me"):
            st.write(f"Here are some {activity.lower()} recommendations for when you're feeling {mood.lower()}:")

            
if __name__ == "__main__":
    main()
