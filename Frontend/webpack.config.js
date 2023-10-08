module.exports = {
    entry: './index.js',
    output: {
      filename: './bundle.js'
    },
    module: {
      rules: [
        {
          test: require.resolve('jsdom'),
          loader: 'expose-loader',
          options: {
            exposes: 'JSDOM'
          }
        }
      ]
    }
  };