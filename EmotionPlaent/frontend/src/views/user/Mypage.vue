<template>
  <section id="mypage-container" v-if="userInfo">
    <side-profile-card :user-info="userInfo" />
    <article id="profile-container">
      <img id="profile-img" :src="userInfo.profileImg">
      <div id="profile-card">
        <div id="name-card">
          <h1>{{ userInfo.nickname }}</h1>
          <button v-if="isMypage" @click="$router.push({name: 'Setting'})">프로필 수정</button>
          <div v-else>
            <button v-if="!isFollow" id="follow" @click="follow">팔로우</button>
            <button v-else id="unfollow" @click="follow">언팔로우</button>
          </div>
        </div>
        <div id="info">
          <h4 id="intro" style="color: #777777; font-size: 1.2rem; font-weight: bold;">{{ userInfo.intro }}</h4>
          <br>
          <div id="info-card">
            <h3>이야기 {{userInfo.feedCount }}</h3>
            <h3 @click="showFollowerList" v-if="followers" style="cursor: pointer;">팔로워 {{ followers.length }}</h3>
            <h3 @click="showFollowingList" v-if="followings" style="cursor: pointer;">팔로우 {{ followings.length }}</h3>
          </div>
        </div>
      </div>
    </article>
    <article id="tab">
      <span id="dot1" :class="pageTab == 'feed' ? 'slide-out':'slide-in'" />
      <p id="tab_dot" @click="changeTab('feed')" :class="pageTab == 'feed' ? 'activate': ''">이야기</p>
      <p id="tab_dot" @click="changeTab('pick')" :class="pageTab == 'pick' ? 'activate': ''">찜 목록</p>
    </article>
    <article id="list-container">
      <router-view/>
    </article>
  </section>  
</template>

<script>
import SideProfileCard from '@/components/SideProfileCard.vue'
import axios from 'axios'

const session = window.sessionStorage

export default {
  name: 'Mypage',
  components: {SideProfileCard},
  data() {
    return {
      userInfo: null,
      followers: null,
      followings: null,
      pageTab: 'feed',
      filter: 0,
    }
  },
  props: {
    userId: Number,
  },
  methods: {
    changeTab(tap){
      this.pageTab = tap
      if (this.$route.path.includes('item')){
        this.$router.push({ path: `/user/${this.userInfo.no}/${tap}` })
      }
      else {
        this.$router.push({ path: `${tap}`})
      }
    },
    showFollowerList: function () {
      this.$store.commit('mypagefollowerListActivate', this.followers)
    },
    showFollowingList: function () {
      this.$store.commit('mypagefollowingListActivate', this.followings)
    },
    follow() {
      let method = 'post'
      if (this.isFollow){
        method = 'delete'
      }
      let headers = {
        'at-jwt-access-token': session.getItem('at-jwt-access-token'),
        'at-jwt-refresh-token': session.getItem('at-jwt-refresh-token'),
      };
      let data = {
        sender : JSON.parse(window.sessionStorage.getItem('userInfo')).no,
        receiver : Number(this.userId),
      };
      console.log(data, method)
      axios({
        method: method,
        url: '/api/follows',
        data: data, // post 나 put에 데이터 넣어 줄때
        headers: headers,  // 넣는거 까먹지 마세요
      })
      .then((res) => {
      console.log("팔로우 성공")
      console.log(res.data)
      this.$store.dispatch('follow', Number(this.userId))
      })
      .catch((error) => {
        console.log("팔로우 실패")
        console.log(error);
      })
      .finally(() => {
        this.getFollowData()
      })
    },

    getFollowData: function () {
      const headers = {
        'at-jwt-access-token': session.getItem('at-jwt-access-token'),
        'at-jwt-refresh-token': session.getItem('at-jwt-refresh-token'),
      };

      axios({
        method: 'get',
        url: `/api/follows/${this.$store.state.userInfo.no}/${this.userInfo.no}`,
        headers: headers,  // 넣는거 까먹지 마세요
      })
      .then(res => {
        console.log("팔로우 정보 가져오기 성공")
        console.log(res.data)
        this.followers = res.data.follower
        this.followings = res.data.following
        this.$store.dispatch('accessTokenRefresh', res) // store에서
      })
      .catch(() => {console.log('팔로우 에러')})
    },
    getFeedData: function(){

      const headers = {
        'at-jwt-access-token': session.getItem('at-jwt-access-token'),
        'at-jwt-refresh-token': session.getItem('at-jwt-refresh-token'),
      };

      axios({
        method: 'get',
        url: `/api/feeds/my/${this.userInfo.no}`,
        headers: headers,  // 넣는거 까먹지 마세요
      })
      .then(res => {
        console.log("피드 가져오기 성공")
        console.log(res.data)
        this.feeds = res.data
        this.$store.dispatch('accessTokenRefresh', res)
      })
      .catch(() => console.log('피드 에러'))
    }
  },
  computed:{
    isMypage(){
      if (this.$route.path.includes('mypage')){
        return true
      }
      return false
    },
    isFollow(){
      let result = false
      if (this.followers){
        this.followers.forEach(ele => {
          if (ele.no == JSON.parse(window.sessionStorage.getItem('userInfo')).no){
            result = true
          }
        })
      }
      return result
    }
  },
  created() {
    console.log('프롭임', this.userId)
    if (this.$route.params.userId){
      const headers = {
        'at-jwt-access-token': session.getItem('at-jwt-access-token'),
        'at-jwt-refresh-token': session.getItem('at-jwt-refresh-token'),
      };

      axios({
        method:'get',
        url:`/api/users/${this.userId}`,
        headers: headers,
      })
      .then(res => {
        if(res.headers['at-jwt-access-token'] != session.getItem('at-jwt-access-token')){
          session.setItem('at-jwt-access-token', "");
          session.setItem('at-jwt-access-token', res.headers['at-jwt-access-token']);
          console.log("Access Token을 교체합니다!!!")
        }
        this.userInfo = res.data
        console.log(this.userInfo)
      })
      .then(() => {
        this.getFollowData() // 팔로우 데이터
      })
      .then(() => {
        this.getFeedData() // 피드 데이터
      })
      .catch(error => console.log('안되네', error))
      .finally(() => this.$store.commit('load', false))
    }
    else {
      const myInfo = function(){
        return new Promise(resolve => resolve())
      }
      myInfo()
      .then(() => {
        this.userInfo = JSON.parse(session.getItem('userInfo'))
      })
      .then(() => {
        this.getFollowData()
      })
      .then(() => this.getFeedData())
      .catch(err => console.log(err))
      .finally(() => {this.$store.commit('load', false)})
    }
  },
  mounted(){
    const path = this.$route.path
    console.log('좀 돼라 ㅋㅋ')
    if (path.includes('item') || path.includes('pick')){
      this.pageTab = 'pick'
    }
  },
}
</script>

