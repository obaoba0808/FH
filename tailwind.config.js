/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html",
    "./**/*.html"
  ],
  safelist: [
    // Dynamic classes that might be missed
    'bg-midnight',
    'bg-bgStart',
    'bg-bgEnd',
    'text-electricPurple',
    'text-neonPink',
    'text-violetBlue',
    'text-textWhite',
    'border-electricPurple',
    'border-neonPink',
    'from-electricPurple',
    'to-neonPink'
  ],
  theme: {
    extend: {
      colors: {
        midnight: '#0D0616',
        bgStart: '#0F0A1A',
        bgEnd: '#2A0E3F',
        electricPurple: '#7B2CFF',
        neonPink: '#FF2DAF',
        violetBlue: '#6A5CFF',
        textWhite: '#F5F3FF',
      },
      fontFamily: {
        sans: ['"Noto Sans TC"', 'sans-serif'],
        display: ['"Syncopate"', 'sans-serif'],
      },
      animation: {
        'glowing': 'glowing 20s linear infinite',
        'float': 'float 6s ease-in-out infinite',
      },
    },
  },
  plugins: [],
}
