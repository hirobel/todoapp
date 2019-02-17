# todoapp

# how to test(local)
``
$ cd  
``
# how to test(remote)
``
$ cd 4_src/2_server/remote_test_todos
$ test.sh {id_token}
``

## how to get id_token
・事前順部
管理者に、cognitoのユーザプールに認証情報を追加してもらう
test.phpを起動する
```
$ php -S localhost:9999
```

・ブラウザアクセス
https://todoapp.auth.ap-northeast-1.amazoncognito.com/oauth2/authorize?response_type=token&client_id=5dmua6kg2gjearp4kmd0k1pftp&redirect_uri=http://localhost:9999/test.php

・ID、パスワードを入力

・リダイレクト先でid_tokenが表示される