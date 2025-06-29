# 🎬 Daily American Movies and Their Gross Revenue (2000–2020)

This project scrapes daily box office data from [Box Office Mojo](https://www.boxofficemojo.com/) for all movies shown in American theaters between January 1, 2000 and December 31, 2020. It collects this information into a structured CSV file, allowing further analysis using Python and Pandas.

## 📊 Project Purpose

The main goal is to create a comprehensive dataset that shows:
- Which movies were shown each day in U.S. theaters
- How much domestic gross each movie earned
- Which distributors dominated the market

Using this dataset, you can explore long-term industry trends, market shares of studios, and daily movie performance.

## 🐍 Tech Stack

- **Python Version:** 3.x
- **Libraries Used:**
  - requests
  - beautifulsoup4
  - csv
  - datetime
  - time
  - pandas

## Usage

1. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the script:

    ```bash
    python daily-00-20.py.py
    ```
> ⚠️ It takes approximately 5–6 hours to complete, depending on your system and internet speed.

3. Analyze the dataset:
  
    ```bash
    python istatistik.py
    ```


#### What this script does:
- Loads the `data.csv` file and filters the date range (2000–2020).
- Calculates total gross revenue per distributor.
- Computes each distributor’s percentage share of the market.
- Visualizes the top 10 distributors using a pie chart.

## Sample Output
Top 10 Distributors by Market Share (2000–2020)
![market-shares-new](https://user-images.githubusercontent.com/44267861/219720951-f478d908-caa8-4dfb-802c-99eddf05b693.png)
