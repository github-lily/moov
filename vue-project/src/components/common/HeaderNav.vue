<template>
  <div>
    <div class="container">
      <nav class="navbar navbar-expand-lg bg-body-tertiary" >

        <div class="container-fluid">
          <a class="navbar-brand" href="#">MOOV.</a>
          
          <!-- 화면 줄어들 때 -->
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>

          <div class="collapse navbar-collapse" id="navbarSupportedContent">

            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link" aria-current="page" href="#" >홈</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">내가 찜한 리스트</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#" >마이페이지</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#" >로그아웃</a>
              </li>
            </ul>

            <!-- 검색 창 -->
            <form class="d-flex" role="search">
              <input class="movieSearch" placeholder="영화를 검색해보세요!">
              <button class="btn" type="submit">
                <i class="fas fa-search"></i>
              </button>
            </form>
          </div>

        </div>

      </nav>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>

/* nav bar */
body {
  position: relative;
}

.contanier {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.navbar {
  width: 100%;
  height: 45px;
  margin: 20px 0px;
  border-radius: 50px; 
  padding-left: 50px;
  padding-right: 50px;
  background-color: red;
}

.bg-body-tertiary {
  background-color: rgb(255, 255, 115) !important; 
}

.navbar-brand {
  font-size: 20px;
  font-family: 'Krona One';
  font-weight: bold;
  margin-right: 50px;
}

.nav-link {
  font-family: 'Noto Sans KR';
}

.movieSearch {
  border: none;
  border-bottom: 1px solid gray;
  width: 100%;
  text-align: center;
  background-color: transparent;
  font-family: 'Noto Sans KR';
}

.movieSearch:focus {
  border: none ;
  border-bottom: 1px solid gray;
  outline: none;
}

</style>