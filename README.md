# earnings-sentiment-analysis
Code to analyze sentiment across earnings calls. Uses Python and the NLTK library on top of the standard Python data analysis libraries.

In this project, my objective was to investigate whether sentiment in earnings transcripts for a public company would fluctuate as the company’s performance improved or worsened. I chose Beyond Meat because its market cap and performance have fluctuated wildly during the "helicopter money" era of COVID-related stimulus.

I utilized Python to extract and clean the data, and employed the Natural Language Toolkit (NLTK) Python library to process and analyze the data. The primary figure of the project showcases the distributions of sentence sentiment scores derived from the analysis. I performed sentiment analysis on both sentences and words within each transcript but ultimately found the analysis at the sentence level to be more relevant and insightful.

In summary, while the transcripts generally exhibited an optimistic tone across the years, I observed that during years of poor company performance, there were more negative observations at the tail of each distribution.

Future iterations would focus on improving data wrangling and adding the ability to scrape data from Seeking Alpha or another relevant data source.
