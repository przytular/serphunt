var path = require('path');
var webpack = require('webpack');

module.exports = {
	mode: 'development',
	entry: './static/js/app.js',
	output: {
		filename: 'main.js',
		path: path.resolve('./dist')
	},
	devServer: {
		host: '0.0.0.0',
		sockPort: 8080,
		publicPath: '/static/'
	},
	module: {
		rules: [
			{
			test: /\.(scss)$/,
			use: [
				{
					loader: 'style-loader'
				},
				{
					loader: 'css-loader'
				},
				{
					loader: 'postcss-loader',
					options: {
						plugins: function () {
						return [
							require('autoprefixer')
						];
						}
					}
				},
				{
					loader: 'sass-loader'
				}
			]
			}
		]
	}
};
