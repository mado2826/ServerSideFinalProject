import { GoogleLogin } from "@react-oauth/google"

export default function Login({onLogin}) {
    const handleSuccess = async (response) => {
        const res = await fetch("http://localhost:5000/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ credential: response.credential })
        })
        const data = await res.json()
        if (res.ok) {
            localStorage.setItem("token", data.token)
            onLogin(data)
        } else {
            alert(data.error)
        }
        
    }

    return <GoogleLogin onSuccess={handleSuccess} onError={() => alert("Login failed")} />
}