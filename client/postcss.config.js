module.exports = {
  // postcss 플러그인이라 vendor prefix를 자동으로 추가해준다. webkit-moz, webkit-ms 등의 브라우저별 사양이 조금씩 차이가 있는데 
  // 개발자는 기본 css만 넣어주면 이 플러그인이 브라우저별 css를 넣어줌
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
  ],
}