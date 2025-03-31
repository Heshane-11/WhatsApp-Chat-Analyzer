# 📊 MessageMiner

**MessageMiner** is a WhatsApp Chat Analyzer built using **Python, Streamlit, pandas, and seaborn**. It helps users gain insights from their WhatsApp chat data by visualizing key statistics, message trends, and other analytics.

## ✨ Features

- 🧹 **Chat Preprocessing:** Cleans and structures raw WhatsApp chat exports.
- 📊 **Message Analysis:** Provides insights into message frequency, user activity, and word usage.
- ❌ **Stopword Filtering:** Removes unnecessary words using a predefined Hinglish stopword list.
- 📈 **Graphical Representations:** Uses **seaborn** and **matplotlib** to generate charts and graphs.
- 🎨 **Streamlit UI:** User-friendly interface for easy interaction.

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/messageiner.git
   cd messageiner
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. **Run the Streamlit App:**
   ```bash
   streamlit run UI.py
   ```

2. **Upload WhatsApp Chat File:**
   - 📂 Export chat from WhatsApp (without media).
   - ⬆️ Upload it to the application.

3. **View Analysis:**
   - 🏆 **Top contributors** in the chat.
   - ⏳ **Message frequency** over time.
   - 🔤 **Commonly used words** (excluding stopwords).
   - 🎭 **Sentiment analysis** (if applicable).

## 📂 Project Structure

```
/messageiner
│── 🗂️ preprocessing.py    # Data cleaning and processing
│── 📜 set.py              # Stopword handling
│── 🎨 UI.py               # Streamlit app
│── 📃 stop_hinglish.txt   # Hinglish stopword list
│── 📌 requirements.txt    # Dependencies
```

## 🛠️ Technologies Used

- 🐍 **Python**
- 🎨 **Streamlit**
- 📊 **pandas**
- 📈 **seaborn**
- 📉 **matplotlib**

## 📸 Screenshots

### 📊 Chat Statistics Overview
![Chat Statistics](https://github.com/Heshane-11/WhatsApp-Chat-Analyzer/blob/main/images/Screenshot%202025-03-11%20221223.png)

### ⏳ Monthly Messages Over Time
![Message Frequency](https://github.com/Heshane-11/WhatsApp-Chat-Analyzer/blob/main/images/Screenshot%202025-03-11%20221320.png)

### ⏳ Chat Activity Trends
![Message Frequency](https://github.com/Heshane-11/WhatsApp-Chat-Analyzer/blob/main/images/Screenshot%202025-03-11%20221357.png)

### ⏳ Weekly Activity
![Message Frequency](https://github.com/Heshane-11/WhatsApp-Chat-Analyzer/blob/main/images/Screenshot%202025-03-11%20221417.png)

### 🔠 Wordcloud
![Common Words](https://github.com/Heshane-11/WhatsApp-Chat-Analyzer/blob/main/images/Screenshot%202025-03-11%20221517.png)


### 🎭 Sentiment Analysis (if applicable)
![Sentiment Analysis](https://github.com/Heshane-11/WhatsApp-Chat-Analyzer/blob/main/images/Screenshot%202025-03-11%20232206.png)


## 🤝 Contribution

Feel free to contribute by submitting pull requests or reporting issues.

---
