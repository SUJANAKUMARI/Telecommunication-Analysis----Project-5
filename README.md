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

![user engagement correlation matrix](https://github.com/user-attachments/assets/ab14aaa6-c687-4bac-8bd9-752a022faeb5)

Interpretation of Correlation Matrix:
High correlations (close to 1) suggest strong linear relationships. For example, session_frequency has a very high correlation with total_upload (0.93) and a high correlation with total_traffic (0.81).
Moderate correlations indicate moderate relationships between variables, such as total_duration and total_download (0.60).
The correlation between total_download and total_traffic is extremely high (0.99), indicating a near-perfect linear relationship, likely because total traffic is the sum of total download and upload.
These correlations can help identify key relationships between user engagement metrics, guiding further analysis or decision-making.

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

![optimized k value elbow method](https://github.com/user-attachments/assets/1b88cb73-f51e-40cb-bfb3-73fda95ddf63)

## The optimized value of K is 3 from the above elbow method plot ##

![visualization of 2D cluster for app data](https://github.com/user-attachments/assets/262d3c32-22bf-4320-9290-d2d73797cd62)
![visualization of 3D cluster for app data](https://github.com/user-attachments/assets/96c33025-771d-402f-87e8-86cccf091abd)

Key Observations:
Cluster Separation: The clusters are visually well-separated, suggesting that the algorithm has successfully identified meaningful groupings within the data.
Cluster Density: Cluster 0 and Cluster 2 appear to have higher densities of data points, indicating that there might be more applications in these clusters. Cluster 1 seems to have a lower density.
Cluster Distribution: The clusters are distributed in different regions of the 3D space, suggesting that they are defined by distinct combinations of the PCA components.

## Experience Analytics:

The Telecommunication industry has experienced a great revolution in the last decade. Mobile devices have become the new fashion trend and play a vital role in everyone's life. The success of the mobile industry is largely dependent on its consumers. Therefore, the vendors must focus on their target audience i.e. what are the needs and requirements of their consumers and how they feel and perceive their products. Tracking & evaluating customers’ experience can help organizations optimize their products and services so that they meet evolving user expectations, needs, and acceptance.

![visualization of average tcp values](https://github.com/user-attachments/assets/24faf145-4e57-4888-8c38-29ee81a1e483)

![visualization of average rtt values](https://github.com/user-attachments/assets/8c499c9c-1779-4695-a141-8dd987ef156f)

![visualization of average throughput values](https://github.com/user-attachments/assets/e0361807-243f-4431-928b-a2d642c6b27b)

Interpretation of Average Throughput per Handset Type
Top Performers: Handsets like the Zyxel Communicat. Sbg3600 and A-Link Telecom I. Cubot Power offer the highest throughput, which is beneficial for users requiring high-speed internet access, such as for streaming or large data downloads.
Moderate Performers: Devices like the A-Link Telecom I. Cubot Nova and Zyxel Communicat. Lte7460 show good throughput but may not provide the highest speeds available.
Low Performers: Devices like the A-Link Telecom I. Cubot Note Plus and Zyxel Communicat. Zyxel Wah7706 have lower throughput, which could be a limitation for users who need faster internet speeds.

Interpretation of Average TCP Retransmission per Handset Type¶
High Retransmission Devices: Devices like Zyxel Communicat. Sbg3600 and Lte7460 exhibit extremely high retransmissions, which could be a result of poor signal quality, interference, or network congestion.
Moderate Retransmission Devices: Devices such as the A-Link Telecom I. Cubot Note S and A5 are in the moderate range, indicating some issues that could be addressed with better network configurations or hardware improvements.
Low Retransmission Devices: Devices like A-Link Telecom I. Cubot Power and Nova show minimal retransmission activity, suggesting a good connection quality and fewer issues related to network loss.

![visualization of 2D cluster in experience analysis](https://github.com/user-attachments/assets/aadc6e76-a9b6-4566-a6bb-02dfc27cfc63)

![Visualization of 3D cluster in experience analysis1](https://github.com/user-attachments/assets/781a24b2-9f1f-4b95-be08-7b26933d1e92)

Interpreting the Clusters based on 2D and 3D scatter plots of Experience Analysis:
Cluster 0 (Yellow): This cluster appears to represent users with a high average throughput, low average TCP retransmission rate, and relatively low average RTT. These users likely experience a smooth and efficient network connection with minimal latency and data loss.
Cluster 1 (Teal): This cluster seems to represent users with a lower average throughput, higher average TCP retransmission rate, and potentially higher average RTT. These users might encounter network congestion, instability, or increased latency, leading to slower data transfer and decreased user experience.
Cluster 2 (Purple): This cluster is relatively small and seems to be located between Cluster 0 and Cluster 1. It might represent a group of users with mixed experiences, possibly due to intermittent network issues or varying usage patterns.

## Satisfaction Analytics:

Assuming that the satisfaction of a user is dependent on user engagement and experience, you’re expected in this section to analyze customer satisfaction in depth.

![7](https://github.com/user-attachments/assets/7c5628c7-6242-4cde-b258-fd0654451e46)

![visualization of rmse cv of each model](https://github.com/user-attachments/assets/11f13595-3646-460e-b2ef-fb9e29a4c03e)

Best Fit:
Based on the metrics, Random Forest seems to offer the best fit due to its combination of low error rates and robust generalization, making it the most reliable model for predicting the satisfaction score in this context.

Conclusion:
While Ridge Regression and linear regression metrics are impressive, they suggest overfitting rather than a model that generalizes well. Random Forest offers a better balance between performance and generalization, making it a more reliable choice for real-world application.

![visualization of 2D cluster of experience vs engagement scores](https://github.com/user-attachments/assets/75481f5d-29d5-43ad-bd34-307950deb83e)

![visualization of 2D cluster of pca1 and pca2 experience vs engagement scores](https://github.com/user-attachments/assets/b05e68a0-437a-438c-a7e3-fdecc2ce4f2f)

![visualization of average satisfaction and experience scores of clusters](https://github.com/user-attachments/assets/89308327-6559-4157-a02f-346e8e056caf)

Interpretation
Cluster 0 has a significantly higher Average Satisfaction Score compared to Cluster 1. This suggests that customers in Cluster 0 are generally more satisfied with their experience. Cluster 1 has a slightly higher Average Experience Score than Cluster 0. This indicates that while the overall satisfaction is lower, the experience score is marginally better.

Decision Making
Based on these scores, here are some considerations for your employer:

Customer Satisfaction:
The high satisfaction score in Cluster 0 is a positive indicator. It suggests that a significant portion of the customer base is very satisfied, which is a good sign for customer retention and loyalty.

Customer Experience:
The experience scores are relatively close, with Cluster 1 having a slight edge. This indicates that the overall customer experience is fairly consistent across clusters, though there is room for improvement in satisfaction for Cluster 1.

Recommendation
Given the high satisfaction score in Cluster 0 and the relatively consistent experience scores, it seems that the company has a strong base of satisfied customers. However, the lower satisfaction in Cluster 1 suggests there are areas that need attention.

Recommendation: Proceed with the purchase, but with a strategy to improve customer satisfaction in Cluster 1. This could involve targeted improvements in customer service, product quality, or other areas impacting satisfaction.

## FINAL OUTPUT OF THE MODEL AFTER DEPOYING:

![8](https://github.com/user-attachments/assets/e998a614-df73-4c13-8317-a8f75a80c7a3)
![9](https://github.com/user-attachments/assets/a6867829-92ff-4acb-afca-86b4b9149edf)

## ACKNOWLEDGEMENT:

 I would like to express my special thanks of gratitude to my Mentor, "Ms. Swetha Sutar" for the guidance and support by giving some reference articles by which I was very much succesful in understanding and completing my project.





















