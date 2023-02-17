# Insurance-Premium-Prediction

Web Application link
```bash
https://humeranaz-insurance-premium-prediction-app-k6vac5.streamlit.app/
```
### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```


Dataset Link:
```bash
https://github.com/HUMERANAZ/Insurance_Premium_Prediction/blob/main/insurance.csv
```

AWS Credentials to be used:
```bash
AWS_ACCESS_KEY_ID= 
AWS_SECRET_ACCESS_KEY= 
AWS_REGION= 
AWS_ECR_LOGIN_URI= 
ECR_REPOSITORY_NAME=
BUCKET_NAME= 
MONGO_DB_URL= 

```



Install Docker into EC2:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

Command to re-run the ec2 instances:
```bash
cd actions-runner/
./run.sh
```

Deleted ECR due to charges constrains
```bash
Successfully deleted docker image and respository from ECR
```
