/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'nav': '#E6ECFF'
      },
      height: {
        "view": "calc(100vh - 56px)"
      }
    },
  },
  plugins: [],
}
