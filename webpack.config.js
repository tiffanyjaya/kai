let debug = process.env.NODE_ENV !== "production";
let webpack = require("webpack");

module.exports = {
    context: __dirname,
    devtool: debug ? "inline-source-map" : false,
    entry: "./kai/MainEntry.js",
    output: {
        path: __dirname + "/public",
        filename: "kai.min.js"
    },
    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                exclude: /(node_modules|bower_components)/,
                loader: "babel",
                query: {
                    presets: ["react", "es2017"]
                }
            }
        ]
    },
    resolveLoader: {
        moduleExtensions: ["-loader"]
    },
    plugins: debug ? [] : [
        new webpack.optimize.OccurrenceOrderPlugin(),
        new webpack.optimize.UglifyJsPlugin({mangle: false, sourcemap: false})
    ]
}