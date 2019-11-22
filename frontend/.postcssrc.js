// https://github.com/michael-ciniawsky/postcss-load-config

module.exports = {
  "plugins": {
    "postcss-import": {},
    "postcss-url": {},
    // to edit target browsers: use "browserslist" field in package.json
    "autoprefixer": {}
  }//,
  // pages: {
  //   index: {
  //     // entry for the page
  //     entry: 'src/index/main.js',
  //     // the source template
  //     template: 'public/index.html',
  //     // output as dist/index.html
  //     filename: 'index.html',
  //     // when using title option,
  //     // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
  //     title: 'Index Page',
  //     // chunks to include on this page, by default includes
  //     // extracted common chunks and vendor chunks.
  //     chunks: ['chunk-vendors', 'chunk-common', 'index']
  //   },
  //   // when using the entry-only string format,
  //   // template is inferred to be `public/subpage.html`
  //   // and falls back to `public/index.html` if not found.
  //   // Output filename is inferred to be `subpage.html`.
  //   subpage: 'src/subpage/main.js'
  // }
}
