
## Running the demo

```bash
$ npm install -g serverless # skip this line if you have already installed Serverless Framework
$ export AWS_REGION=ap-northeast-2 # You can specify region or skip this line. us-east-1 will be used by default.
$ sls create --template-url "https://github.com/hhheywj/lambda-serverless-tutorial/tree/main" --path docker-selenium-lambda && cd $_
$ sls deploy
$ sls invoke --function demo # Yay! You will get texts of example.com
```

## 디비 정보, 슬랙 webhook은 별도로 넣어주어야합니다.