<style scoped>
  h1 {
    color: black;
    font-size: 2rem;
    font-weight: bold;
  }

  h3 {
    color: black;
    font-size: 1.2rem;
    font-weight: bold;
    line-height: 100%;
    letter-spacing: 0.05rem;
    margin: 0;
  }

  p {
    color: #777777;
    font-size: 1.2rem;
    font-weight: bold;
    margin: 0 1rem;
    cursor: pointer;
  }
  label {
    color: #5E39B3;
    font-size: 1.125rem;
    font-weight: bold;
    letter-spacing: -0.5px;
    margin-left: 0.5rem;
  }

  button {
    background-color: #5E39B3;
    color: white;
    font-size: 1rem;
    font-weight: bold;
    border: none;
    border-radius: 20px;
    padding: 0.41rem 0.45rem;
    margin-bottom: 0.1rem;
    cursor: pointer;
    line-height: 1rem;
  }

  input {
    border: 2px #5E39B3 solid;
    border-radius: 20px;
    width: 35vh;
    min-width: 350px;
    height: 4vh;
    min-height: 40px;
    padding: 0.75rem;
    font-size: 1rem;
    font-weight: bold;
  }

  #mypage-container {
    width: 50%;
    min-width: 700px;
    min-height: 100vh;
    margin: auto;
    border-left: 1px solid #cccccc;
    border-right: 1px solid #cccccc;
    background-color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
  }

  #profile-container {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    width: 90%;
    padding: 2rem 1rem;
  }

  #profile-img {
    width: 20%;
    height: inherit;
    aspect-ratio: 1/1;
    border-radius: 50%;
  }

  #profile-card {
    width: 60%;
  }

  #name-card {
    display: flex;
    direction: row;
    justify-content: space-between;
    align-items: center;
    margin-top: 0.2rem;
    margin-bottom: 0rem;
    width: 100%;
  }
  
  #info-card {
    display: flex;
    direction: row;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-top: 1.4rem;
  }
  
  #card {
    display: flex;
    flex-direction: row;
    justify-content: center;
  }

  #tab {
    display: flex;
    justify-content: center;
    align-items: flex-end;
    position: relative;
    border-top: 1px solid gainsboro;
    width: 100%;
    padding: 1rem;
  }

  #dot1 {
    width: 18px;
    height: 18px;
    border-radius: 50%;
    position: absolute;
    top: -15%;
    left: 44%;
    background-color: #5E39B3;
  }

  #list-container {
    width: 100%;
    display: flex;
    justify-content: center;
  }

  @keyframes slide-in {
    from {left: 44%;}
    to {left: 54%;}
  }

  @keyframes slide-out {
    from {left: 54%;}
    to {left: 44%;}
  }

  .slide-in {
    animation: slide-in 0.5s ease-out forwards;
  }
  #short_comment {
    text-align: left;
  }
  #my_comment {
    font-size: 1.1rem;
    font-weight: bold;
  }
  .slide-out {
    animation: slide-out 0.5s ease-out forwards;
  }

  .activate {
    color: black;
    font-size: 1.3rem;
  }

  #info {
    display: flex;
    flex-direction: column;
  }

  #follow {
    background-color: #5E39B3;
    color: white;
    font-size: 1rem;
    font-weight: bold;
    border-radius: 20px;
    padding: 0.41rem 0.45rem;
    margin-bottom: 0.7rem;
    cursor: pointer;
    line-height: 1rem
  }

  #unfollow {
    background-color: slategray;
    color: white;
    font-size: 1rem;
    font-weight: bold;
    border-radius: 20px;
    padding: 0.41rem 0.45rem;
    margin-bottom: 0.7rem;
    cursor: pointer;
    line-height: 1rem;
  }

</style>
