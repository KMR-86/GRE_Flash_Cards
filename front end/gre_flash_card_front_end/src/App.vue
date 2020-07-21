<template>
  <div id="app">
    <flashcard v-bind:words="words"/>
  </div>
</template>

<script>
import flashcard from './components/flashcard.vue'
import axios from 'axios'
export default {
  name: 'App',
  components: {
    flashcard
  },
  data(){
      return{
        words:[

      ]
      }
  },
  mounted(){
  var vm = this
      axios.get("http://127.0.0.1:8000/get_all_words/").then(response=>{
          vm.words=response.data;
          console.log(vm.words);
      }).catch(function(error){
          console.log('erros : ',error);
      })  
  },

  methods:{

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
  margin-top: 5px;
}
</style>
