import React from "react";
import { NavLink } from "react-router-dom";
import s from './MainPage.module.scss'
import { CategoriesCard } from "../../Cards/CategoriesCard/CategoriesCard";
import axios from "axios";
import { useState } from "react";
import { useEffect } from 'react';

export const MainPage = () => {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        axios.get("http://95.163.240.234:8000/api/categories").then((response) => {
            setUsers(response.data.data);
        });
    }, []);
    return (
        <div className={s.wrapper}>
            <div className={s.imgcontent}>
                <div className={s.text}>Оставьте все <br />заботы нам</div>
                <div className={s.textin}>
                    <div>
                        <input type="text" />
                    </div>
                    <div className={s.input}>Поиск</div>
                </div>
            </div>
            <div className={s.textcat}>
                Категории Исполнителей
            </div>
            <div className={s.wrappercard}>
                {users.map((user) => (
                    <CategoriesCard users={user} />
                ))}
            </div>
            <div className={s.textcat}>
                Как работает SkillMatch?
            </div>
            <div className={s.wrappercardinfo}>
                <div className={s.cardinfo1}></div>
                <div className={s.cardinfo2}></div>
                <div className={s.cardinfo3}></div>
            </div>
            <div className={s.textcardinfo}>
                <div className={s.cardtext}>Опишите задачу</div>
                <div className={s.cardtext}>Получите отклики</div>
                <div className={s.cardtext}>Выберите исполнителя</div>
            </div>
        </div >
    )
}