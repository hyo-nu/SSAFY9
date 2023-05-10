<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <header>
      <h1><b>버튼 박스 제작</b></h1>
    </header>
    <section>
      <h2>예약 페이지</h2>
      <h3>시간 선택</h3>
      <div class="time-table">
        <span v-for="(time,index) in times" :key = "index" class="time" :class="{selected:isSelected(time)}" @click="selectTime(time)">
          {{time}}
        </span>    
      </div>
      <div class="divider"></div>
      <div class="select-table">
        선택시간 : <span v-for="(time,index) in selectTimes" :key="index">{{time}}</span>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      selectTimes: [],
    }
  },
  methods:{
    isSelected(time){
      return this.selectTimes.includes(time)
    },
    selectTime(time){
      const idx = this.selectTimes.indexOf(time)
      if(idx < 0){
        if(this.selectTimes.length === 5){
          alert("5타임까지만 신청할 수 있습니다.")
        }
        this.selectTimes.push(time)
      }else{
        this.selectTimes.splice(idx, 1)
      }
    }
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
header{
  text-align: center;

}
section{
  display:flex;
  flex-direction: column;
  align-items: center;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
}
.divider{
  border-bottom: 2px solid #0F4C81;
  width: 80%;
}
.time-table{
  width: 560px;
  display: flex;
  flex-wrap:wrap
}
.time{
  width: 80px;
  margin-bottom: 10px;
  text-align: center;
}
.time:hover {
  cursor:pointer;
  background-color: #658dc63d;
}
.selected{
  background-color: #658dc63d;
}

</style>
