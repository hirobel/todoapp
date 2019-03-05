import Amplify from 'aws-amplify'
Amplify.configure({
  Auth: {
    // フェデレーションアイデンティティのID
    identityPoolId: 'ap-northeast-1_SMs7PL98T',
    // リージョン
    region: 'ap-northeast-1',
    // ユーザープールのID
    userPoolId: 'ap-northeast-1_SMs7PL98T',
    // ユーザープールのウェブクライアントID
    userPoolWebClientId: '2t08gp4v20cpdsm8qvbsebmne',
    mandatorySignIn: true
  },
  API: {
    endpoints: [
      {
        name: 'cognito-tutorial-api',
        endpoint: 'https://htl40rznca.execute-api.ap-northeast-1.amazonaws.com/prod/todos'
      }
    ]
  }
})