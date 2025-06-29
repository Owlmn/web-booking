"use client";
import { useRouter } from "next/navigation";
import { useAuth } from "../../shared/store";
import styles from "./Footer.module.css";

export default function Footer() {
    const router = useRouter();
    const { user } = useAuth();

    return (
        <div className={styles.footer}>
            <div className={styles.container}>
                <div className={styles.footerSection}>
                    <h3>О нас</h3>
                    <p>Мы помогаем жителям и гостям Владивостока находить лучшие рестораны города и наслаждаться изысканной кухней</p>
                </div>
                <div className={styles.footerSection}>
                    <h3>Навигация</h3>
                    <ul>
                        <li><button onClick={() => router.push("/restaurants")}>Рестораны</button></li>
                        {user && <li><button onClick={() => router.push("/bookings")}>Мои брони</button></li>}
                        {!user && <li><button onClick={() => router.push("/login")}>Войти</button></li>}
                    </ul>
                </div>
                <div className={styles.footerSection}>
                    <h3>Контакты</h3>
                    <p>📧 mistrekov.sr@students.dvfu.ru</p>
                    <p>📞 +7 (923) 582-12-85</p>
                </div>
            </div>
            <div className={styles.footerBottom}>
                <div className={styles.container}>
                    <p>&copy; 2024 Рестораны Владивостока. Все права защищены.</p>
                </div>
            </div>
        </div>
    );
} 