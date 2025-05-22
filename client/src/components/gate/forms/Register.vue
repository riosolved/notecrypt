<template>
    <div
        id="form"
        v-if="mode === MODES.REGISTER"
    >
        <div class="block">
            <span class="title">Email</span>

            <input type="text" v-model="form.email" placeholder="a@b.com" />
        </div>

        <div class="block">
            <span class="title">Password</span>

            <input type="password" v-model="form.password" />
        </div>

        <button type="button" @click="register">Register</button>
    </div>

    <div
        v-else-if="mode === MODES.CONFIRM"
    >
        <h1>Account created!</h1>
        <span>An activation link has been sent.</span>

        <span>Back to log-in</span>

        <span @click="confirm">Re-send activation link</span>

        <span>Contact Support</span>
    </div>
</template>

<script setup>
import axios from 'axios';
import { reactive, defineEmits, ref } from 'vue';

const MODES = {
    REGISTER: 'register',
    CONFIRM: 'confirm',
}

// const emit = defineEmits([
//     'registered'
// ]);

const form = reactive({
    email: '', 
    password: ''
});

const mode = ref(MODES.REGISTER);

const register = async () => {
    axios.post(
        "https://api.localhost/api/register",
        {
            email: form.email,
            password: form.password,
        }
    ).then((response) => {
        console.log("DEBUG::register::response.data", response.data);

        // emit('registered');

        mode = MODES.CONFIRM;
    }).catch((error) => {
        console.log("DEBUG::register::error", error);
    });
}

const confirm = () => {
    axios.get(
        `https://api.localhost/api/confirm?email=${email}`,
    )
}
</script>
