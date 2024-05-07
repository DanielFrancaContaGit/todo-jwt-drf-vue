import { defineStore } from "pinia";
import { ref } from "vue";
import jwtDecode from 'jwt-decode'

interface TokenValues {
    exp: number,
    iat: number,
    jti: string,
    token_type: string,
    user_id: number,
}


export const useAuthStore = defineStore('authentication', () => {
    const token = ref('')
    const isAuthenticate = ref(false)
    const userId = ref(0)

    function setToken(userToken: string) {
        token.value = userToken
        isAuthenticate.value = true
        const decode: TokenValues = jwtDecode(userToken)
        userId.value = decode.user_id
    }

    function cleanToken() {
        token.value = ''
        isAuthenticate.value = false
    }

    return { token, userId, isAuthenticate, setToken, cleanToken }
})