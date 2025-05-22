<template>
    <div id="form">
        <div class="block">
            <span class="title">Email</span>

            <input type="text" v-model="form.email" placeholder="a@b.com" />
        </div>

        <button type="button" @click="enter">Send Reset</button>

        <div class="navigate" @click="navigate">
            <- Back
        </div>
    </div>
</template>

<script setup>
    import { reactive, defineEmits } from 'vue';

    const emit = defineEmits([
        'navigate_to_door'
    ]);

    const form = reactive({
        email: ''
    });

    const navigate = () => {
        emit('navigate_to_door')
    };
</script>
