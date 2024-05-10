# A web based service

1. needs internet to enjoy it's benefit
2. Three ways to access AWS > CLI,GUI management console and SDK

**Pricing model is pay as you go(On demand)**

1. All upfront reserve (1-3 years)
2. partial upfront reserve (1-3 years)
3. No payment reserved (1-3 years)

- Some services are always free like IAM and VPC, while others cost you, due to supporting services such as elastic beanstalk, cloudformation,which are free but the EC2/S3 other services launched behind them are paid

**Pricing Calculator, Budgets, etc**

- AWS Regions, availability zones

**Shared responsibility**

- AWS is responsible for the security of the cloud
- You are responsible for security inside the cloud

**S3 Simple Storage Service**

- Can store items as objects (known as item storage)
- You get eleven 9's of duribility (9.9999999999)
- You get four 9's of availability (9.999)
- A single object must not exceed 5tb in size
- Access to bucket can be restricted, to the bucket as a whole or to individual items inside the bucket
- Data is private, there is an option to encrypt
- Each objust MUST have a unique name
- When a file is edited you must make the change then re-upload the file to the bucket

**S3 Types**

- S3 standard storage
- S3 intelligent tiering (moves objects to cheaper storage based on use case)
- S3 standard I.A (Infrequent-Access)
- S3 one-zone I.A
- S3 Glacier
- S3 Glacier Deep Archive
