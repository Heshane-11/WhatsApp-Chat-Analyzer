import streamlit as st
import preprocessing
import set
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
from textblob import TextBlob
from urlextract import URLExtract
from wordcloud import WordCloud
from collections import Counter
import emoji

# --- Custom CSS for Streamlit UI ---
st.markdown("""
    <style>
    body {
        background-color: #f7fafc;
    }
    .reportview-container {
        background-color: #e6edf2;
    }
    .sidebar .sidebar-content {
        background-color: #1e2a47;
        color: white;
    }
    .sidebar .sidebar-header {
        font-size: 20px;
        color: #f9d423;
        text-align: center;
    }
    .sidebar .sidebar-subheader {
        font-size: 15px;
        color: #f9d423;
    }
    .stButton>button {
        background-color: #1e2a47;
        color: white;
        border-radius: 12px;
        font-size: 16px;
        padding: 10px 15px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #f9d423;
        color: black;
    }
    .metric-container {
        background-color: #1e3a5f;
        color: white;
        padding: 10px;
        border-radius: 12px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        margin-bottom: 15px;
    }
    .metric-container .stMetric .value {
        font-size: 30px;
        color: #f9d423;
    }
    .stTextInput input {
        background-color: #f0f7fa;
        border-radius: 10px;
        border: 1px solid #c5c7c9;
    }
    .stDataFrame {
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .stPlotlyChart {
        border-radius: 10px;
        background-color: #f7fafc;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        padding: 10px;
    }
    .stPlotlyChart h2 {
        color: #1e2a47;
    }
    </style>
""", unsafe_allow_html=True)

# 🎨 Sidebar Design
st.sidebar.title("📊 MessAge MiNeR")
st.sidebar.markdown("**Analyze WhatsApp Chat Data Smartly!**")

# 📂 File Upload Section
uploaded_file = st.sidebar.file_uploader("📂 Upload your WhatsApp Chat File", type=["txt"])

if uploaded_file is not None:
    # Read the uploaded file
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessing.preprocess(data)

    # 📌 User Selection Dropdown
    user_list = df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, 'Overall')

    selected_user = st.sidebar.selectbox("👤 Select a User", user_list)

    if st.sidebar.button('🔍 Show Analysis'):
        st.markdown("<h2 style='text-align: center; color: #1e2a47;'>📊 WhatsApp Chat Analysis</h2>", unsafe_allow_html=True)

        # 🎯 **TOP STATISTICS**
        st.title("📊 Top Chat Statistics")
        with st.expander("ℹ️ What this section does"):
            st.write("""
            In this section, we display the overall statistics like the number of messages, words shared, media files shared, and links exchanged in the chat. These metrics give an overview of the volume of communication.
            """)
        num_messages, words, num_media, num_links = set.fetch_stats(selected_user, df)
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("💬 Total Messages", num_messages)
        col2.metric("📝 Total Words", words)
        col3.metric("📷 Media Shared", num_media)
        col4.metric("🔗 Links Shared", num_links)

        # 📅 **TIMELINE ANALYSIS**
        st.title("📆 Chat Timeline Analysis")
        with st.expander("ℹ️ What this section does"):
            st.write("""
            The Timeline Analysis section showcases how the messaging activity has evolved over time. You can see both the monthly and daily patterns of messaging in the chat.
            """)
        # 🔹 Monthly Timeline
        st.subheader("📅 Monthly Messages")
        timeline = set.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='green', linewidth=2)
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # 🔹 Daily Timeline
        st.subheader("📆 Daily Messages")
        daily_timeline = set.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black', linewidth=2)
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # 🔥 **ACTIVITY MAP**
        st.title("🔥 Chat Activity Trends")
        with st.expander("ℹ️ What this section does"):
            st.write("""
            The Activity Map shows which days and months were the most active in terms of messaging. It helps in identifying periods of high or low activity in the chat.
            """)
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Most Active Days")
            busy_day = set.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.subheader("📆 Most Active Months")
            busy_month = set.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # 🌍 **WEEKLY ACTIVITY HEATMAP**
        st.title("🌍 Weekly Activity Heatmap")
        with st.expander("ℹ️ What this section does"):
            st.write("""
            The Weekly Activity Heatmap provides a visual representation of the activity levels across the days of the week, allowing you to spot patterns in chat behavior.
            """)
        user_heatmap = set.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap, cmap="coolwarm", annot=True, fmt=".0f")
        st.pyplot(fig)

        # 🏆 **MOST BUSY USERS**
        if selected_user == 'Overall':
            st.title("🏆 Most Active Users")
            with st.expander("ℹ️ What this section does"):
                st.write("""
                This section ranks the most active participants in the chat based on the number of messages they sent. It also provides a pie chart showing the distribution of messages among the top users.
                """)
            x, new_df = set.most_busy_users(df)
            x = x[x.index != 'group_notification']
            new_df = new_df[new_df['name'] != 'group_notification']

            col1, col2 = st.columns(2)
            with col1:
                fig, ax = plt.subplots()
                ax.bar(x.index, x.values, color='green')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df.style.set_properties(**{'text-align': 'center'}))

            # 🥧 **Pie Chart for User Distribution**
            st.subheader("📌 User Activity Distribution")
            fig = px.pie(new_df, values="percent", names="name", title="Most Busy Users",
                         color_discrete_sequence=px.colors.qualitative.Pastel)
            st.plotly_chart(fig)

        # ☁️ **WORDCLOUD**
        st.title("☁️ WordCloud - Most Used Words")
        with st.expander("ℹ️ What this section does"):
            st.write("""
            The WordCloud provides a visual representation of the most frequently used words in the chat, with larger words indicating higher usage.
            """)
        df_wc = set.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(fig)

        # 🔠 **MOST COMMON WORDS**
        st.title("🔠 Most Commonly Used Words")
        with st.expander("ℹ️ What this section does"):
            st.write("""
            This section displays a bar graph of the most frequently used words, offering insight into the common terms or phrases shared in the chat.
            """)
        most_common_df = set.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.barh(most_common_df[0], most_common_df[1], color='pink')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # 📧 **EMOJI ANALYSIS**
        st.title("📧 Emoji Analysis")
        with st.expander("ℹ️ What this section does"):
            st.write("""
            The Emoji Analysis breaks down the usage of emojis in the chat, showing the top emojis shared and their respective counts.
            """)
        emoji_df = set.emoji_helper(selected_user, df)
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(emoji_df)

        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f")
            st.pyplot(fig)

        # **SENTIMENT ANALYSIS**
        st.title("🧠 Sentiment Analysis")
        with st.expander("ℹ️ What this section does"):
            st.write("""
            This section analyzes the sentiment of messages, determining whether the conversations tend to be positive, negative, or neutral based on the words used.
            """)
        sentiment_df = df[['message']].copy()
        sentiment_df['polarity'] = sentiment_df['message'].apply(lambda msg: TextBlob(msg).sentiment.polarity)
        sentiment_df['sentiment'] = sentiment_df['polarity'].apply(
            lambda score: 'Positive' if score > 0 else ('Negative' if score < 0 else 'Neutral')
        )
        sentiment_counts = sentiment_df['sentiment'].value_counts()
        fig = px.pie(sentiment_counts, values=sentiment_counts.values, names=sentiment_counts.index,
                     title="Sentiment Analysis")
        st.plotly_chart(fig)

else:
    st.sidebar.warning("⚠️ Please upload a WhatsApp chat file for analysis.")
