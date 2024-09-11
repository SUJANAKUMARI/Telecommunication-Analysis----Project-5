import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import joblib
import sklearn
import os


# Navigation menu
image = Image.open('telecom image navigation bar.png')
st.sidebar.image(image)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "User Overview Analysis", "User Engagement Analysis", "Experience Analytics", "Satisfaction Analysis", "Satisfaction Score Predictor"])

# Define Home page
if page == "Home":
    st.title("User Analytics in the Telecommunication Industry")
    st.write("""
        Welcome to the User Analytics Dashboard for the Telecommunication Industry. 
        Use the navigation bar to explore user overview analysis and gain insights into user behavior and handset usage.
    """)

    image = Image.open('telecom industry.png')
    st.image(image) 

# Define User Overview Analysis page
elif page == "User Overview Analysis":
    st.title("User Overview Analysis")
    
    # Introduction
    st.markdown("""
    The lifeblood of any business is its customers. Businesses are always finding ways to better understand their customers so that they can provide more efficient and tailored solutions to them. 
    Exploratory Data Analysis (EDA) is a fundamental step in the data science process. It involves all the processes used to familiarize oneself with the data and explore initial insights that will inform further steps in the data science process.
    """)

    # Task: Top 10 Handsets
    st.subheader("Top 10 Handsets Used by Customers")
    # Example display of the top 10 handsets
    top_10_handsets = pd.read_csv('top_10_handsets.csv')
    # st.write(top_10_handsets)

        # Create two columns
    col1, col2 = st.columns(2)

    # Display the CSV data in the first column
    with col1:
        st.subheader("Top 10 Handsets Data")
        st.dataframe(top_10_handsets)

    # Display the plot in the second column
    with col2:
        st.subheader("Top 10 Handsets Plot")
        image = Image.open('top_10_handsets.png')
        st.image(image, caption='Top 10 Handsets Used by Customers', width=700) 

    st.markdown("""
    - **Interpretation of Top Handsets and Manufacturers:**  
        - Huawei B528S-23A leads as the most popular handset, with a significant margin over other models.  
        - Apple dominates the market with a variety of iPhone models, collectively representing the majority of top handsets.  
        - Samsung holds a strong presence with notable models like the Galaxy S8 and A5, though less dominant than Apple.  
    """)

    # Task: Top 3 Handset Manufacturers
    st.subheader("Top 3 Handset Manufacturers")
    # Example code to calculate top manufacturers
    top_3_manufacturers = pd.read_csv('top_3_manufacturers.csv')
    # st.write(manufacturers)
    
    col1, col2 = st.columns(2)

    # Display the CSV data in the first column
    with col1:
        st.subheader("Top 3 manufacturers Data")
        st.dataframe(top_3_manufacturers)

    # Display the plot in the second column
    with col2:
        st.subheader("Top 10 Handsets Plot")
        image = Image.open('top_3_manufacturers.png')
        st.image(image, caption='Top 3 Manufacturers') 

    st.write("""
    The top 3 handset manufacturers are:
    - Manufacturer 1 - APPLE
    - Manufacturer 2 - SAMSUNG
    - Manufacturer 3 - HUAWEI
    """)

    # Task: Top 5 Handsets per Top 3 Manufacturers
    st.subheader("Top 5 Handsets per Top 3 Manufacturers")
    top_5_handsets_df = pd.read_csv('top_5_handsets_per_manufacturer.csv')
    st.dataframe(top_5_handsets_df)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Top 5 Handsets Plot for Apple Phones")
        image = Image.open('top_5_handsets_Apple.png')
        st.image(image, caption='Top 5 Handsets for Apple Phone') 

    with col2:
        st.subheader("Top 5 Handsets Plot for Samsung Phones")
        image = Image.open('top_5_handsets_Samsung.png')
        st.image(image, caption='Top 5 Handsets for Samsung Phone') 

    with col3:
        st.subheader("Top 5 Handsets Plot for Huawei Phones")
        image = Image.open('top_5_handsets_huwaie.png')
        st.image(image, caption='Top 5 Handsets for Huawei Phone')

    # Interpretation and Recommendation Based on Handset Data
    st.subheader("Interpretation and Recommendation Based on Handset Data")

    # Interpretation Section
    st.markdown("### Interpretation:")
    st.markdown("""
        1. **Top Handsets and Manufacturers:**
        - Huawei B528S-23A leads as the most popular handset, with a significant margin over other models.
        - Apple dominates the market with a variety of iPhone models, collectively representing the majority of top handsets.
        - Samsung holds a strong presence with notable models like the Galaxy S8 and A5, though less dominant than Apple.
   
        2. **Manufacturer Breakdown:**
        - Apple is the most prevalent manufacturer, followed by Samsung and Huawei. This indicates a high preference for Apple devices among customers.
        - Huawei's leading handset is significantly more popular than its other models.
   
        3. **Brand-Specific Insights:**
        - Apple's top models are mainly older versions, which may reflect customer satisfaction with these devices or slower upgrade cycles.
         - Samsung and Huawei users also favor specific models, with Samsung users showing interest in various Galaxy series and Huawei users favoring the B528S-23A.
        """)

        # Recommendation Section
    st.markdown("### Recommendations to Marketing Teams:")
    st.markdown("""
        1. **Focus on Apple Device Users:**
        - **Strategy:** Tailor marketing campaigns to target Apple device users, considering their high engagement and loyalty.
        - **Action:** Promote Apple-specific offers, such as accessories or app bundles, and consider partnerships with Apple-related services to enhance customer experience.
    
        2. **Highlight Top Handsets:**
        - **Strategy:** Since Huawei B528S-23A is highly popular, create targeted promotions or loyalty programs focused on users of this and similar handsets.
        - **Action:** Develop exclusive deals or bundles for users of the top handsets to encourage continued engagement and brand loyalty.
        """)
    
    st.subheader("Correlation Analysis of App Data")
    image = Image.open('correlation_matrix_overview.png')
    st.image(image)
    
    st.markdown("""
        ***Interpreting the Correlation Matrix:***
        
        Key Observations:
        1.  Social Media DL (Bytes) and Social Media UL (Bytes) have a strong positive correlation (1.000), indicating that users who download more social media data also tend to upload more.
        2.  Google DL (Bytes) and Google UL (Bytes) show a similar pattern, with a strong positive correlation (1.000).
        3.  Netflix DL (Bytes) and Netflix UL (Bytes) also exhibit a strong positive correlation (1.000).
        4.  Gaming DL (Bytes) and Gaming UL (Bytes) have a strong positive correlation (1.000).
                
        Overall:
        The correlation matrix provides valuable information about the relationships between different application data variables. The strong positive correlations between download and upload data for specific applications highlight their interdependent nature, while the lack of strong correlations between different applications suggests their relative independence.
        """)

    st.subheader("Dimensionality Reduction")
    st.write("Visualization of PCA Components")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Scatterplot of PCA1 and PCA2")
        image = Image.open('1.png')
        st.image(image)
    
    with col2:
        st.subheader("Biplot of PCA1 and PCA2")
        image = Image.open('2.png')
        st.image(image)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("KDE plot of PCA1 and PCA2")
        image = Image.open('3.png')
        st.image(image)

    with col2:
        st.subheader("3D Visualization of PCA1 and PCA2")
        image = Image.open('4.png')
        st.image(image)
    
     # Title or heading for the section
    st.title('Principal Component Analysis Interpretation')

    # Markdown content
    st.markdown("""
    ### Interpretation

    #### Significant Information Captured
    The first two principal components capture a substantial portion of the variance in the data, indicating that they are capturing significant patterns in the data.

    #### Dimensionality Reduction
    Reducing the data to two principal components has retained a considerable amount of the original information.

    #### Meaningful Interpretationl
    PC1 and PC2 are likely capturin 8g the most important variations in the data, potentially related to overall data usage patterns, network quality, or device characteristics.

    #### Focus on Main Patterns
    Since the first two components explain a significant amount of variance, you can focus on analyzing and interpreting them for your analysis, as they capture the most important relationships in the data.

    ##Interpretation of PC1:##

    PC1 seems to represent the overall network performance and data usage intensity. Users with higher values on PC1 likely have sessions with higher average throughput, longer activity durations, and fewer seconds with low data volumes. They experience less time with very low download and upload throughputs.

    ##Interpretation of PC2:##

    PC2 seems to represent the dominance of download volume in a session. Higher values on PC2 indicate sessions with a greater amount of data downloaded (especially for non-gaming applications).
    """)

    # Define User Overview Analysis page
