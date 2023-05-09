<template>
  <div>
    <TodoListItem v-for = "(todo,index) in todos" :key='index' :todoitem="todo"/>
    <!-- :todoitem=todo ==> 부모가 자식에게 데이터를 내려준다 -->
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
  name : 'TodoList',
  components:{
    TodoListItem,
  },
  computed:{
    todos() {
      return this.$store.state.todos
    }
  }
}
</script>

<style>

</style>