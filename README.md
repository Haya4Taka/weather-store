# weather-store
Open weather map APIから日本の主要都市の天候情報を取得し、DBに保存するバッチ処理。
## requirements
* docker
* mysqlデータベース  
*マイグレーションについてはweather-servicesレポジトリを参照  
* Open weather map APIのAPI KEY

## build
```
docker build -t weather-services/weather-store:0.0.1 .
```

## run
```
docker run -it --rm -w="/opt/app/weather-store" \
                        --env-file ./test_db_conf \
                        weather-services/weather-store:0.0.1 python bin/batch_script.py
```

データベースの情報及びAPI_KEYを設定ファイルに記載するなどして、コンテナの環境変数として
渡す必要があります。

```
DB_USERNAME=
DB_PASSWORD=
DB_URL=
DB_NAME=
WEATHER_API_KEY=
```