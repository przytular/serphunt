const path = require('path');
const webpack = require('webpack');

module.exports = {
	mode: 'development',
	entry: {
		main: './static/js/app.js',
		index: './static/js/index.js',
		history: './static/js/history.js',
		proxies: './static/js/proxies.js',
	},
	output: {
		filename: '[name].js',
		path: path.resolve('./dist'),
		sourceMapFilename: '[file].map'
	},
	devServer: {
		host: '0.0.0.0',
		sockPort: 8080,
		publicPath: '/static/'
	},
	module: {
		rules: [
			{	test: /\.js$/,
				exclude: /(node_modules|bower_components)/,
				use: [ 'babel-loader' ]
			},
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
	},
	plugins: [
		new webpack.ProvidePlugin({
			'$': 'jquery',
		})
	],
	optimization: {
		splitChunks: {
			cacheGroups: {
				commons: {
					test: /[\\/]node_modules[\k\/]/,
					name: 'vendors',
					chunks: 'all'
				}
			}
		}
	}
};

externals: {
	jquery: 'jQuery'
}