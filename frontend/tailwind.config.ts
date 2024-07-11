import type { Config } from 'tailwindcss';
const { nextui } = require('@nextui-org/react');

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './node_modules/@nextui-org/theme/dist/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        poppins: ['Poppins', 'sans-serif'],
      },
      colors: {
        customGreen: {
          light: '#85d7ff',
          DEFAULT: '#12B981',
          dark: '#009eeb',
        },
        customYellow: {
          light: '#7bed9f',
          DEFAULT: '#FFC264',
          dark: '#1e8659',
        },
        customRed: {
          light: '#85d7ff',
          DEFAULT: '#E4355B',
          dark: '#009eeb',
        },
      },
    },
  },
  plugins: [nextui()],
};
export default config;
