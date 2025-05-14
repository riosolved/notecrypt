<template>
    <div>
        <input v-model="form.email" placeholder="Email" />
        <input type="password" v-model="form.password" placeholder="Password" />

        <button @click="enter">Enter</button>
        <button @click="register">Register</button>


        <!--
        <form @submit.prevent="enter">
            <input v-model="form.email" placeholder="Email" />
            <input type="password" v-model="form.password" placeholder="Password" />
            <button type="submit">Log In</button>
        </form>
        -->
    </div>
</template>

<script setup>
import axios from 'axios';
import { reactive, defineEmits } from 'vue';

const emit = defineEmits([
    'entered',
    'registered'
]);

const form = reactive({
    email: '', 
    password: ''
})

const enter = async () => {
    axios.post(
        "https://api.localhost/api/enter",
        {
            email: form.email,
            password: form.password,
        },
        {
            withCredentials: true,
        }
    ).then((response) => {
        console.log("DEBUG::enter::response.data", response.data);

        emit('entered');
    }).catch((error) => {
        console.log("DEBUG::enter::error", error);
    });
}

const register = async () => {
    axios.post(
        "https://api.localhost/api/register",
        {
            email: form.email,
            password: form.password,
        }
    ).then((response) => {
        console.log("DEBUG::enter::response.data", response.data);

        emit('registered');
    }).catch((error) => {
        console.log("DEBUG::enter::error", error);
    });
}
</script>
