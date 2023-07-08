# SpotifyAPI-Data-Engineering-Project
This project uses ETL (Extract, Transform, and Load) pipeline to extract data from Spotify using its API and loads the data to a data source(AWS Athena). The entire pipeline will be built using Amazon Web Services (AWS).


### About Dataset / API
The API contains information about music, artists, albums, and songs. [Spotify API](https://developer.spotify.com/documentation/web-api)

### Services Used
<li><strong>AWS S3</strong>: Amazon S3 (Simple Storage Service) is a highly scalable object storage service that can store and retrieve any amount of data from anywhere on the web.
It is commonly used to store and distribute large media files, data backups, and static website files.</li>
<li><strong>AWS Lambda</strong>: AWS Lambda is a serverless computing service that lets you run your code without managing servers. You can use lambda to run code in response to
events like changes in S3, DynamoDB, or other AWS services.</li>
<li><strong>AWS CloudWatch</strong>: Amazon CloudWatch is a monitoring< service for AWS resources and the applications you run on them. You can use CloudWatch to collect and
track metrics, collect and monitor log files, and set alarms.</li>
<li><strong>Glue Crawler</strong>: AWS Glue Crawler is a fully managed service that automatically crawls your data sources, identifies datatypes, and infers schema to create
an AWS Glue Data Catalog.</li>
<li><strong>Data Catalog</strong>: AWS Data Catalog is a fully managed metadata repository that makes it easy to discover and manage data in AWS. Data Catalog can be used with
other AWS Services, such as AWS Athena.</li>
<li><strong>Amazon Athena</strong>: Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena can be used to analyze
data in Glue Data Catalog or in other S3 buckets</li>

### Install Packages
```
pip install pandas
pip install numpy
pip install spotipy
```