elif page == "User Engagement Analysis":
    st.title("User Engagement Analysis")
    
    # Introduction
    st.markdown("""
                As telecom brands are the data providers of all online activities, meeting user requirements, and creating an engaging user experience is a prerequisite for them. Building & improving the QoS (Quality of Service) to leverage the mobile platforms and to get more users for the business is good but the success of the business would be determined by the user engagement and activity of the customers on available apps. 
                """)
    st.subheader("Correlation Matrix table")
    corr_matrix = pd.read_csv('corr_matrix.csv')
    st.dataframe(corr_matrix)

    st.subheader("Correlation Matrix of Engagement Metrix")
    image = Image.open('user engagement correlation matrix.png')
    st.image(image)

    st.markdown("""
        #### Interpretation of Correlation Matrix:
        
        1. High correlations (close to 1) suggest strong linear relationships. For example, session_frequency has a very high correlation with total_upload (0.93) and a high correlation with total_traffic (0.81).
        2. Moderate correlations indicate moderate relationships between variables, such as total_duration and total_download (0.60).
        3. The correlation between total_download and total_traffic is extremely high (0.99), indicating a near-perfect linear relationship, likely because total traffic is the sum of total download and upload.
        4. These correlations can help identify key relationships between user engagement metrics, guiding further analysis or decision-making.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Customers with Top 10 Session Frequency")
        top_10_session_frequency = pd.read_csv('top_10_session_frequency.csv')
        st.dataframe((top_10_session_frequency[['MSISDN/Number','session_frequency']]))


    with col2:
        st.subheader("Customers with Top 10 Total Duration")
        top_10_duration = pd.read_csv('top_10_duration.csv')
        st.dataframe((top_10_duration[['MSISDN/Number', 'total_duration']]))

    with col3:
        st.subheader("Customers with Top 10 Total Traffic")
        top_10_total_traffic = pd.read_csv('top_10_total_traffic.csv')
        st.dataframe((top_10_total_traffic[['MSISDN/Number', 'total_traffic']]))

    st.subheader("Visualization of Engagement Metrics")
    image = Image.open('Visualization of engagement metrics.png')
    st.image(image)

    st.markdown("""
        #### Interpretation of TOP 10 Customers using enagement metrics
        
        1. Some MSISDNs appear in multiple top lists, indicating that they are significant users in terms of frequency, duration, and total traffic.
        2. High session frequency does not always equate to high total duration or traffic, and vice versa. This suggests that user behavior can vary widely.
        
        These insights can guide targeted marketing, customer support, and optimization of services based on user engagement metrics.
    """)

    st.subheader("Visualization of 2D Clusters in 3 Groups in Engagement Metrics")
    image = Image.open('Visualization of 2D cluster in engagement metrics.png')
    st.image(image)

    st.subheader("Visualization of 3D Clusters in 3 Groups in Engagement Metrics")
    image = Image.open('visualization of 3D cluster in engagement metrics.png')
    st.image(image)

    st.subheader("K-3 Means Cluster Metrics")
    cluster_metrics = pd.read_csv('cluster_metrics.csv')
    st.dataframe(cluster_metrics)


    st.markdown("""
        #### Interpretation of K-3 means clustering both by 2D and 3D
                
        1. Cluster 0: Likely represents users with moderate engagement frequency and high total usage. These users may have substantial data consumption over a range of session frequencies. 
        2. Cluster 1: Characterized by less frequent but high total usage. This cluster might represent users with occasional intense usage or high data consumption in fewer sessions.
        3. Cluster 2: Represents highly active users with both high session frequencies and high data usage. These users are very engaged, using large amounts of data frequentl
        """)
    
    st.subheader("Pair Plot of User Engagement Data")
    image = Image.open('pairplot of cluster metrics.png')
    st.image(image)

    st.markdown("""
        #### Interpretation of min, max, average, sum of 3 clusters
        1. Cluster 0: shows moderate session frequencies with very high total durations, downloads, uploads, and traffic. This cluster likely contains highly active users with significant data usage.
        2. Cluster 1: has lower session frequencies but still high total durations and data usage. This cluster might represent users with less frequent but intensive data usage.
        3. Cluster 2: features high session frequencies with very high total durations and data usage. This cluster likely represents highly engaged users with extensive data activities.
    """)

    st.subheader("Customers with Top 10 Gaming Total Data")
    top_10_Gaming_Total_Data = pd.read_csv('top_10_Gaming_Total_Data.csv')
    st.dataframe((top_10_Gaming_Total_Data[['MSISDN/Number','Gaming_Total_Data']]))

    st.subheader("Customers with Top 10 Youtube Total Data")
    top_10_Youtube_Total_Data = pd.read_csv('top_10_Youtube_Total_Data.csv')
    st.dataframe((top_10_Youtube_Total_Data[['MSISDN/Number','Youtube_Total_Data']]))

    st.subheader("Customers with Top 10 Netflix Total Data")
    top_10_Netflix_Total_Data = pd.read_csv('top_10_Netflix_Total_Data.csv')
    st.dataframe((top_10_Netflix_Total_Data[['MSISDN/Number','Netflix_Total_Data']]))

    st.subheader("Customers with Top 10 Google Total Data")
    top_10_Google_Total_Data = pd.read_csv('top_10_Google_Total_Data.csv')
    st.dataframe((top_10_Google_Total_Data[['MSISDN/Number','Google_Total_Data']]))

    st.subheader("Customers with Top 10 Email Total Data")
    top_10_Email_Total_Data = pd.read_csv('top_10_Email_Total_Data.csv')
    st.dataframe((top_10_Email_Total_Data[['MSISDN/Number','Email_Total_Data']]))

    st.subheader("Customers with Top 10 Social Media Total Data")
    top_10_Social_Media_Total_Data = pd.read_csv('top_10_Social_Media_Total_Data.csv')
    st.dataframe((top_10_Social_Media_Total_Data[['MSISDN/Number','Social_Media_Total_Data']]))

    st.subheader("Customers with Top 10 Other Total Data")
    top_10_Other_Total_Data = pd.read_csv('top_10_Other_Total_Data.csv')
    st.dataframe((top_10_Other_Total_Data[['MSISDN/Number','Other_Total_Data']]))

    st.subheader("Visualization of Top 10 Customers of Different Apps")
    image = Image.open('Visualization of top 10 customers of app data.png')
    st.image(image)

    st.markdown("""
        #### General Observations of the top 10 most engaged users per application:
        1. Heavy Users: The data indicates that the same users are consistently appearing across multiple categories, showing a trend of general heavy data usage.
        2. Gaming vs. Streaming: Gaming requires the most data, followed by "Other" activities and then streaming services like YouTube and Netflix. This reflects the data-intensive nature of modern gaming and the increasing popularity of streaming services.
        
        Impact: Understanding these usage patterns can help in designing more efficient networks and tailored user experiences, potentially leading to more satisfied customers and optimized service delivery.
        """)
    
    st.subheader("Visualization of Optimized K-Value using Elbow Method")
    image = Image.open('optimized k value elbow method.png')
    st.image(image)

    st.markdown("""
        #### The optimized value of K is 3 from the above elbow method plot
        """)
    
    st.subheader("Visualization of 2D clustering for App Data")
    image = Image.open('visualization of 2D cluster for app data.png')
    st.image(image)

    st.subheader("Visualization of 3D clustering for App Data")
    image = Image.open('visualization of 3D cluster for app data.png')
    st.image(image)

    st.markdown("""
        #### Interpretation of Applications Data k- means cluster by optimal k method both 2D and 3D
        
        Based on the provided 3D visualization, the K-Means clustering algorithm appears to have effectively grouped the applications into three distinct clusters.

        #### Key Observations:
        1. Cluster Separation: The clusters are visually well-separated, suggesting that the algorithm has successfully identified meaningful groupings within the data.
        2. Cluster Density: Cluster 0 and Cluster 2 appear to have higher densities of data points, indicating that there might be more applications in these clusters. Cluster 1 seems to have a lower density.
        3. Cluster Distribution: The clusters are distributed in different regions of the 3D space, suggesting that they are defined by distinct combinations of the PCA components.
        """)

elif page == "Experience Analytics":
    st.title("Experience Analytics")
    
    # Introduction
    st.markdown("""
        The Telecommunication industry has experienced a great revolution in the last decade. Mobile devices have become the new fashion trend and play a vital role in everyone's life. The success of the mobile industry is largely dependent on its consumers. Therefore, the vendors must focus on their target audience i.e. what are the needs and requirements of their consumers and how they feel and perceive their products. Tracking & evaluating customers’ experience can help organizations optimize their products and services so that they meet evolving user expectations, needs, and acceptance.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Customers with Top 10 Average TCP Values")
        top_10 = pd.read_csv('top_10.csv')
        st.dataframe((top_10[['MSISDN/Number','Avg TCP Retransmission (Bytes)']]))


    with col2:
        st.subheader("Customers with Last 10 Average TCP Values")
        last_10 = pd.read_csv('last_10.csv')
        st.dataframe((last_10[['MSISDN/Number', 'Avg TCP Retransmission (Bytes)']]))

    with col3:
        st.subheader("Customers with most frequent TCP Values")
        most_10 = pd.read_csv('most_10.csv')
        st.dataframe((most_10[['Avg TCP Retransmission (Bytes)','Frequency', 'Occurrences']]))

    st.subheader("Visualization of Top 10, Bottom 10 & Most Frequent TCP Value Customers")
    image = Image.open('visualization of average tcp values.png')
    st.image(image)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Customers with Top 10 Average RTT Values")
        top_10_rtt= pd.read_csv('top_10_rtt.csv')
        st.dataframe((top_10_rtt[['MSISDN/Number','Avg RTT (ms)']]))


    with col2:
        st.subheader("Customers with Last 10 Average RTT Values")
        last_10_rtt = pd.read_csv('last_10_rtt.csv')
        st.dataframe((last_10_rtt[['MSISDN/Number', 'Avg RTT (ms)']]))

    with col3:
        st.subheader("Customers with most frequent RTT Values")
        most_10_rtt = pd.read_csv('most_10_rtt.csv')
        st.dataframe((most_10_rtt[['Avg RTT (ms)','Frequency', 'Occurrences']]))

    st.subheader("Visualization of Top 10, Bottom 10 & Most Frequent RTT Value Customers")
    image = Image.open('visualization of average rtt values.png')
    st.image(image)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Customers with Top 10 Average Throughput Values")
        top_10_throughput= pd.read_csv('top_10_throughput.csv')
        st.dataframe((top_10_throughput[['MSISDN/Number','Avg Throughput (kbps)']]))


    with col2:
        st.subheader("Customers with Last 10 Average Througput Values")
        last_10_throughput = pd.read_csv('last_10_throughput.csv')
        st.dataframe((last_10_throughput[['MSISDN/Number', 'Avg Throughput (kbps)']]))

    with col3:
        st.subheader("Customers with most frequent Throughput Values")
        most_10_throughput = pd.read_csv('most_10_throughput.csv')
        st.dataframe((most_10_throughput[['Avg Throughput (kbps)','Frequency', 'Occurrences']]))

    st.subheader("Visualization of Top 10, Bottom 10 & Most Frequent Throughput Value Customers")
    image = Image.open('visualization of average throughput values.png')
    st.image(image)

    st.subheader("Distribution of Average Throughput Per Handset")
    throughput_distribution = pd.read_csv('throughput_distribution.csv')
    st.dataframe(throughput_distribution)

    st.markdown("""
        #### Interpretation of Average Throughput per Handset Type
        1. Top Performers: Handsets like the Zyxel Communicat. Sbg3600 and A-Link Telecom I. Cubot Power offer the highest throughput, which is beneficial for users requiring high-speed internet access, such as for streaming or large data downloads.
        2. Moderate Performers: Devices like the A-Link Telecom I. Cubot Nova and Zyxel Communicat. Lte7460 show good throughput but may not provide the highest speeds available.
        3. Low Performers: Devices like the A-Link Telecom I. Cubot Note Plus and Zyxel Communicat. Zyxel Wah7706 have lower throughput, which could be a limitation for users who need faster internet speeds.
        """)
    
    st.subheader("Distribution of Average TCP Retransmission Per Handset")
    retransmission_distribution = pd.read_csv('retransmission_distribution.csv')
    st.dataframe(retransmission_distribution)

    st.markdown("""
        #### Interpretation of Average TCP Retransmission per Handset Type¶
        1. High Retransmission Devices: Devices like Zyxel Communicat. Sbg3600 and Lte7460 exhibit extremely high retransmissions, which could be a result of poor signal quality, interference, or network congestion.
        2. Moderate Retransmission Devices: Devices such as the A-Link Telecom I. Cubot Note S and A5 are in the moderate range, indicating some issues that could be addressed with better network configurations or hardware improvements.
        3. Low Retransmission Devices: Devices like A-Link Telecom I. Cubot Power and Nova show minimal retransmission activity, suggesting a good connection quality and fewer issues related to network loss.
        """)

    st.subheader("Visualization of 2D clustering using Experience Analysis")
    image = Image.open('visualization of 2D cluster in experience analysis.png')
    st.image(image)

    st.subheader("Visualization of 3D clustering using Experience Analysis")
    image = Image.open('Visualization of 3D cluster in experience analysis1.png')
    st.image(image)

    st.markdown("""
        ####Interpreting the Clusters based on 2D and 3D scatter plots of Experience Analysis:
        1. Cluster 0 (Yellow): This cluster appears to represent users with a high average throughput, low average TCP retransmission rate, and relatively low average RTT. These users likely experience a smooth and efficient network connection with minimal latency and data loss.
        2. Cluster 1 (Teal): This cluster seems to represent users with a lower average throughput, higher average TCP retransmission rate, and potentially higher average RTT. These users might encounter network congestion, instability, or increased latency, leading to slower data transfer and decreased user experience.
        3. Cluster 2 (Purple): This cluster is relatively small and seems to be located between Cluster 0 and Cluster 1. It might represent a group of users with mixed experiences, possibly due to intermittent network issues or varying usage patterns.
        """)

elif page == "Satisfaction Analysis":
    st.title("Satisfaction Analytics")
    
    # Introduction
    st.markdown("""
                Assuming that the satisfaction of a user is dependent on user engagement and experience, you’re expected in this section to analyze customer satisfaction in depth.
                """)
    
    st.subheader("Top 10 Customers With Highest Satisfaction Score ")
    top_10_customers_summary = pd.read_csv('top_10_customers_summary.csv')
    st.dataframe(top_10_customers_summary)

    st.subheader("Table of Metrics For Each Model")
    metrics_df = pd.read_csv('metrics_df.csv')
    st.dataframe(metrics_df)

    st.subheader("Visualization of Best Fit Model")
    image = Image.open('visualization of rmse cv of each model.png')
    st.image(image) 

    st.markdown("""
        #### Best Fit:
        Based on the metrics, Random Forest seems to offer the best fit due to its combination of low error rates and robust generalization, making it the most reliable model for predicting the satisfaction score in this context.

        #### Conclusion:
        While Ridge Regression and linear regression metrics are impressive, they suggest overfitting rather than a model that generalizes well. Random Forest offers a better balance between performance and generalization, making it a more reliable choice for real-world application.
    """) 

    st.subheader("Visualization of 2D K-Means Clusters of Experience Score and Engagement Scores")
    image = Image.open('visualization of 2D cluster of experience vs engagement scores.png')
    st.image(image) 

    st.subheader("Visualization of 2D K-Means Clusters PCA1 and PCA2 using Experience Score and Engagement Scores")
    image = Image.open('visualization of 2D cluster of pca1 and pca2 experience vs engagement scores.png')
    st.image(image)

    st.subheader("Visualization of Average Satisfaction and Experience Scores of Clusters")
    image = Image.open('visualization of average satisfaction and experience scores of clusters.png')
    st.image(image)

    st.markdown("""
        #### Interpretation
        Cluster 0 has a significantly higher Average Satisfaction Score compared to Cluster 1. This suggests that customers in Cluster 0 are generally more satisfied with their experience.
        Cluster 1 has a slightly higher Average Experience Score than Cluster 0. This indicates that while the overall satisfaction is lower, the experience score is marginally better.

        #### Decision Making
        Based on these scores, here are some considerations for your employer:

        #### Customer Satisfaction:
        The high satisfaction score in Cluster 0 is a positive indicator. It suggests that a significant portion of the customer base is very satisfied, which is a good sign for customer retention and loyalty.

        #### Customer Experience:
        The experience scores are relatively close, with Cluster 1 having a slight edge. This indicates that the overall customer experience is fairly consistent across clusters, though there is room for improvement in satisfaction for Cluster 1.

        #### Recommendation
        Given the high satisfaction score in Cluster 0 and the relatively consistent experience scores, it seems that the company has a strong base of satisfied customers. However, the lower satisfaction in Cluster 1 suggests there are areas that need attention.

        #### Recommendation: Proceed with the purchase, but with a strategy to improve customer satisfaction in Cluster 1. This could involve targeted improvements in customer service, product quality, or other areas impacting satisfaction.
    
        """)
    
elif page == "Satisfaction Score Predictor":
    
    # Load the saved models
    random_forest_model = joblib.load('random_forest_model.joblib')  # Use consistent variable name
    kmeans_model = joblib.load('kmeans_model.joblib')
    scaler = joblib.load('scaler_model.joblib')

    # Title of the Streamlit app
    st.title("Customer Satisfaction Score & Cluster Prediction")

    # Input fields for feature values
    st.header("Input Features")

    session_frequency = st.number_input('Session Frequency', min_value=0.0)
    total_duration = st.number_input('Total Duration', min_value=0.0)
    total_traffic = st.number_input('Total Traffic', min_value=0.0)
    avg_tcp_retrans = st.number_input('Avg TCP Retransmission (Bytes)', min_value=0.0)
    avg_rtt = st.number_input('Avg RTT (ms)', min_value=0.0)
    avg_throughput = st.number_input('Avg Throughput (kbps)', min_value=0.0)
    engagement_score = st.number_input('Engagement Score', min_value=0.0)
    experience_score = st.number_input('Experience Score', min_value=0.0)

    # Predict button
    if st.button("Predict Satisfaction and Cluster"):

        # Prepare input features for the satisfaction model
        features = np.array([[session_frequency, total_duration, total_traffic, avg_tcp_retrans, avg_rtt, avg_throughput, experience_score, engagement_score]])
    
        # Predict satisfaction score using Random Forest model
        satisfaction_score = random_forest_model.predict(features)  # Correctly using the loaded variable name
    
        # Prepare the engagement and experience scores for clustering
        cluster_data = np.array([[engagement_score, experience_score]])
    
        # Scale the data for clustering
        cluster_data_scaled = scaler.transform(cluster_data)
    
        # Predict cluster using KMeans model
        cluster = kmeans_model.predict(cluster_data_scaled)
    
        # Display the results
        st.subheader("Results")
        st.write(f"Satisfaction Score: {satisfaction_score[0]:.4f}")
        st.write(f"Predicted Cluster: {cluster[0]}")

        # Recommendations based on cluster prediction
        if cluster[0] == 0:
            st.success("Proceed with the purchase. Customer satisfaction is high.")
        elif cluster[0] == 1:
            st.warning("Purchase not recommended. Consider improvements before proceeding.")
        else:
            st.info("Further analysis needed for this cluster.")



# To run the Streamlit app
# Run this command in the terminal: streamlit run app.p