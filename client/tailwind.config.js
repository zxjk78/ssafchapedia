module.exports = {
  content: [
    './public/**/*.html',
    //여기 확장자 앞에 공백이 없어야 함
    "./src/**/*.{html,js,vue}"
  ],
  //darkmode media인데 class로 바꿈: 브라우저 설정이 아니라 css class를 따르겠다
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [],
}
