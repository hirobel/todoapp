###############
# Test > Create
###############

curl -X POST \
  https://zm7ajk3pk4.execute-api.ap-northeast-1.amazonaws.com/dev/todos \
  -H "Authorization: $1" \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{ 
            "title": "Test Title",
            "content": "Test Content",
            "due_date": 1550288140777,
            "status": "New"
      }' \
> result/create-testValidateInput1.json

curl -X POST \
  https://zm7ajk3pk4.execute-api.ap-northeast-1.amazonaws.com/dev/todos \
  -H "Authorization: $1" \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{ 
            "content": "Test Content",
            "due_date": 1550288140777,
            "status": "New"
      }' \
> result/create-testValidateInput2.json

curl -X POST \
  https://zm7ajk3pk4.execute-api.ap-northeast-1.amazonaws.com/dev/todos \
  -H "Authorization: $1" \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{ 
            "title": "",
            "content": "Test Content",
            "due_date": 1550288140777,
            "status": "New"
      }' \
> result/create-testValidateInput3.json



###############
# Test > Update
###############
targetid=`cat result/create-testValidateInput1.json | tr -d ' "[]{}' | awk -F: '{ print $5 }' | cut -d "," -f 1`

curl -X PUT \
  "https://zm7ajk3pk4.execute-api.ap-northeast-1.amazonaws.com/dev/todos/hogehogeupdate" \
  -H "Authorization: $1" \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
            "title": "Test Title Modified1",
            "content": "Test Content",
            "due_date": 1550288140777,
            "status": "New"
      }' \
> result/update-testValidateInput2.json

curl -X PUT \
  "https://zm7ajk3pk4.execute-api.ap-northeast-1.amazonaws.com/dev/todos/$targetid" \
  -H "Authorization: $1" \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
            "title": "Test Title Modified2",
            "content": "Test Content",
            "due_date": 1550288140777,
            "status": "New"
      }' \
> result/update-testValidateInput1.json


###############
# Test > Delete
###############
# targetid=`cat result/create-testValidateInput1.json | tr -d ' "[]{}' | awk -F: '{ print $5 }' | cut -d "," -f 1`

curl -X DELETE \
  "https://zm7ajk3pk4.execute-api.ap-northeast-1.amazonaws.com/dev/todos/hogehogedelete" \
  -H "Authorization: $1" \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
> result/delete-testValidateInput2.json

curl -X DELETE \
  "https://zm7ajk3pk4.execute-api.ap-northeast-1.amazonaws.com/dev/todos/$targetid" \
  -H "Authorization: $1" \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
> result/delete-testValidateInput1.json


###############
# Test > Read
###############
curl -X GET \
  https://zm7ajk3pk4.execute-api.ap-northeast-1.amazonaws.com/dev/todos \
  -H "Authorization: $1" \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
> result/read-testValidateInput1.json
