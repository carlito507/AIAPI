import styles from '../../styles/Login.module.css'
import UserMessage from "@/components/userMessage"

const Login = () => {
    return (
        <div className={styles.container}>
            <UserMessage />
            <div className={styles.login_box}>
                <h1>Login</h1>
                <form>
                    <div className={styles.input_box}>
                        <label>Username</label>
                        <input type="text" name="username" required />
                        <label>Password</label>
                        <input type="password" required/>
                    </div>
                    <div className={styles.left_aligned}>
                        <a href="/password-reset">forgot password?</a>
                    </div>
                    <button type="submit">Login</button>
                    <a className="mem" href="/register">not a member?</a>
                </form>

            </div>
        </div>
    )
}

export default Login