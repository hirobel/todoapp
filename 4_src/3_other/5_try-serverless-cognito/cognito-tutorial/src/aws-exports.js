import Amplify from 'aws-amplify'
Amplify.configure({
  Auth: {
    // フェデレーションアイデンティティのID
    identityPoolId: 'ap-northeast-1:40af0582-a748-4d9a-8c96-3ef788e9d492',
    // リージョン
    region: 'ap-northeast-1',
    // ユーザープールのID
    userPoolId: 'ap-northeast-1_OGmKWZnB5',
    // ユーザープールのウェブクライアントID
    userPoolWebClientId: '5dmua6kg2gjearp4kmd0k1pftp',
    mandatorySignIn: true
  },
  API: {
    endpoints: [
      {
        name: 'cognito-tutorial-api',
        endpoint: 'https://zm7ajk3pk4.execute-api.ap-northeast-1.amazonaws.com/'
      }
    ]
  }
})