## User Analytics in the Telecommunication Industry

We are working for a wealthy investor that specializes in purchasing assets that are undervalued. This investor’s due diligence on all purchases includes a detailed analysis of the data that underlies the business, to try to understand the fundamentals of the business and especially to identify opportunities to drive profitability by changing the focus of which products or services are being offered.

The employer wants us to provide a report to analyze opportunities for growth and make a recommendation on whether TellCo is worth buying or selling.  We will do this by analyzing a telecommunication dataset that contains useful information about the customers & their activities on the network. We will deliver insights you managed to extract to the employer through an easy-to-use web-based dashboard and a written report

## Dependencies

Downloads: Jupyter Notebook, VS Code

Libraries to be imported: 

1.  Pandas.
2.  Numpy.
3.  Matplotlib.
4.  SNS.
5.  PIL.
6.  joblib.
7.  sklearn. etc.

## Features

1.  SOURCE OF TELECOM DATA:  The data used for the analysis is provided by Next Hikes.

2.  FEATURES/VARIABLES INCLUDED:  There are around 55 features and variables included in the data. The target variable is Satisfaction Score which can be calculated using the Experience Score and Engagement Score.

3.  DATA SIZE AND FORMAT:  The data has around 150001 rows and 55 columns in the form of xlsx.

## User Overview Analysis

The lifeblood of any business is its customers. Businesses are always finding ways to better understand their customers so that they can provide more efficient and tailored solutions to them. Exploratory Data Analysis (EDA) is a fundamental step in the data science process. It involves all the processes used to familiarize oneself with the data and explore initial insights that will inform further steps in the data science process.

# Visualization of User Overview Analysis:

![top_10_handsets](https://github.com/user-attachments/assets/ca30b3d1-b21b-4f0e-a57f-622fdb07808a)

![top10handsetssnip](https://github.com/user-attachments/assets/7e756cbd-e185-4206-ab49-3ea51b8e362f)

![top_3_manufacturers](https://github.com/user-attachments/assets/5c1394ad-3fae-4ffe-bf32-47193fe83e63)

![2](https://github.com/user-attachments/assets/2f2fb82d-fff4-48ee-aec0-867a3583e2a3)

![3](https://github.com/user-attachments/assets/08c1d1de-71f2-4d9e-801a-821474ffbb52)

![4](https://github.com/user-attachments/assets/a17409f1-db20-471c-bfab-0343b3d7374a)

# Findings from User Overview Analysis:
Interpretation of Top Handsets and Manufacturers:
Huawei B528S-23A leads as the most popular handset, with a significant margin over other models.
Apple dominates the market with a variety of iPhone models, collectively representing the majority of top handsets.
Samsung holds a strong presence with notable models like the Galaxy S8 and A5, though less dominant than Apple.

Interpretation and Recommendation Based on Handset Data
Interpretation:
Top Handsets and Manufacturers:
Huawei B528S-23A leads as the most popular handset, with a significant margin over other models.
Apple dominates the market with a variety of iPhone models, collectively representing the majority of top handsets.
Samsung holds a strong presence with notable models like the Galaxy S8 and A5, though less dominant than Apple.
Manufacturer Breakdown:
Apple is the most prevalent manufacturer, followed by Samsung and Huawei. This indicates a high preference for Apple devices among customers.
Huawei's leading handset is significantly more popular than its other models.
Brand-Specific Insights:
Apple's top models are mainly older versions, which may reflect customer satisfaction with these devices or slower upgrade cycles.
Samsung and Huawei users also favor specific models, with Samsung users showing interest in various Galaxy series and Huawei users favoring the B528S-23A.

## User Engagement Analysis

As telecom brands are the data providers of all online activities, meeting user requirements, and creating an engaging user experience is a prerequisite for them. Building & improving the QoS (Quality of Service) to leverage the mobile platforms and to get more users for the business is good but the success of the business would be determined by the user engagement and activity of the customers on available apps.

# Visualization of User Engagement Analysis:

![user engagement correlation matrix](https://github.com/user-attachments/assets/ab14aaa6-c687-4bac-8bd9-752a022faeb5)
![5](https://github.com/user-attachments/assets/2f7ee3a8-23c7-4715-b53e-9388509b6454)

Interpretation of TOP 10 Customers using enagement metrics
Some MSISDNs appear in multiple top lists, indicating that they are significant users in terms of frequency, duration, and total traffic.
High session frequency does not always equate to high total duration or traffic, and vice versa. This suggests that user behavior can vary widely.
These insights can guide targeted marketing, customer support, and optimization of services based on user engagement metrics.


![6](https://github.com/user-attachments/assets/aba920ba-f7f5-454a-a1a6-574916e50605)

Interpretation of K-3 means clustering both by 2D and 3D
Cluster 0: Likely represents users with moderate engagement frequency and high total usage. These users may have substantial data consumption over a range of session frequencies.
Cluster 1: Characterized by less frequent but high total usage. This cluster might represent users with occasional intense usage or high data consumption in fewer sessions.
Cluster 2: Represents highly active users with both high session frequencies and high data usage. These users are very engaged, using large amounts of data frequentl

![pairplot of cluster metrics](https://github.com/user-attachments/assets/737d89e8-84e7-4185-bdab-f6fc95f5193a)

Interpretation of min, max, average, sum of 3 clusters
Cluster 0: shows moderate session frequencies with very high total durations, downloads, uploads, and traffic. This cluster likely contains highly active users with significant data usage.
Cluster 1: has lower session frequencies but still high total durations and data usage. This cluster might represent users with less frequent but intensive data usage.
Cluster 2: features high session frequencies with very high total durations and data usage. This cluster likely represents highly engaged users with extensive data activities.

![Visualization of top 10 customers of app data](https://github.com/user-attachments/assets/8d75be17-887d-41b8-a66e-516a820eac56)

General Observations of the top 10 most engaged users per application:
Heavy Users: The data indicates that the same users are consistently appearing across multiple categories, showing a trend of general heavy data usage.
Gaming vs. Streaming: Gaming requires the most data, followed by "Other" activities and then streaming services like YouTube and Netflix. This reflects the data-intensive nature of modern gaming and the increasing popularity of streaming services.
Impact: Understanding these usage patterns can help in designing more efficient networks and tailored user experiences, potentially leading to more satisfied customers and optimized service delivery.







