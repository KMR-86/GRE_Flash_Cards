<template>
    <div>
        <!--<h3>{{ test_msg }}</h3> -->
        <div v-bind:key="word.id" v-for="word in words">
            <h3>{{word.word}}</h3>
        </div>
    </div>
</template>

<script>
export default {
    name: "flashcard",
  props: ["words"]
  
}
</script>

<style scoped>

</style>