<template>
	<div id="login_fail">
    <div id="modal">
			<h4><span style="color:red;">이메일</span> 또는 <span style="color:red;">비밀번호</span>를 <br> 다시 확인해주세요</h4>
			<hr>
			<p @click="loginAgain">확인</p>
    </div>
	</div>
</template>

<script>
import { mapState } from 'vuex'

export default {
	methods: {
		loginAgain: function () {
			// console.log('여기옴')
			// console.log(this.$store.state.userInfo)
			this.$store.commit('loginFailModalActivate')
			this.$router.go(0)
		}
	},
	computed: 
		mapState([
			'serverErrorMessage'
		])
}
</script>

<style scoped>
#login_fail {
	display: flex;
	justify-content: center;
	align-items: center;
	width: 100vw;
	height: 100vh;
	background-color: rgb(0, 0, 0, 0.5);
	position: fixed;
	top: 0;
	left: 0;
	z-index: 9999;
}
#modal {
	display: flex;
	flex-direction: column;
	justify-content: center;
	background-color: white;
	border-radius: 20px;
	width: 19rem;
	height: 13rem;
}
p {
	margin: auto;
	font-weight: bold;
	cursor: pointer;
	font-size: 1.3rem;
}
hr {
	margin: 0;
}
h4 {
	margin: auto;
	text-align: center;
	font-weight: bold;
}
</style>