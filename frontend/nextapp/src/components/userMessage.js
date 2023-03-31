import styles from '../styles/Login.module.css'

const UserMessage = ({ message }) => {
    return (
        <div className={styles.message}>
        <p>{message ? message : 'fuckshit of a fuckshit'}</p><p>X</p>
        </div>
    );
}

export default UserMessage