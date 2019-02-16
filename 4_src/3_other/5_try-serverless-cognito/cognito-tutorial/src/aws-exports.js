import Amplify from 'aws-amplify'
Amplify.configure({
  Auth: {
    // フェデレーションアイデンティティのID
    identityPoolId: 'ap-northeast-1_X6BzBBoUo',
    // リージョン
    region: 'ap-northeast-1',
    // ユーザープールのID
    userPoolId: 'ap-northeast-1_X6BzBBoUo',
    // ユーザープールのウェブクライアントID
    userPoolWebClientId: '7pji25gih5n75ir50h3ph5a421',
    mandatorySignIn: true
  },
  API: {
    endpoints: [
      {
        name: 'cognito-tutorial-api',
        endpoint: 'https://arws51ov2f.execute-api.us-east-1.amazonaws.com'
      }
    ]
  }
})