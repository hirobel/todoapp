FORMAT: 1A

# Group 概要

## 概要
* ToDoの作成、変更、削除、一覧取得を行うAPIの仕様について記載する

## 認証について
* 全てのAPIでAuthorizationヘッダが必要である
* Authorizationヘッダには有効なid_tokenをセットする必要がある
* 有効なid_tokenを取得するには、所定のcognitoクライアントへアクセスして認証を行う必要がある
    * cognitoクライアントへのアクセスURLは本番環境へのデプロイ時に決定される
    * その上で、認証を行うユーザをクライアントに紐付いたユーザプールへ事前に登録しておく必要がある。
    * さらに、初回ログイン時は初期パスワードの変更が必要となる

## API実装について
* github( [Link](https://github.com/hirobel/todoapp) )を参照

## その他
* 本番環境へのデプロイ時にステージをdevからprodへ変更する
    * 本ドキュメントでは執筆時点のステージ名(dev)及びエンドポイント名で記載する

# Group 設計
 
## ToDo情報管理 [/todos/{id}]

* アクセス情報

| key | value |
| --- | --- |
| Endpoint URL | https://zm7ajk3pk4.execute-api.ap-northeast-1.amazonaws.com |
| Stage | dev |

### ToDo登録 [POST]
 
#### 処理概要
 
* 入力内容を基にTODOの新規追加を行う
 
+ Request (application/json)
 
    + Headers

            Authorization: eyJraWQiOiJmVDdnTk9QbUR4OVFaV1lhbXFES1BNV3gyaHVcL1NIRVVMd3RwSEhhMERhRT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJjMTA1MTI4Ny1iNGExLTQxNTctYTA4ZC1mMTc1NzdiOWI4YTIiLCJhdWQiOiI1ZG11YTZrZzJnamVhcnA0a21kMGsxcGZ0cCIsImV2ZW50X2lkIjoiMDU5ODE3ZmMtMzI0MC0xMWU5LThlNjQtMmI3MzdjMTcxMWZlIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE1NTAzNTg2MTYsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1ub3J0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1ub3J0aGVhc3QtMV9PR21LV1puQjUiLCJjb2duaXRvOnVzZXJuYW1lIjoiaGthdG8iLCJleHAiOjE1NTAzNjIyMTYsImlhdCI6MTU1MDM1ODYxNn0.nYQ-MzE_yRh4aMGdCLeEP0G1ILpZkDdPS4ZYh0jFZu5L5P2vj1SPinl4ovT0YH8AW4kL5qDOO4XA14tVxZmHiofcnaMjjIwHxhFPCXqwytXNU8Qs1PajFtL-pHhWJ8FtG-qLdbmUjweyJ7-pPYm5y_H3ARQTbwHLtLiPPr3Rq2mU7vmAIj8fdN4ANdCLRhj7lnFCvuJn6rRhyDdlVFruNUV_EqyfhpOdUEWv8H1wLcJHiBWcJI1aCzKyluZhuE_MfY-QgHsEvMHZtyGN9H5sO0VnSBUBMgWS7t8qYoe0z4WENukoR1eCRIKJwZKxVlUeAzkKTQv7bRYZcAz-Kbh1gA (string, required) - 認証トークン
 
    + Attributes
        + title: Test Title (string, required) - タイトル
        + content: Test Content (string, required) - 内容
        + due_Date: 1550288140777 (number, required) - 期限日（タイムスタンプ型）
        + status: New (string, required) - ステータス
 
+ Response 200 (application/json)
 
    + Attributes
        + result (required)
        + errors (required)
        + data (required)
            + id: 4419f2da-32b7-11e9-a317-f6e8a5a58d35 (string, required) - id
            + title: Test Title (string, required) - タイトル
            + content: Test Content (string, required) - 内容
            + due_date: 1550288140777 (number, required) - 期限日（タイムスタンプ型）
            + status: New (string, required) - ステータス種別(New:新規, WIP:作業中, Done:完了, Pending:保留 )

### ToDo一覧取得 [GET]
 
#### 処理概要
 
* すべてのTODOの取得を行う
 
+ Request (application/json)
 
    + Headers

            Authorization: eyJraWQiOiJmVDdnTk9QbUR4OVFaV1lhbXFES1BNV3gyaHVcL1NIRVVMd3RwSEhhMERhRT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJjMTA1MTI4Ny1iNGExLTQxNTctYTA4ZC1mMTc1NzdiOWI4YTIiLCJhdWQiOiI1ZG11YTZrZzJnamVhcnA0a21kMGsxcGZ0cCIsImV2ZW50X2lkIjoiMDU5ODE3ZmMtMzI0MC0xMWU5LThlNjQtMmI3MzdjMTcxMWZlIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE1NTAzNTg2MTYsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1ub3J0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1ub3J0aGVhc3QtMV9PR21LV1puQjUiLCJjb2duaXRvOnVzZXJuYW1lIjoiaGthdG8iLCJleHAiOjE1NTAzNjIyMTYsImlhdCI6MTU1MDM1ODYxNn0.nYQ-MzE_yRh4aMGdCLeEP0G1ILpZkDdPS4ZYh0jFZu5L5P2vj1SPinl4ovT0YH8AW4kL5qDOO4XA14tVxZmHiofcnaMjjIwHxhFPCXqwytXNU8Qs1PajFtL-pHhWJ8FtG-qLdbmUjweyJ7-pPYm5y_H3ARQTbwHLtLiPPr3Rq2mU7vmAIj8fdN4ANdCLRhj7lnFCvuJn6rRhyDdlVFruNUV_EqyfhpOdUEWv8H1wLcJHiBWcJI1aCzKyluZhuE_MfY-QgHsEvMHZtyGN9H5sO0VnSBUBMgWS7t8qYoe0z4WENukoR1eCRIKJwZKxVlUeAzkKTQv7bRYZcAz-Kbh1gA (string, required) - 認証トークン
  
+ Response 200 (application/json)
 
    + Attributes
        + result (required)
        + errors (required)
        + data (required)
            + Array (array)
                + id: 4419f2da-32b7-11e9-a317-f6e8a5a58d35 (string, required) - id
                + title: Test Title (string, required) - タイトル
                + content: Test Content (string, required) - 内容
                + due_date: 1550288140777 (number, required) - 期限日（タイムスタンプ型）
                + status: New (string, required) - ステータス種別(New:新規, WIP:作業中, Done:完了, Pending:保留 )

 
### ToDo削除 [DELETE]
 
#### 処理概要
 
* 入力内容を基にTODOの削除を行う
 
+ Parameters
 
    + id: `4419f2da-32b7-11e9-a317-f6e8a5a58d35` (string, required) - id
 
+ Response 204

### ToDo更新 [PUT]
 
#### 処理概要
 
* 入力内容を基にTODOの更新を行う

+ Parameters
 
    + id: `4419f2da-32b7-11e9-a317-f6e8a5a58d35` (string, required) - id

+ Request (application/json)
 
    + Headers

            Authorization: eyJraWQiOiJmVDdnTk9QbUR4OVFaV1lhbXFES1BNV3gyaHVcL1NIRVVMd3RwSEhhMERhRT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJjMTA1MTI4Ny1iNGExLTQxNTctYTA4ZC1mMTc1NzdiOWI4YTIiLCJhdWQiOiI1ZG11YTZrZzJnamVhcnA0a21kMGsxcGZ0cCIsImV2ZW50X2lkIjoiMDU5ODE3ZmMtMzI0MC0xMWU5LThlNjQtMmI3MzdjMTcxMWZlIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE1NTAzNTg2MTYsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1ub3J0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1ub3J0aGVhc3QtMV9PR21LV1puQjUiLCJjb2duaXRvOnVzZXJuYW1lIjoiaGthdG8iLCJleHAiOjE1NTAzNjIyMTYsImlhdCI6MTU1MDM1ODYxNn0.nYQ-MzE_yRh4aMGdCLeEP0G1ILpZkDdPS4ZYh0jFZu5L5P2vj1SPinl4ovT0YH8AW4kL5qDOO4XA14tVxZmHiofcnaMjjIwHxhFPCXqwytXNU8Qs1PajFtL-pHhWJ8FtG-qLdbmUjweyJ7-pPYm5y_H3ARQTbwHLtLiPPr3Rq2mU7vmAIj8fdN4ANdCLRhj7lnFCvuJn6rRhyDdlVFruNUV_EqyfhpOdUEWv8H1wLcJHiBWcJI1aCzKyluZhuE_MfY-QgHsEvMHZtyGN9H5sO0VnSBUBMgWS7t8qYoe0z4WENukoR1eCRIKJwZKxVlUeAzkKTQv7bRYZcAz-Kbh1gA (string, required) - 認証トークン
 
    + Attributes
        + title: Test Title (string, required) - タイトル
        + content: Test Content (string, required) - 内容
        + due_Date: 1550288140777 (number, required) - 期限日（タイムスタンプ型）
        + status: New (string, required) - ステータス
 
+ Response 200 (application/json)
 
    + Attributes
        + result (required)
        + errors (required)
        + data (required)
            + title: Test Title (string, required) - タイトル
            + content: Test Content (string, required) - 内容
            + due_date: 1550288140777 (number, required) - 期限日（タイムスタンプ型）
            + status: New (string, required) - ステータス種別(New:新規, WIP:作業中, Done:完了, Pending:保留 )