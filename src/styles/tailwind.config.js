module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
        extend: {
          backgroundImage: theme => ({
           'layal-hero': "url('./images/LayalLiverpool3.jpg')",
          })
        }
      },
  variants: {
    extend: {},
  },
  plugins: [],
}
