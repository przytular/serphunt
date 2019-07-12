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
				test: /\.css$/,
				use: [
					'style-loader',
					'css-loader'
				]
			},
			{
				test: /\.(png|svg|jpg|gif)$/,
				use: [
					'file-loader'
				]
			},
			{
			test: /\.(scss)$/,
			use: [
				'style-loader',
				'css-loader',
				'sass-loader',
				{
					loader: 'postcss-loader',
					options: {
						plugins: function () {
						return [
							require('autoprefixer')
						];
						}
					}
				}
			]
			}
		]
	}
};

externals: {
  jquery: 'jQuery'
}